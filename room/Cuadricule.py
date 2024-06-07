from abc import abstractmethod
from room.RoomObjects import Door, Air, Wall
# from resources.Exceptions import InvalidStack

class Cuadricule():
    def __init__(self, initialContent, room): #le doy el contenido inicial
        initialContent.set_cuadricule(self) #se pasa a sí mismo
        self.content = [initialContent] 
        self.room = room
        
    def do_turn(self):
        for content in self.content: #no debería haber mucho para recorrer
            content.turn()
        
    def first_object(self): #devuelve el primer objeto de la cuadrícula, el que la define
        return self.content[0]
    
    def add_to_content(self, content):
        self.content = self.content + [content]
        
    def restart_content_to_first(self): #dejar una lista con el primer objeto
        # if (player in self.content):
        #     self.content.remove(player)
        
        self.content = [self.first_object()]

    def map_representation(self):
        return self.content[-1].representation_for_room__(self) #siempre agarra la representación en base al último del contenido (-1 es el último)

    # def set_default_content(self):
    #     pass
    
    def move_to_self_num_in_room_(self, room, num: int):
    #para continuar si el jugador se mueve o no dentro de las cuadrículas
        # print(num)
        self.first_object().locate_player_in_room_in_cuadricule_num(room, num)
        
    def destroy_content(self): #cambio lo que esté por Air
        self.content = [Air()]
        
        
        
        
        

# class EmptyCuadricule(Cuadricule):
    
#     # def __init__(self):
#     #     self.set_default_content() 
        
#     def set_default_content(self): #no tiene nada (aire)
#         self.content = [Air()]
        
#     # def restart_content_to_first(self, player): #quitar el último elemento de la lista
#     #     # if (player in self.content):
#     #     #     self.content.remove(player)
        
#     #     self.content = [self.content[0]]
    
#     # def add_to_content(self, content): #setter para cambiar el contenido de una cuadrícula
#     #     self.content = content 
    
#     # def map_representation(self): 
#     #     return self.content.representation_for_room__()
    
#     def move_to_self_num_in_room_(self, num: int, room):
#         room.locate_player_in_cuadricule_num(num)
          
    
# class DoorCuadricule(Cuadricule): #la cuadrícula que posee la puerta
#     # def __init__(self):
#     #     set_default_content() 
    
#     # def restart_content_to_first(self, player): #quitar el último elemento de la lista
#     #     # if (player in self.content):
#     #     #     self.content.remove(player)
        
#     #     self.content = [self.content[0]]
        
#     def set_default_content(self): #de predeterminado tiene la puerta (puede tener un jugador o un enemigo) (por lo menos gráficamente hablando)
#         self.content = [Door()]
    
#     # def add_to_content(self, content): #setter para cambiar el contenido de una cuadrícula
#     #     self.content = content 
        
#     def move_to_self_num_in_room_(self, num: int, room):
#         room.locate_player_in_cuadricule_num(num)
    
#     # def map_representation(self):
#         # return self.content.representation_for_room__()
    
# class WallCuadricule(Cuadricule):
    
#     def set_default_content(self): #de predeterminado tiene una pared (y no debería cambiar)
#         self.content = [Wall()]
        
#     # def restart_content_to_first(self, player): #quitar el último elemento de la lista
#     #     # if (player in self.content):
#     #     #     self.content.remove(player)
        
#     #     # self.content = [self.content[0]]
#     #     pass
    
#     def add_to_content(self, content): 
#         raise InvalidStack
    
#     def move_to_self_num_in_room_(self, num: int, room):
#         print("Cant enter a wall!")
    
#     # def map_representation(self):
#         # return self.content.representation_for_room__()
        
    