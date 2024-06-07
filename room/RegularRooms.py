from entities.DamagefulEntities import SpikeBox
from resources.CardinalDirection import East, North, South, West
from room.Cuadricule import Cuadricule
from room.Room import BaseRoom
from room.RoomObjects import Air, Door, Wall
from entities.GeneralEntities import *


class DefaultRoom(BaseRoom):
    def default_cuadricules(self):
        north_door = Cuadricule(Door(North()))
        west_door = Cuadricule(Door(West()))
        south_door = Cuadricule(Door(South()))
        east_door = Cuadricule(Door(East()))

        inside_cuadricules = [ #habitación por dentro
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  north_door     ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                             west_door, Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   east_door         ,
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  south_door       ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   Cuadricule(Wall()),
                   ]

        return inside_cuadricules


    def __repr__(self): #para cambiar cómo se ve en el mapa
        return "■"
    
class Room_1(BaseRoom):
    def default_cuadricules(self):
        north_door = Cuadricule(Door(North()))
        west_door = Cuadricule(Door(West()))
        south_door = Cuadricule(Door(South()))
        east_door = Cuadricule(Door(East()))

        inside_cuadricules = [ #habitación por dentro
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  north_door     ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),Cuadricule(SpikeBox()), Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                             west_door, Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),Cuadricule(SpikeBox()), Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   east_door         ,
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),Cuadricule(SpikeBox()), Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  south_door       ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   Cuadricule(Wall()),
                   ]

        return inside_cuadricules


    def __repr__(self): #para cambiar cómo se ve en el mapa
        return "■"