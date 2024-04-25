#Name: Joshua Kamerer
#Date: 4/24/2024
#Class: CPSC 1050
#Github Link: https://github.com/Jkamere/Project-02---RPG
#Description: Riddle solving game

import logging

#class for when exit not found error
class ExitNotFoundError(Exception):
    def __init__(self, room_name, message="Room not found"):
        self.room_name = room_name
        self.message = message

    #returns the room name and a message
    def __str__(self):
        return f"{self.room_name} -> {self.message}"

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items if items else []

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def list_exits(self):
        return "\n".join(self.exits)

    def list_items(self):
        if self.items:
            item_list = "Items in the room:\n"
            for item in self.items:
                item_list += f"{item.name}: {item.description}\n"
            return item_list
        else:
            return "There are no items in the room."

    def __str__(self):
        return f"{self.name}: {self.description}\n"


class AdventureMap:
    def __init__(self):
        self.map = {}

    def add_room(self, room):
        self.map[room.get_name().lower()] = room

    def get_room(self, room_name):
        room_name_lower = room_name.lower()
        if room_name_lower not in self.map:
            raise ExitNotFoundError(room_name)
        return self.map[room_name_lower]

def setup_logger():
    logger = logging.getLogger('adventure_game_logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('adventure_game.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def main():
    logger = setup_logger()
    
    adventure_map = AdventureMap()

    adventure_map.add_room(Room("Hallway", "A long, unsettling hallway that has 3 rooms, room 901, room 902, room 903, and a dimly lit elevator at the end.", ['Room 901', 'Room 902', 'Room 903', 'Elevator']))
    adventure_map.add_room(Room("Room 901", "You open the door and enter the room and instantly you see a man in, what you think is, a medieval jester costume telling you incomprehensible riddles and countless other items laying around.", ["Hallway", 'Elevator'], [Item("An annoying riddler", "you just wish he would shut up"), Item("A toy spider", "At least you hope its a toy"), Item("A book", "It is titled 'Sweet Dreams'"), Item("Statue of the Letter E", "Statue of a letter E for some reason")]))
    adventure_map.add_room(Room("Room 902", "As you open the door, you see a destroyed hotel room, as if a tornado went through it. But through the rubble, you see a few items that aren't destroyed and ones that stick out.", ["Hallway", 'Elevator'], [Item("A book", "It is called 'Temper Management'"), Item("A plastic tongue", "Please be plastic..."), Item("A sword", "It is sharpened and has a nice shine to it"), Item("A portrait", "Of everything destroyed, a painting of Jesus remains on the wall")]))
    adventure_map.add_room(Room("Room 903", "As you enter the room, you see that it looks nothing like a hotel room. There is sand every, some small trees and potted bushes, and a light up moon hanging from the ceiling.", ["Hallway", 'Elevator'], [Item("A sandbox", "It has a castle and a little town in it"), Item("The moon", "A small lamp moon thats hanging from the ceiling"), Item("A map", "There is a map of some unknown place on the wall"), Item("An Idea", "There is a box that is labelled, think tank")]))
    adventure_map.add_room(Room("Elevator", "When you get to the elevator and press the only button on it, down, nothing happens, it doesn't open, doesn't call an elevator, and you can't even pry it open with your hands.", ["Hallway", 'Room 901', 'Room 902', 'Room 903']))

    current_room = adventure_map.get_room("Hallway")
    entered_room_901 = False
    entered_room_902 = False
    entered_room_903 = False
    inventory = []

    print("As you wake up, you see a ceiling you don't recognize. And upon sitting up, you realize you are in a long hallway with no exit behind you, only an elevator at the end of the hallway and 3 rooms around. Rooms 901 and 903 on the left, and Room 902 on the left. You also find a note on the ground.\n")
    print("The note reads: 'Hello player, welcome to my lovely hotel! If you wish to leave, you need to solve 3 riddles, 1 for each room. When you enter, pick up the note and read it, then grab the item you think the answer is.'\n")
    print("After reading, you could ignore the note and head straight towards the elevator, or you can start investigating the rooms like it said.\n")

    while True:
        choice = input("Where do you head?\n").strip().lower()
        
        exits = current_room.get_exits()
        if choice in [exit.lower() for exit in exits]:
            current_room = adventure_map.get_room(choice)
            print(current_room)
            if current_room.name.lower() == "room 901" and not entered_room_901:
                print("A riddle appears in front of you:")
                print("'Often will I spin a tale, never will I charge a fee. I'll amuse you an entire eve, but alas, you won't remember me.'")
                entered_room_901 = True
                print("Items available in the room:")
                print(current_room.list_items())
            elif current_room.name.lower() == "room 901" and entered_room_901:
                print(current_room.list_items())
                choice = input("Do you want another item? Yes or No?\n").strip().lower()
                if choice == "no":
                    continue
            elif current_room.name.lower() == "room 902" and not entered_room_902:
                print("A riddle appears in front of you")
                print("'I'm rarely touched but often held. If you have wit, you'll use me well.'")
                entered_room_902 = True
                print("Items available in the room:")
                print(current_room.list_items())
            elif current_room.name.lower() == "room 902" and entered_room_902:
                print(current_room.list_items())
                choice = input("Do you want another item? Yes or No?\n").strip().lower()
                if choice == "no":
                    continue
            elif current_room.name.lower() == "room 903" and not entered_room_903:
                print("A riddle appears in front of you")
                print("'I have seas with no water, coasts with no sand, towns without people, mountains without land. What am I?'")
                entered_room_903 = True
                print("Items available in the room:")
                print(current_room.list_items())
            elif current_room.name.lower() == "room 903" and entered_room_903:
                print(current_room.list_items())
                choice = input("Do you want another item? Yes or No?\n").strip().lower()
                if choice == "no":
                    continue
            elif current_room.name.lower() != "room 901" and current_room.name.lower() != "room 902" and current_room.name.lower() != "room 903":
                continue




            item_choice = input("Which item do you pick up?\n").strip().lower()
            if current_room.name.lower() == "room 901" and entered_room_901 and entered_room_902 and entered_room_903:
                correct_item_names4 = ["statue of the letter e"]
                if item_choice in correct_item_names4:
                    print('As soon as you grab it, you hear a DING! You look out the door, the elevator opened! You sprint for it and just make it inside, you made it out!')
                    break
                else:
                    print("The door slams shut, and you run to it! You aren't able to open it! You realize you are trapped there forever.... GAME OVER!")
                    break
            elif current_room.name.lower() == "room 901" and entered_room_901:
                correct_item_names = ["a book"]
                if item_choice in correct_item_names:
                    print("After grabbing the item, a new note appears that reads, 'Congrats, you have beat the riddle. Now onto the next!'")
                    inventory.append(item_choice)
                    current_room.items = [item for item in current_room.items if item.name.lower() != item_choice]
                else:
                    print("The door slams shut, and you run to it! You aren't able to open it! You realize you are trapped there forever.... GAME OVER!")
                    break
                    inventory.append(item_choice)
            elif current_room.name.lower() == "room 902" and entered_room_902:
                correct_item_names2 = ["a plastic tongue"]
                if item_choice in correct_item_names2:
                    print("After grabbing the item, a new note appears that reads, 'Congrats, you have beat the riddle Now onto the next!'")
                    inventory.append(item_choice)
                    current_room.items = [item for item in current_room.items if item.name.lower() != item_choice]
                else:
                    print("The door slams shut, and you run to it! You aren't able to open it! You realize you are trapped there forever.... GAME OVER!")
                    break
            elif current_room.name.lower() == "room 903" and entered_room_903:
                correct_item_names3 = ["a map"]
                if item_choice in correct_item_names3:
                    print("After grabbing the item, a new note appears that reads, 'Congrats, you have beat the riddle. Now onto the next!'")
                    inventory.append(item_choice)
                    current_room.items = [item for item in current_room.items if item.name.lower() != item_choice]
                else:
                    print("The door slams shut, and you run to it! You aren't able to open it! You realize you are trapped there forever.... GAME OVER!")
                    break
            else:
                print("The door slams shut, and you run to it! You aren't able to open it! You realize you are trapped there forever.... GAME OVER!")
                break
        else:
            print(f"{choice} -> That isn't connected to this area")
        
        print("Your Inventory:")
        for item in inventory:
            print("- " + item)
        
        if entered_room_901 and entered_room_902 and entered_room_903:
            print("After reading the note, a voice starts talking in your head! 'You seem to have made it past all 3 rooms... you should head back to the elevator'")
            adventure_map.get_room("elevator").description = "The voice in your head speaks again,\n'Grab the note from in between the doors, I have 1 final riddle for you, then you will be free, and no choices this time though... What is the beginning of eternity, the end of time and space, the beginning of every end and the end of every place.'"
            continue

            
if __name__ == "__main__":
    main()