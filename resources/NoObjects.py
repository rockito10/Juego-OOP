

class NoRoom(): #para cuando no hay una habitación
    def __init__(self):
        pass
    
    def player_leave(self):
        pass


class NoPlayer(): #para cuando una habitación no tiene un jugador actual
    def __init__(self):
        self.current_floor = None
        self.current_room = None
        self.current_cuadricule_number = 0
        self.position_number = None

    def representation_for_room__(self, cuadricule):
        return cuadricule.__repr__()
    
    def representation_for_floor__(self, room):
        return room.__repr__()