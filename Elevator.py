import time
import threading
# Code for a "real" elevator:
# Hor door is open and closed
# How many floors
# How many persons in the elevator
# If it is moving up or down.
# If moving up no stops with down bottom.
# If moving down no stops with up bottom.
# Define current state
UP = 1
DOWN = -1
STOP = 0
CLOSED = 0
OPENED = 1

class Building:
    def __init__(self, number_of_floors, num_basement = 0):
        self.number_of_floors = number_of_floors
        self.num_basement = num_basement
        self.people = []

    def has_person(self,person):
        self.people.append(person)
    
    def dont_has_person(self, person):
        self.people.remove(person)

class Person:
    def __init__(self, desired_floor = 0, current_floor = 0, name = "", weight = 120):
        self.name = name
        self.weight = weight
        self.desired_floor = desired_floor
        self.current_floor = current_floor
    
    def enters(self,building):
        print(self.name, "entered the building.")
        building.has_person(self)

    def leave(self, building):
        print(self.name, "left the building.")
        building.dont_has_person(self)

    def waits_to_get_into(self, elevator):
        # input()
        while not (elevator.door_status == OPENED and elevator.current_floor == self.current_floor): # We should use threads for more than one passenger...
            print(self.name, "is waiting elevator. Current elevator floor:", elevator.current_floor)
            elevator.turn_on()
            # input()
        else:
            print("Elevator is here...")

    def waits_to_get_off_of(self,elevator):
        while not (elevator.door_status == OPENED and elevator1.current_floor == self.desired_floor):
            print("Waiting to get off of the elevator")
            elevator.turn_on()
            # input()
        else:
            print("Elevator arrived at the desired floor,",self.name)
    
    def press_elevator_button_up_of(self, elevator):
        print(self.name, "pressed the up button of the elevator")
        elevator.called_at_floor(self.current_floor,UP)
    
    def press_elevator_button_down_of(self, elevator):
        print(self.name, "pressed the down button of the elevator")
        elevator.called_at_floor(self.current_floor,DOWN)
    
    def press_floor(self, desired_floor, elevator):
        print(self.name, "pressed the button (Floor:", desired_floor, ") inside the elevator")
        elevator.desired_floor(desired_floor)

    def get_into_elevator(self, elevator):
        print(self.name, "got inside the elevator")
        elevator.add_person(self)

    def get_off_elevator(self, elevator):
        print(self.name, "left the elevator")
        elevator.drop_person(self)
        self.current_floor = elevator.current_floor
    
    def holds_door_opened(self, elevator):
        print(self.name, "is holding the door opened")
        elevator.blocked_door()
    
    def releases_door(self, elevator):
        print(self.name, "is releasing the door")
        elevator.free_door()

class Elevator:
    def __init__(self, building, max_number_of_passangers = 6, max_kg = 720):
        self.max_floor = building.number_of_floors
        self.num_basement = building.num_basement
        self.number_of_passangers = 0
        self.max_number_of_passangers = max_number_of_passangers
        self.max_kg = max_kg
        self.door_status = 0 # 0 is closed, 1 is opened.
        self.current_floor = 0
        self.passangers = []
        self.direction = 0 # 0 = stopped; 1 = going up; -1 going down
        self.calls = []
        self.blocked_door = 0 # No obstacle at the sensor door.
        self.running = 1

    # Just make the calls nice, without repetition, and sorted by floor.
    def fix_calls(self):
        self.calls = [list(item) for item in set(tuple(row) for row in self.calls)] # Eliminate duplicate button calls
        return self.calls.sort(key=lambda x: x[0]) # Sort by floor

    # Just return the true if there are calls at floor to goes up.
    def up_calls(self, floor):
        self.fix_calls()
        return any(self.calls[e][1] == UP and self.calls[e][0] == floor for e in range(len(self.calls)))

    # Just return true if there are calls at floor that goes down
    def down_calls(self,floor):
        self.fix_calls()
        return any(self.calls[e][1] == DOWN and self.calls[e][0] == floor for e in range(len(self.calls)))
    
    # Just return true if there are calls to stop (calls from inside the elevator) at floor
    def stop_calls(self, floor):
        self.fix_calls()
        return any(self.calls[e][1] == STOP and self.calls[e][0] == floor for e in range(len(self.calls)))

    def is_running(self):
        return self.running
    
    def shutdown(self):
        self.running = 0


    def turn_on(self): 
        # I BET USD 1.000.000,00 that this can be **REALLY** improved!!!!!
        # What a mess!!
        
        self.fix_calls() # just to be sure...    
        for elem in range(len(self.calls)):
            self.fix_calls() # just to be sure...
            # print(self.calls)
            if len(self.calls) > 0:
                # print(self.calls[elem])
                if self.direction == STOP or self.direction == self.calls[elem][1] or len(self.calls) == 1:
                    if (self.calls[elem][0] == self.current_floor):
                        print("Reached the floor...")
                        if self.door_status == CLOSED:
                            print("But door is closed...")
                            self.direction = STOP
                            self.open_door()
                            del self.calls[elem] # ???
                            # print("Debug Calls2", self.calls)
                            break
                                #True # Now person needs to take another action (press floor button or someone calls the elevator)
                        if self.door_status == OPENED: # and self.calls[elem][1] == STOP: # Pressed button to go to a floor
                            self.close_door()
                            del self.calls[elem] # ???
                            # print("Debug Calls", self.calls)
                            # elem = 0
                            # Define the where it must go:
                            if (self.current_floor < self.calls[elem][0]):
                                self.direction = UP
                                self.move_up()
                                    #self.action()
                            if (self.current_floor > self.calls[elem][0]):
                                self.direction = DOWN
                                self.move_down()
                                    #self.action()
                            # elem = 0     
                            break
                    else: # Not at the right floor
                        print("Not at floor..")
                        if self.door_status == OPENED: #and self.calls[elem][1] == STOP: # Pressed button to go to a floor
                            self.close_door()
                            # print("Debug Calls3", self.calls)
                            # elem = 0
                            
                                #self.action() # Lets move on...
                            if (self.current_floor < self.calls[elem][0]):
                                print("Up.. ")
                                self.direction = UP
                                self.move_up()
                                return self.turn_on()
                            if (self.current_floor > self.calls[elem][0]):
                                print("Down..")
                                self.direction = DOWN
                                self.move_down()
                                return self.turn_on()
                            # elem = 0     
                            break

            if self.direction == UP:
                if self.up_calls(self.current_floor) or self.stop_calls(self.current_floor):
                    self.direction = STOP
                    # print("Going up, and reached the floor")
                    continue# self.action()
                self.move_up()
            if self.direction == DOWN:
                if self.down_calls(self.current_floor) or self.stop_calls(self.current_floor):
                    self.direction = STOP
                    # print("Going down, and reached the floor")
                    continue# self.action()
                self.move_down()
        

    # When someone calls the elevator at one floor, to go up or down.
    def called_at_floor(self, floor, up_or_down):
        self.calls.append([floor, up_or_down])
        self.fix_calls()
        if not self.blocked_door:
            self.turn_on()
            
        else:
            print("Sensor door is blocked!")
            return False

    # When someone press the floor button linside the elevator.
    def desired_floor(self, floor):
        self.calls.append([floor, STOP])
        self.fix_calls()
        if not self.blocked_door:
            self.turn_on()
            
            
        else:
            print("Sensor door is blocked!")
            return False

    def close_door(self):
        print("Door is closing...")
        self.door_status = 0

    def open_door(self):
        print("Door is openning...")
        self.door_status = 1
    
    def move_up(self):
        if self.current_floor < self.max_floor:
            self.current_floor += 1
            print("Current floor:", self.current_floor)
            return
        else:
            print("Elevator cannot fly through the roof...")

    def move_down(self):
        if self.current_floor > self.num_basement:
            self.current_floor -= 1
            print("Current floor:", self.current_floor)
        else:
            print("Elevator cannot move down... are you going to hell?")



    
    def sensor_door(self):
        return self.blocked_door
    
    def block_door(self):
        self.blocked_door = 1
    
    def free_door(self):
        self.blocked_door = 0

    def get_direction(self):
        return self.direction
    
    def add_person(self, person):
        self.passangers.append(person)
        # check if elevator is ok?!
        return self.passangers
    
    def drop_person(self,person):
        self.passangers.remove(person)

    def get_weight(self):
        current_weight = 0
        for person in self.passangers:
            current_weight += person.weight
        return current_weight
    

  
    @property
    def current_floor(self):
        # print("Current floor: ", self._current_floor)
        return self._current_floor

    @current_floor.setter
    def current_floor(self, floor):
        self._current_floor = floor


    @property
    def door_status(self):
        # print("Current door: ", ["Closed", "Opened"][self._door_status], " and it is ", ["free", "blocked"][self.blocked_door])
        return self._door_status

    @door_status.setter
    def door_status(self, door):
        self._door_status = int(door) 
       
        
def thead_me(person, elevator):
    person.press_elevator_button_up_of(elevator)
    person.waits_to_get_into(elevator)
    person.get_into_elevator(elevator) 
    person.press_floor(person.desired_floor, elevator)
    person.waits_to_get_off_of(elevator)
    person.get_off_elevator(elevator)

def use_elevator(person, elevator):
    f1 = threading.Thread(name=person.name, target=thead_me(person,elevator))
    f1.start


building1 = Building(number_of_floors=10, num_basement=0)
elevator1 = Elevator(building=building1,max_number_of_passangers=6,max_kg=720)


felipe = Person(desired_floor = 2, current_floor= 0, name="Felipe", weight=120)
aqeel = Person(desired_floor = 2, current_floor= 1, name="Aqeel", weight=120)
john = Person(desired_floor = 2, current_floor= 1, name="John", weight=120)

aqeel.enters(building1) # 1st floor
felipe.enters(building1)
john.enters(building1)
use_elevator(felipe, elevator1)
use_elevator(aqeel, elevator1)
use_elevator(john, elevator1)






