with open('Start.txt') as intro_file:
    read_intro = intro_file.read()
    print(read_intro)
    intro_file.closed

rooms_file = open('Rooms.txt')
print(rooms_file)
