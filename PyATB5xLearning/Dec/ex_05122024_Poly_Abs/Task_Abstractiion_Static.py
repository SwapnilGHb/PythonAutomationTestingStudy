# Create a Program
# Class - PC
# Class - MotherBoard
# abstract method - start mother board
# Class - RAM
# abstractMethod → start RAM
# Class - Processor
# abstractMethod → start processor
# Class - Storage
# abstractMethod → storage data,
# static method -># loadOS
# non static -> # startMouse,# UseHeadPhone

from abc import ABC, abstractmethod

class PC:
    def parent(self):
        print("I am Personal Computer Parent class")

class Motherboard:
    def start_mother_board(self):
        print("Starting Motherboard")

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):
    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def load_os():
        print("Loading OS")

    def start_mouse(self):
        print("Starting Mouse")

    def use_head_phone(self):
        print("Using HeadPhone")



obj_pc = PC()
obj_pc.parent()
obj_mb = Motherboard()
obj_mb.start_mother_board()
Storage.load_os()

class Motherboard1(RAM):
    def start_ram(self):
        print("Starting RAM")

class Processor1(Processor):
    def start_processor(self):
        print("Starting Processor")

class Storage1(Storage):
    def storage_data(self):
        print("Starting Storage Data")

obj_mb1 = Motherboard1()
obj_pro1 = Processor1()
obj_str1 = Storage1()
obj_mb1.start_ram()
obj_pro1.start_processor()
obj_str1.storage_data()
