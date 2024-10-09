class BatteryManagement:
    def __init__(self):
        self.battery_level = 100

    def monitor_battery(self):
        self.check_battery()

    def check_battery(self):
        if self.battery_level < 20:
            print("Warning: Battery low")
