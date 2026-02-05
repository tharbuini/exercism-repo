class SpaceAge:
    def __init__(self, seconds):
        self.age = seconds / (60 * 60 * 24 * 365.25)

    def on_mercury(self):
        return (self.age / 0.2408467).__round__(2)
    
    def on_venus(self):
        return (self.age / 0.61519726).__round__(2)
        
    def on_earth(self):
        return (self.age / 1.0).__round__(2)
        
    def on_mars(self):
        return (self.age / 1.8808158).__round__(2)
        
    def on_jupiter(self):
        return (self.age / 11.862615).__round__(2)
        
    def on_saturn(self):
        return (self.age / 29.447498).__round__(2)
        
    def on_uranus(self):
        return (self.age / 84.016846).__round__(2)
        
    def on_neptune(self):
        return (self.age / 164.79132).__round__(2)
    