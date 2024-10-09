from visor_controller import VisorController
from display_controller import DisplayController
from ventilation_system import VentilationSystem
from battery_management import BatteryManagement

def main():
    visor_controller = VisorController()
    display_controller = DisplayController()
    ventilation_system = VentilationSystem()
    battery_management = BatteryManagement()

    while True:
        visor_controller.check_conditions()
        display_controller.update_display()
        ventilation_system.manage_airflow()
        battery_management.monitor_battery()

if __name__ == "__main__":
    main()
