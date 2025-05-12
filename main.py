import sys
import room

with open('Start.txt') as intro_file:
    read_intro = intro_file.read()
    print(read_intro)
    intro_file.closed

rooms_file = open('Rooms.txt')
rooms_file_lines = rooms_file.readlines()

running = True

def move():
    direction = input("What do you want to do: ")
    if direction == "MOVE WEST":
        print("You moved west!")
    elif direction == "MOVE EAST":
        print("You moved east!")
    elif direction == "MOVE NORTH":
        print("You moved north!")
    elif direction == "MOVE SOUTH":
        print("You moved south!")
    elif direction == "Q":
        sys.exit()
    else:
        print("You didn't move!")
    
    return direction

def replay_quit():
    running = False
    asking_to_replay = True
    replay = input("Choose 'R' to replay or 'Q' to quit: ")
    while asking_to_replay:
        if replay == "R":
            running = True
            asking_to_replay = False
        elif replay == "Q":
            asking_to_replay = False
            sys.exit()
        else:
            replay = input("Invalid command! Choose 'R' to replay or 'Q' to quit: ")

  


room_1 = room.Room(True, False, True, True, False, False)
room_2 = room.Room(False, False, True, True, True, True)
room_3 = room.Room(False, False, False, False, True, True)
room_4 = room.Room(False, True, False, False, False, True)
room_5 = room.Room(False, True, True, True, False, False)
room_6 = room.Room(False, False, True, False, True, False)
room_7 = room.Room(False, False, False, True, False, True)
room_8 = room.Room(False, True, False, False, True, True)
room_9 = room.Room(False, True, False, False, False, False)

current_room = room_1

room_1.describe_room(rooms_file_lines[0])


while running:
    direction = move()

    # Room 1 conditional logic
    if current_room == room_1 and direction == "MOVE WEST":
        print("GAME OVER")
        replay_quit()       
    elif current_room == room_1 and direction == "MOVE EAST":
        current_room = room_2
        room_2.describe_room(rooms_file_lines[1])
        
    elif current_room == room_1 and direction == "MOVE NORTH":
        print("You hit a wall!")
    elif current_room == room_1 and direction == "MOVE SOUTH":
        current_room = room_4
        room_4.describe_room(rooms_file_lines[3])


    # Room 2 conditional logic
    elif current_room == room_2 and direction == "MOVE WEST":
        current_room == room_1
        room_1.describe_room(rooms_file_lines[0])

        # !!! Issue: once in room 1 by moving west again it's not game over
        # it seems the first conditional in Room1 conditional logic is not executed
    elif current_room == room_2 and direction == "MOVE EAST":
        current_room == room_3
        room_3.describe_room(rooms_file_lines[2])
    elif current_room == room_2 and direction == "MOVE NORTH":
        print("You hit a wall!")
    elif current_room == room_2 and direction == "MOVE SOUTH":
        print("You hit a wall!")

    
        

    






# room = None

# def room_1():
#     room = True
#     print(rooms_file_lines[0])
#     return room

# def room_2():
#     room = True
#     print(rooms_file_lines[1])
#     return room

# def room_3():
#     room = True
#     print(rooms_file_lines[2])
#     return room

# def room_4():
#     room = True
#     print(rooms_file_lines[3])
#     return room

# def room_5():
#     room = True
#     print(rooms_file_lines[4])
#     return room

# def room_6():
#     room = True
#     print(rooms_file_lines[5])
#     return room

# def room_7():
#     room = True
#     print(rooms_file_lines[6])
#     return room

# def room_8():
#     room = True
#     print(rooms_file_lines[7])
#     return room

# def room_9():
#     room = True
#     print(rooms_file_lines[8])
#     return room

# print(room)
# first_room = room_1()
# print(first_room)
# second_room = room_2()

# third_room = room_3()

# fourth_room = room_4()

# fifth_room = room_5()

# sixth_room = room_6()

# seventh_room = room_7()

# eighth_room = room_8()

# nonth_room = room_9()


