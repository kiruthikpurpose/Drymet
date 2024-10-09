class DisplayController:
    def __init__(self):
        self.alerts = []

    def update_display(self):
        self.check_alerts()
        self.show_alerts()

    def check_alerts(self):
        self.alerts.append("Alert: Vehicle approaching")

    def show_alerts(self):
        for alert in self.alerts:
            print(alert)
        self.alerts.clear()
