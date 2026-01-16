"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    # Attributes
    total_aliens_created = 0
    print(total_aliens_created)
    
    # Constructor
    def __init__(self, x_new_coordinate, y_new_coordinate):
        self.health = 3
        self.x_coordinate = x_new_coordinate
        self.y_coordinate = y_new_coordinate
        Alien.total_aliens_created +=  1

    # Methods
    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        if (self.health > 0):
            return True
        return False

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, alien):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    aliens = []
    for position in alien_start_positions:
        alien = Alien(position[0], position[1])
        aliens.append(alien)

    return aliens        