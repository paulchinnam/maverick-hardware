This repo contains scripts for my Nvidia Jetson Orin Nano Mini-based project: 'Maverick.ai'

Maverick is the name of my customized Jetson-based system (see full project blog (yet to be posted))

lcd_controller.py collects and displays hardware metrics from the board using the Jetson-Stats and CharLCD libraries respectively.

## Resources
1. Jetson-Stats Documentation: https://rnext.it/jetson_stats/index.html
2. RPLCD Documentation: https://rplcd.readthedocs.io/en/stable/usage.html

## References for my future self
1. Service file (lcd_telemetry.service) is located under /env/systemd/system/ (NOTE: use sudo to access)
2. Run nano /env/systemd/system/lcd_telemetry.service to open the service file
    a. Run CTRL+x then y then enter in order to save and exit the file after modifications
3. Run the following commands every time you modify the service file (NOTE: all these commands need to be run under sudo)
    a. systemctl daemon-reload (NOTE: reloads systemd)
    b. systemctl enable lcd_telemetry.service (Note: enables service file)
    c. systemctl start lcd_telemetry.service (NOTE: starts service file)
    d. systemctl status lcd_telemetry.service (NOTE: prints status of the service)
    e. Follow these troubleshooting steps if the service has errors
        i. journalctl -u lcd_telemetry.service --no-pager --lines=50 (NOTE: prints service logs)

## TODO
2. Write script to control on and reset buttons
3. Run button script on system startup
