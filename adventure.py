import random
import os
import json

ROOM_TREASURE = "Treasury"
ROOM_HALLWAY_A = "Hallway-A"
ROOM_HALLWAY_B = "Hallway-B"
ROOM_CHAMBER = "King's Chamber"
ROOM_STORAGE = "Weapons Storage"
ROOM_DEN = "Lion's Den"
ROOM_DUNGEON = "Dungeon"

player = {"Location": ROOM_TREASURE, "Inventory": [], "Love_Rescued": False, "Blackmailed": False, "Threatened": False}
guard = {"Active": True, "Location": ROOM_HALLWAY_A}
Treasury_Shelf = ["Bottle"]
Table = ["Documents"]
Guard_Rooms = [ROOM_STORAGE, ROOM_HALLWAY_A, ROOM_HALLWAY_B, ROOM_DUNGEON]
Lion_Health = 100
Lion_Alive = True
Won = False 
T_Door_Open = False
Gate_Open = False

#Room Descriptions
ROOM_TREASURE_DESC = "You're in the treasury room. There is a table in the middle of the room, a shelf by a wall, and a window by another wall. Go west to leave this room to hallway A"
ROOM_HALLWAY_A_DESC = "You're in hallway A. Go north to see the weapons storage, go east to see the treasury, and go south to go to the Lion’s den. To get to hallway B, move left"
ROOM_HALLWAY_B_DESC = "You're in hallway B. Go north to get to the dungeon, go west to get to the king’s chamber. To get to hallway A, move right"
ROOM_CHAMBER_DESC = "You're in the King’s chamber and the tyrant king is also present. East of the king's chamber is hallway B"
ROOM_DESC_INI = ". What is your move?"
ROOM_STORAGE_DESC = " You're in the weapons storage. In this room, there is a shelf by the wall. Go south to get to hallway A"
ROOM_DEN_DESC = "You're in the lion’s den. North of the den is hallway A"
ROOM_DEN_W_LION = ROOM_DEN_DESC + ", there is a lion chained to the wall"
ROOM_DEN_W_BOTH = ROOM_DEN_W_LION + ", and on the wall is a key"
ROOM_DEN_W_KEY = ROOM_DEN_DESC + ", there is a key on the wall"
ROOM_DUNGEON_DESC = "You walk into the dungeon"
ROOM_DUNGEON_W_LOVE = ", where your true love is being held"
ROOM_DUNGEON_REM = ", south of the dungeon is hallway B"
GUARD_PRESENT = ", however beware the guard, he may be lurking in the room"

#General Action Descriptions
SAVE_DESC = "Your progress is being saved"
LOAD_DESC = "Your last game is being loaded"
INDUCE_DESC = "You choke the guard with chloroform in the handkerchief, rendering him inactive"
INDUCE_FAIL_DESC = "You made an attempt to choke the guard when you do not possess chloroform. The guard manages to break free and hits you. You are jailed and have lost the game"
STAB_GUARD_DESC = "You make a successful attempt to stab the guard with your sword through his armor, rendering him inactive"
STAB_FAIL_DESC = "You made a stab attempt towards the guard with a wooden knife you had on you. It fails to pierce through his armor. You are arrested and have lost the game"
CLOSE_DESC = "Closing game"
WIN_DESC = "You have won the game by "
B_MAIL_DESC = WIN_DESC + "blackmailing the King to release your true love"
CAUGHT = "You tried to go into the King's chamber while the guard is still active. You have been caught and jailed. You lose the game"
SORRY = "Sorry, that is an invalid input at this point"

#Treasury Action Descriptions
OPEN_DOOR_DESC = "The door opens"
CLOSE_DOOR_DESC = "The door closes"
DOOR_CLOSED = "The door is closed"
T_SHELF_DESC = "There is a shelf by the wall"
SHELF_W_CLRF = T_SHELF_DESC + ", on which there is a bottle of chloroform and an handkerchief"
TABLE_DESC = "There is a table in the middle of the room"
TABLE_DESC_W_DOC = TABLE_DESC + ", on which there are some documents"
PICK_DOC_DESC = "You pick the documents on the table, they are documents that can expose the King's fraud"
PICK_BOTTLE_DESC = "You pick the bottle of chloroform and the handkerchief from the shelf, they can help render a person inactive"
ESCAPE_W_DESC = WIN_DESC + "successfully escaping with your true love through the window"
ESCAPE_L_DESC = "You have tried to escape without your true love, you have lost the game"

#Weapons Storage Action Descriptions
W_SHELF_DESC = "There is a shelf by the wall"
W_SHELF_W_BOTH = W_SHELF_DESC + ", on which there is a sword and a sling shot"
W_SHELF_W_SWORD = W_SHELF_DESC + ", on which there is a sword"
W_SHELF_W_SLING = W_SHELF_DESC + ", on which there is a sling shot"
PICK_SWORD = "You pick the sword, a mighty weapon"
PICK_SLING = "You pick the sling shot, a tricky weapon"

#Dungeon Action Descriptions
OPEN_GATE_DESC = "You unlock the gate of the dungeon with the keys"
NO_GATE_KEY_DESC = "You do not have the keys to unlock the gate"
GATE_LOCK_DESC = "The gate has not been unlocked yet"
RESCUE_LOVE_DESC = "You open the gate and prep to leave the dungeon with your love"

#Den Action Descriptions
STAB_LION_DESC = "You make a successful attempt to stab the lion with your sword"
LION_DEAD_DESC = ", the lion is now dead"
SHOOT_DESC = "You shoot the lion with your sling shot"
LOOK_KEY_DESC = "There is a key on the wall behind the lion, the key opens the gate in the dungeon"
PICK_KEY_DESC = "You pick the key, you can now open the gate of the dungeon"
KILLED_BY_LION = "You make an attempt to pick the key while the lion is still alive. It pounces on you and rips you apart. You lose the game"

#Chamber Action Descriptions
SHOW_DOC_DESC = "You bring out the documents from your inventory and show them to the King, the now troubled King makes the decision to let you leave the palace with your true love for your silence"
NO_DOC_DESC = "You do not have the documents in your inventory"
THREATEN_DESC = "You pull out your sword and point it at the King's neck. He agrees to let you leave with your true love, but you have to escape through how you got into the palace"
THREATEN_FAIL = "You do not have a sword in your inventory"
EMPTY_APPROACH = "You do not have anything in your inventory to convince the King to release your true love. Because you have made an attempt to go into the king's chamber empty-handed, you have lost the game"

#functions
def player_stats():
    base = "Your current"
    loc = " location is " + player["Location"] + ","
    invt = " and you currently have " + ", ".join(player["Inventory"]) + " in your inventory"
    invt_empty = " and your inventory is currently empty"
    if len(player["Inventory"]) == 0:
        res = base + loc + invt_empty
    else:
        res = base + loc + invt
    print(res)

def induce_guard():
    global Won
    if guard["Active"]:
        if guard["Location"] == player["Location"]:
            if "Bottle" in player["Inventory"]:
                print(INDUCE_DESC)
                guard["Active"] = False
            else:
                print(INDUCE_FAIL_DESC)
                Won = True
        else:
            print(SORRY + ", the guard is not in this room")
    else:
        print(SORRY + ", the guard is inactive")

def stab_guard():
    global Won
    if guard["Active"]:
        if guard["Location"] == player["Location"]:
            if "Sword" in player["Inventory"]:
                print(STAB_GUARD_DESC)
                guard["Active"] = False
            else:
                print(STAB_FAIL_DESC)
                Won = True
        else:
            print(SORRY + ", the guard is not in this room")
    else:
        print(SORRY + ", the guard is inactive")

def save_progress():
    print(SAVE_DESC)
    with open("game_progress.txt", "w", encoding="utf8") as progress_fh:
        progress_fh.write(json.dumps(player) + "\n")
        progress_fh.write(json.dumps(guard) + "\n")
        progress_fh.write(json.dumps(Treasury_Shelf) + "\n")
        progress_fh.write(json.dumps(Table) + "\n")
        progress_fh.write(json.dumps(guard["Location"]) + "\n")
        progress_fh.write(json.dumps(Lion_Health) + "\n")
        progress_fh.write(json.dumps(Lion_Alive) + "\n")
        progress_fh.write(json.dumps(Won) + "\n")
        progress_fh.write(json.dumps(T_Door_Open) + "\n")
        progress_fh.write(json.dumps(Gate_Open))
        
def load_game():
    if os.path.isfile("game_progress.txt"):
        print(LOAD_DESC)
        with open("game_progress.txt", "r", encoding="utf8") as progress_fh:
            global player, guard, Treasury_Shelf, Table, Lion_Health, Lion_Alive, Won, T_Door_Open, Gate_Open
            prog = progress_fh.read().split("\n")
            player = json.loads(prog[0])
            guard = json.loads(prog[1])
            Treasury_Shelf = json.loads(prog[2])
            Table = json.loads(prog[3])
            guard["Location"] = json.loads(prog[4])
            Lion_Health = json.loads(prog[5])
            Lion_Alive = json.loads(prog[6])
            Won = json.loads(prog[7])
            T_Door_Open = json.loads(prog[8])
            Gate_Open = json.loads(prog[9])
        print("Loading complete. Check your stats to verify")
    else:
        print("There is no saved game in memory")

print(ROOM_TREASURE_DESC)
while not Won:
    command = input("> ")
    guard["Location"] = random.choice(Guard_Rooms)
    if command.lower() == "close":
        print(CLOSE_DESC)
        break
    if player["Location"] == ROOM_TREASURE:
        if command.lower() == "open door":
            if T_Door_Open:
                print(SORRY)
            else:
                print(OPEN_DOOR_DESC)
                T_Door_Open = True
        elif command.lower() == "close door":
            if T_Door_Open:
                print(CLOSE_DOOR_DESC)
                T_Door_Open = False
            else:
                print(SORRY)
        elif command.lower() == "look at shelf":
            if "Bottle" in Treasury_Shelf:
                print(SHELF_W_CLRF)
            else:
                print(T_SHELF_DESC)
        elif command.lower() == "look at table":
            if "Documents" in Table:
                print(TABLE_DESC_W_DOC)
            else:
                print(TABLE_DESC)
        elif command.lower() == "pick bottle":
            if "Bottle" not in player["Inventory"]:
                print(PICK_BOTTLE_DESC)
                player["Inventory"].append("Bottle")
                Treasury_Shelf.remove("Bottle")
            else:
                print(SORRY)
        elif command.lower() == "pick documents":
            if "Documents" not in player["Inventory"]:
                print(PICK_DOC_DESC)
                player["Inventory"].append("Documents")
                Table.remove("Documents")
            else:
                print(SORRY)
        elif command.lower() == "escape":
            if player["Love_Rescued"]:
                print(ESCAPE_W_DESC)
                Won = True
            else:
                print(ESCAPE_L_DESC)
                break
        elif command.lower() == "go west":
            if T_Door_Open:
                if guard["Active"]:
                    print(ROOM_HALLWAY_A_DESC + GUARD_PRESENT)
                else:
                    print(ROOM_HALLWAY_A_DESC)
                player["Location"] = ROOM_HALLWAY_A
            else:
                print(DOOR_CLOSED)
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
    elif player["Location"] == ROOM_HALLWAY_A:
        if command.lower() == "go east":
            print(ROOM_TREASURE_DESC)
            player["Location"] = ROOM_TREASURE
        elif command.lower() == "go north":
            if guard["Active"]:
                print(ROOM_STORAGE_DESC + GUARD_PRESENT)
            else:
                print(ROOM_STORAGE_DESC)
            player["Location"] = ROOM_STORAGE
        elif command.lower() == "go south":
            if Lion_Alive:
                print(ROOM_DEN_W_BOTH)       
            else:
                if "Key" not in player["Inventory"]:
                    print(ROOM_DEN_W_KEY)
                else:
                    print(ROOM_DEN_DESC)
            player["Location"] = ROOM_DEN
        elif command.lower() == "move left":
            if guard["Active"]:
                print(ROOM_HALLWAY_B_DESC + GUARD_PRESENT)
            else:
                print(ROOM_HALLWAY_B_DESC)
            player["Location"] = ROOM_HALLWAY_B
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "induce":
            induce_guard()
        elif command.lower() == "stab guard":
            stab_guard()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
    elif player["Location"] == ROOM_HALLWAY_B:
        if command.lower() == "go north":
            if not player["Love_Rescued"]:
                if guard["Active"]:
                    print(ROOM_DUNGEON_DESC + ROOM_DUNGEON_W_LOVE + ROOM_DUNGEON_REM + GUARD_PRESENT)
                else:
                    print(ROOM_DUNGEON_DESC + ROOM_DUNGEON_W_LOVE + ROOM_DUNGEON_REM)
            else:
                print(ROOM_DUNGEON_DESC + ROOM_DUNGEON_REM + GUARD_PRESENT)
            player["Location"] = ROOM_DUNGEON
        elif command.lower() == "go west":
            if guard["Active"]:
                print(CAUGHT)
                break
            else:
                if "Sword" in player["Inventory"] or "Documents" in player["Inventory"]:
                    print(ROOM_CHAMBER_DESC)
                    player["Location"] = ROOM_CHAMBER
                else:
                    print(EMPTY_APPROACH)
                    break
        elif command.lower() == "move right":
            if guard["Active"]:
                print(ROOM_HALLWAY_A_DESC + GUARD_PRESENT)
            else:
                print(ROOM_HALLWAY_A_DESC)
            player["Location"] = ROOM_HALLWAY_A
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "induce":
            induce_guard()
        elif command.lower() == "stab guard":
            stab_guard()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
    elif player["Location"] == ROOM_STORAGE:
        if command.lower() == "look at shelf":
            if "Sword" not in player["Inventory"]:
                if "Sling shot" not in player["Inventory"]:
                    print(W_SHELF_W_BOTH)
                else:
                    print(W_SHELF_W_SWORD)
            else:
                if "Sling shot" not in player["Inventory"]:
                    print(W_SHELF_W_SLING)
                else:
                    print(W_SHELF_DESC)
        elif command.lower() == "pick sword":
            if "Sword" not in player["Inventory"]:
                print(PICK_SWORD)
                player["Inventory"].append("Sword")
            else:
                print(SORRY)
        elif command.lower() == "pick sling shot":
            if "Sling shot" not in player["Inventory"]:
                print(PICK_SLING)
                player["Inventory"].append("Sling shot")
            else:
                print(SORRY)
        elif command.lower() == "go south":
            if guard["Active"]:
                print(ROOM_HALLWAY_A_DESC + GUARD_PRESENT)
            else:
                print(ROOM_HALLWAY_A_DESC)
            player["Location"] = ROOM_HALLWAY_A
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "induce":
            induce_guard()
        elif command.lower() == "stab guard":
            stab_guard()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
    elif player["Location"] == ROOM_DUNGEON:
        if command.lower() == "open gate":
            if not Gate_Open:
                if "Key" not in player["Inventory"]:
                    print(NO_GATE_KEY_DESC)
                else:
                    print(OPEN_GATE_DESC)
                    Gate_Open = True
            else:
                print(SORRY)
        elif command.lower() == "rescue love":
            if not Gate_Open:
                print(GATE_LOCK_DESC)
            else:
                print(RESCUE_LOVE_DESC)
                player["Love_Rescued"] = True
        elif command.lower() == "go south":
            if guard["Active"]:
                print(ROOM_HALLWAY_B_DESC + GUARD_PRESENT)
            else:
                print(ROOM_HALLWAY_B_DESC)
            player["Location"] = ROOM_HALLWAY_B
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "induce":
            induce_guard()
        elif command.lower() == "stab guard":
            stab_guard()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
    elif player["Location"] == ROOM_DEN:
        if command.lower() == "stab lion":
            if Lion_Alive:
                if "Sword" in player["Inventory"]:
                    print(STAB_LION_DESC + " " + LION_DEAD_DESC)
                    Lion_Alive = False
                    Lion_Health = 0
                else:
                    print(SORRY)
            else:
                print(SORRY)
        elif command.lower() == "shoot lion":
            if Lion_Alive or Lion_Health > 0:
                if "Sling shot" in player["Inventory"]:
                    Lion_Health -= 50
                    if Lion_Health > 0:
                        print(SHOOT_DESC + ", but it is not dead yet")
                    else:
                        print(SHOOT_DESC + LION_DEAD_DESC)
                        Lion_Alive = False
                else:
                    print(SORRY)
            else:
                print(SORRY)
        elif command.lower() == "look at key":
            if "Key" not in player["Inventory"]:
                print(LOOK_KEY_DESC)
            else:
                print(SORRY)
        elif command.lower() == "pick key":
            if not Lion_Alive:
                if "Key" not in player["Inventory"]:
                    print(PICK_KEY_DESC)
                    player["Inventory"].append("Key")
                else:
                    print(SORRY)
            else:
                print(KILLED_BY_LION)
                break
        elif command.lower() == "go north":
            if guard["Active"]:
                print(ROOM_HALLWAY_A_DESC + GUARD_PRESENT)
            else:
                print(ROOM_HALLWAY_A_DESC)
            player["Location"] = ROOM_HALLWAY_A
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)                
    elif player["Location"] == ROOM_CHAMBER:
        if command.lower() == "show documents":
            if not player["Blackmailed"]:
                if "Documents" in player["Inventory"]:
                    print(SHOW_DOC_DESC)
                    player["Blackmailed"] = True
                else:
                    print(NO_DOC_DESC)
            else:
                print(SORRY)
        elif command.lower() == "threaten king":
            if not player["Threatened"]:
                if "Sword" in player["Inventory"]:
                    print(THREATEN_DESC)
                    player["Threatened"] = True
                else:
                    print(THREATEN_FAIL)
            else:
                print(SORRY)
        elif command.lower() == "go east":
            if player["Blackmailed"]:
                print(B_MAIL_DESC)
                Won = True
            else:
                print(ROOM_HALLWAY_B_DESC)
                player["Location"] = ROOM_HALLWAY_B
        elif command.lower() == "stats":
            player_stats()
        elif command.lower() == "save":
            save_progress()
        elif command.lower() == "load":
            load_game()
        else:
            print(SORRY)
