class VentilationSystem:
    def __init__(self):
        self.airflow_enabled = False

    def manage_airflow(self):
        if self.should_enable_airflow():
            self.enable_airflow()

    def should_enable_airflow(self):
        return True

    def enable_airflow(self):
        self.airflow_enabled = True
