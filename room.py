class Room:
    def __init__(self, has_exit, room_n, room_s, room_e, room_w, item):
        self.exit = has_exit
        self.room_n = room_n
        self.room_s = room_s
        self.room_e = room_e
        self.room_w =room_w
        self.item = item

    def describe_room(self, description):
        print(description)