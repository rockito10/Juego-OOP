class ImpossibleMovement(Exception): #creando exceptions
    def __init__(self):
        print("The move cant be executed because it's an impossible situation.")
        
class InvalidStack(Exception): #creando exceptions
    def __init__(self):
        print("Cant stack the objects in the content of cuadricule (most likely due to the current having no more space)")