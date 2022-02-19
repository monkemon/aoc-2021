from ast import Sub


class Submarine():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0
        pass

    def perform_move(self, string):
        parameters = string.split(' ')

        move_direction = parameters[0]
        value = int(parameters[1])

        if move_direction == 'forward':
            self.x = self.x + value
            self.y += self.aim * value
        
        elif move_direction == 'up':
            self.aim = self.aim - value
            
        elif move_direction == 'down':
            self.aim = self.aim + value
        
        else:
            print("move not recognized")

        print(f"{self.x}, {self.y}, {self.aim}")

    def print_status(self):
        print(f"Submarine horizontal position is {self.x}, and its depth is {self.y}")    


def main():
    sub = Submarine()

    input_data = open("submarine_control.txt")
    for input_action in input_data:
        sub.perform_move(input_action)

    sub.print_status()

if __name__ == "__main__":
    main()