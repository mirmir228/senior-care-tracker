import math

class SeniorCareApp:
    def __init__(self, senior_name, home_location):
        self.senior_name = senior_name
        self.home_location = home_location
        self.radius = 500  # Safe zone in meters
        self.app_status = "Active"

    def get_distance(self, current_pos):
        
        R = 6371000
        lat1, lon1 = map(math.radians, self.home_location)
        lat2, lon2 = map(math.radians, current_pos)
        
        dlat, dlon = lat2 - lat1, lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        return R * 2 * math.asin(math.sqrt(a))

    def update_ui(self, current_pos):
        """
        This function simulates updating the mobile screen.
        """
        distance = self.get_distance(current_pos)
        
        if distance > self.radius:
            self.send_push_notification()
            return f"STATUS: OUTSIDE! ({int(distance)}m from home)"
        return f"STATUS: At home. Distance: {int(distance)}m"

    def send_push_notification(self):
        """
        Simulates a mobile push notification to the caregiver's phone.
        """
        print(f"📱 MOBILE NOTIFICATION: {self.senior_name} has left the safe area!")

    def on_sos_click(self):
        """
        Event triggered by the big red button on the senior's phone.
        """
        print("🚨 SOS SIGNAL SENT to emergency contacts and nearby family.")

# --- Simulation for GitHub ---
app = SeniorCareApp("Grandpa", (56.3269, 44.0059))
print(app.update_ui((56.3350, 44.0150))) # Simulation: Moving away
app.on_sos_click() # Simulation: SOS button press
