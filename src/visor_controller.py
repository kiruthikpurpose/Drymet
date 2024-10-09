class VisorController:
    def __init__(self):
        self.heating_enabled = False
        self.auto_dimming_enabled = False

    def check_conditions(self):
        if self.should_heat():
            self.enable_heating()
        if self.should_dim():
            self.enable_auto_dimming()

    def should_heat(self):
        return True

    def enable_heating(self):
        self.heating_enabled = True

    def should_dim(self):
        return True

    def enable_auto_dimming(self):
        self.auto_dimming_enabled = True
