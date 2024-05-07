from structure.Floor import *
from entities.Player import Player
from abc import ABC, abstractclassmethod


class Map(ABC): #Mapa base
    def __init__(self):
        self.floors = self.floor_list() #acá van los pisos que se recorren, nunca vacío
        self.current_floor_num = 0
        
    @abstractclassmethod #defino los pisos para este mapa (partida)
    def floor_list(self):
        pass

    def locate_player_on_first_floor(self, player: Player): #ubica al jugador en el primer piso (en un lugar específico)
        print(f"Putting player in floor 1")
        player.set_map(self) #le ponemos el mapa para después poder moverlo entre pisos (solamente hay uno por partida)
        desired_floor = self.floors[self.current_floor_num]
        desired_floor.put_player(player)
        
    def move_player__to_next_floor(self, player: Player):
        self.current_floor_num += 1
        print(f"Putting player in floor {self.current_floor_num}")
        desired_floor = self.floors[self.current_floor_num]
        desired_floor.put_player(player)


class DefaultMap(Map): #Mapa predeterminado
    # def __init__(self):
    #     self.floors = self.floor_list()

    def floor_list(self):
        return [DefaultFloor(), Manual_Floor_1()]