import math

# Basic location-based logic for the elderly tracking app
class SeniorCareApp:
    def __init__(self, senior_name, home_coords):
        self.senior_name = senior_name
        self.home = home_coords
        self.limit = 500  # radius in meters
        self.is_active = True

    def calculate_range(self, current_pos):
        # Using Haversine here to get more or less accurate distance
        # Standard math for GPS-based apps
        lat1, lon1 = map(math.radians, self.home)
        lat2, lon2 = map(math.radians, current_pos)
        
        d_lat = lat2 - lat1
        d_lon = lon2 - lon1
        
        a = math.sin(d_lat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(d_lon/2)**2
        # R of Earth = 6371km
        return 6371000 * 2 * math.asin(math.sqrt(a))

    def track_status(self, current_pos):
        try:
            dist = self.calculate_range(current_pos)
            
            if dist > self.limit:
                self.trigger_notification()
                return f"OUTSIDE: {int(dist)}m away. Check in!"
            
            return f"Safe. Current distance: {int(dist)}m"
        except Exception as e:
            return f"Error processing location: {e}"

    def trigger_notification(self):
        # TODO: Integrate with actual Firebase or OneSignal later
        print(f"PUSH SENT: {self.senior_name} left the safe zone!")

    def emergency_sos(self):
        # For the big red button in the UI
        print(f"🚨 SOS! Emergency signal for {self.senior_name} broadcasted to family.")

# --- Testing the logic ---
if __name__ == "__main__":
    app = SeniorCareApp("Alexey", (56.3269, 44.0059))
    
    # Check if he's close to home
    print(app.track_status((56.3275, 44.0065)))
    
    # Simulate him going to the shop too far away
    print(app.track_status((56.3450, 44.0250)))
    
    # Emergency test
    app.emergency_sos()
