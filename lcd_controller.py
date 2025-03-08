from RPLCD.i2c import CharLCD
import psutil
import time
from jtop import jtop, JtopException

# Initialize LCD
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=7,
    cols=16,
    rows=2
)

def get_system_metrics():
    """Fetch system metrics: CPU, RAM, Disk, Temperature, GPU."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent  # Get disk usage

    # Get Jetson CPU temperature
    try:
        with open("/sys/devices/virtual/thermal/thermal_zone0/temp", "r") as f:
            temp = round(int(f.read()) / 1000, 1)  # Convert to Celsius
    except FileNotFoundError:
        temp = "Err"

    # Get Jetson GPU usage
    gpu_usage = "N/A"
    try:
        with jtop() as jetson:
            gpu_usage = jetson.stats["GPU"]

    except JtopException:
        gpu_usage = "GPU stats not available" # Ensure gpu usage always has a value

    return cpu_usage, ram_usage, disk_usage, temp, gpu_usage

def display_metrics():
    """Continuously update LCD with system metrics."""
    while True:
        cpu, ram, disk, temp, gpu = get_system_metrics()

        # Define 4 different screens
        screens = [
            'Welcome, Paul.',  # Custom Message
            f"CPU:{cpu:.1f}%\n\rRAM:{ram:.1f}%",
            f"Disk:{disk:.1f}%\n\rTemp:{temp}C",
            f"GPU:{gpu:.1f}%"
        ]

        for screen in screens:
            lcd.clear()
            lcd.write_string(screen)
            time.sleep(2)

try:
    display_metrics()
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("Shutting Down")
    time.sleep(2)
    lcd.clear()
