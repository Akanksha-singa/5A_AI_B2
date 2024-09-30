print("Akanksha Singa")
print("1BM22CS027")
class VacuumCleaner:
    def __init__(self, room_a_dirt, room_b_dirt, starting_room):
        self.current_state = (room_a_dirt, room_b_dirt, starting_room)

    def is_goal_state(self):
        return self.current_state[0] == 0 and self.current_state[1] == 0

    def clean(self):
        if self.current_state[0] == 1:
            self.current_state = (0, self.current_state[1], self.current_state[2])
            print("Cleaned room A.")
        elif self.current_state[1] == 1:
            self.current_state = (self.current_state[0], 0, self.current_state[2])
            print("Cleaned room B.")

    def move(self):
        if self.current_state[2] == 'A':
            self.current_state = (self.current_state[0], self.current_state[1], 'B')
            print("Moved to room B.")
        else:
            self.current_state = (self.current_state[0], self.current_state[1], 'A')
            print("Moved to room A.")

    def run(self):
        while not self.is_goal_state():
            print(f"Current state: {self.current_state}")
            self.clean()
            if not self.is_goal_state():
                self.move()
        print("Both rooms are clean!")

def get_initial_state():
    room_a_dirt = int(input("Is room A dirty? (1 for yes, 0 for no): "))
    room_b_dirt = int(input("Is room B dirty? (1 for yes, 0 for no): "))
    starting_room = input("Which room is the vacuum cleaner in? (A or B): ").strip().upper()
    if starting_room not in ['A', 'B'] or room_a_dirt not in [0, 1] or room_b_dirt not in [0, 1]:
        print("Invalid input. Please enter the correct values.")
        return get_initial_state()
   
    return room_a_dirt, room_b_dirt, starting_room

initial_state = get_initial_state()
vacuum = VacuumCleaner(*initial_state)
vacuum.run()
