import os
import sys
import time
import keyboard as key

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.difficulty = 1

    def attack(self, target, weapon):
        ...

class Crature:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level

class Map:
    def __init__(self, name, biome, level_range):
        self.name = name
        self.biome = biome
        self.level_range = level_range

class Menu:
    # This class will display a list and make the items easy to scroll over and select
    # making it some form of gui
    def __init__(self, items, title):
        self.title = title
        self.items = items
        self.current_item = 0

    def print_items(self):
        # Hopefully works on MacOS and Linux too, I can only verify on Windows
        os.system("cls" if os.name == "nt" else "clear")
        key.read_event(suppress=True) # This is a magic line!
        print(f"""        {self.title}\n
            
            
            """)
        # This highlights the selected item in a list
        for index, item in enumerate(self.items):
            if index == self.current_item:
                print(f"            [{item.strip()}]")
            else:
                print(item)
        
        print("Navigate using arrow keys up/down")
        print("Press Enter to select or Esc to go back\n")

    def navigate(self):
        
        self.print_items()
        while True:
            if key.is_pressed(72) and debounce(72): # Scancode for "up" to work on international keyboard layouts
                self.current_item = (self.current_item - 1) % len(self.items)
                self.print_items()
            if key.is_pressed(80) and debounce(80): # Scancode for "down" to work on international keyboard layouts
                self.current_item = (self.current_item + 1) % len(self.items)
                self.print_items()
            if key.is_pressed("enter") and debounce("enter"):
                return self.items[self.current_item].strip()
            if key.is_pressed("esc") and debounce("esc"):
                return None
            time.sleep(0.1) # This makes sure there is no fire in the CPU

key_cooldown = {}

def debounce(key, delay=0.3):
    current_time = time.time()
    if key not in key_cooldown or (current_time - key_cooldown[key]) > delay:
        key_cooldown[key] = current_time
        return True
    return False

def get_player_name():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome Adventurer!")
    print("What's name do we go by?")

    # This clears any keyboard module sticky input
    while key.is_pressed("enter"):
        time.sleep(0.1)

    player_name = input("Name: ")
    return player_name

def confirm_exit():
    print("Are you sure you want to exit?")
    while True:
        if key.is_pressed("y") and debounce("y"):
            return True
        elif key.is_pressed("n") and debounce("n"):
            return False
        time.sleep(0.1)

splash_screen = r"""
                        
                        
         A GAME         
                        
                        
                        
                        
                        
                        """

def main_menu(player_name):
    main_menu_items = [
        "            PLAY",
        "            OPTIONS",
        "            ABOUT",
        "            EXIT"
        ]

    main_menu = Menu(main_menu_items, "MAIN MENU")

    while True:        
        choice = main_menu.navigate()
        if choice == "PLAY":
            game_loop(player_name)
        elif choice == "OPTIONS":
            options_menu()
        elif choice == "ABOUT":
            print("The README.md will be opened here")
        elif choice == "EXIT":
            if confirm_exit():
                sys.exit("Successfully terminated the game")
        elif choice == None:
            break
        time.sleep(0.1)

def options_menu():
    options_menu_items = [
        "           DIFFICULTY",
        "           ARACHNOPHOBIA MODE"
        ]

    options_menu = Menu(options_menu_items, "OPTIONS")
    choice = options_menu.navigate()

    while True:
        if choice == "DIFFICULTY":
            handle_option("DIFFICULTY")
        elif choice == "ARACHNOPHOBIA MODE":
            handle_option("ARACHNOPHOBIA MODE")
        elif choice == None:
            break

def handle_option(choice):
    if choice == "DIFFICULTY":
        ...
    if choice == "ARACHNOPHOBIA MODE":
        ...

def show_about():
    print("README.md")
    return None

def game_loop(player_name):
    os.system("cls" if os.name == "nt" else "clear")
    player = Player(player_name)
    print(f"{player.name} is a level {player.level} adventurer!")
    print("Press Esc to open options menu")
        
    while True:
        if key.is_pressed("esc") and debounce("esc"):
            options_menu()

            # Game logic
        time.sleep(0.5)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(splash_screen)
    print("Press 'Enter' to continue")

    waiting_for_enter = True
    while waiting_for_enter:
        if key.is_pressed("enter") and debounce("enter"):
            waiting_for_enter = False
            time.sleep(0.1)
    player_name = get_player_name()
    main_menu(player_name)

if __name__ == "__main__":
    main()
