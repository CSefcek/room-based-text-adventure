import room

with open('Start.txt') as intro_file:
    read_intro = intro_file.read()
    print(read_intro)
    intro_file.closed

rooms_file = open('Rooms.txt')
rooms_file_lines = rooms_file.readlines()




room_1 = room.Room(False, False, True, True, False, False)

room_1.describe_room(rooms_file_lines[0])



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


