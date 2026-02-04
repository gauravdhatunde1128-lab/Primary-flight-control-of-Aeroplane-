# ---------------------------------------
# PRIMARY FLIGHT CONTROL SIMULATION
# Aileron  -> Roll
# Elevator -> Pitch
# Rudder   -> Yaw
# ---------------------------------------

class Aircraft:
    def __init__(self):
        self.roll = 0.0   # degrees
        self.pitch = 0.0  # degrees
        self.yaw = 0.0    # degrees

    def apply_aileron(self, aileron_input):
        # aileron_input range: -1 to +1
        self.roll += aileron_input * 5

    def apply_elevator(self, elevator_input):
        # elevator_input range: -1 to +1
        self.pitch += elevator_input * 4

    def apply_rudder(self, rudder_input):
        # rudder_input range: -1 to +1
        self.yaw += rudder_input * 3

    def display_state(self):
        print("\nAircraft Attitude:")
        print(f"Roll  : {self.roll:.2f} degrees")
        print(f"Pitch : {self.pitch:.2f} degrees")
        print(f"Yaw   : {self.yaw:.2f} degrees")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
aircraft = Aircraft()

print("PRIMARY FLIGHT CONTROL SYSTEM")
print("Input range: -1 (left/down) to +1 (right/up)")

aileron = float(input("Enter Aileron input (Roll control): "))
elevator = float(input("Enter Elevator input (Pitch control): "))
rudder = float(input("Enter Rudder input (Yaw control): "))

aircraft.apply_aileron(aileron)
aircraft.apply_elevator(elevator)
aircraft.apply_rudder(rudder)

aircraft.display_state()
