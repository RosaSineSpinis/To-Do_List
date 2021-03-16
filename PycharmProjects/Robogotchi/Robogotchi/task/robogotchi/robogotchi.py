# Write your code here
import random


class BiggerThanMillion(Exception):
    def __str__(self):
        return "Invalid input! The number can't be bigger than 1000000"


class NegativeNumber(Exception):
    def __init__(self):
        self.message = "The number can't be negative!"
        super().__init__(self.message)


class Stats:
    def __init__(self):
        self.player_won = 0
        self.robot_won = 0
        self.draw_stats = 0


    def print_statistics(self):
        print(f"You won: {self.player_won},")
        print(f"Robot won: {self.robot_won},")
        print(f"Draws: {self.draw_stats}.")


class Robogotchi:
    def __init__(self):
        self.robot_number = None
        self.player_number = None
        self.unknown_number = None

        self.player_won = 0
        self.robot_won = 0
        self.draw = 0

        while True:
            print("\nWhat is your number? ")
            command = input()
            # check whether it works for capital letters too
            if command == "exit game":
                self.print_statistics()
                break
            try:
                self.player_number = int(command)
                if 1000000 <= self.player_number:
                    # print("Invalid input! The number can't be bigger than 1000000")
                    raise BiggerThanMillion
                    continue
                elif self.player_number <= 0:
                    # print("The number can't be negative!")
                    raise NegativeNumber
                    continue
                # elif not command.isnumeric()
                else:
                    self.unknown_number = self.choose_number()
                    self.robot_number = self.choose_number()
                    self.print_results()
            except ValueError:
                print("A string is not a valid input a string is not a valid input")
            except BiggerThanMillion as mln:
                print(mln)
            except NegativeNumber as neg:
                print(neg)

    @staticmethod
    def choose_number():
        return random.randint(0, 1000000)

    def print_results(self):
        print(f"\nThe robot entered the number {self.robot_number}.")
        print(f"The goal number is {self.unknown_number}.")
        # print("self.unknown_number", self.unknown_number, "self.player_number", self.player_number)
        if abs(self.unknown_number - self.player_number) < abs(self.unknown_number - self.robot_number):
            print("You won!")
            self.player_won += 1
        elif abs(self.unknown_number - self.player_number) == abs(self.unknown_number - self.robot_number):
            print("It's a draw!")
            self.draw += 1
        else:
            print("The robot won!")
            self.robot_won += 1

    def print_statistics(self):
        print(f"You won: {self.player_won},")
        print(f"Robot won: {self.robot_won},")
        print(f"Draws: {self.draw}.")


class WrongChoice(Exception):
    def __init__(self):
        self.message = "\nNo such option! Try again!"
        super().__init__(self.message)


class RockPaperScissors(Stats):
    choices = ["rock", "paper", "scissors"]

    def __init__(self):
        super().__init__()

        self.robot_choice = None
        self.player_choice = None

        while True:
            print("\nWhat is your move? ")
            self.command = input()
            self.robot_choice = self.choices[random.randint(0, 2)]

            try:
                if self.command == "exit game":
                    self.print_statistics()
                    break

                elif self.command in self.choices:
                    self.print_results()

                else:
                    raise WrongChoice
            except WrongChoice as wc:
                print(wc)

    def print_robot_chose(self):
        print(f"Robot chose {self.robot_choice} ")

    def print_results(self):
        draw = "It's a draw!"
        player = "You won!"
        robot = "The robot won!"
        if self.command == self.robot_choice:
            self.print_robot_chose()
            self.draw_stats += 1
            print(draw)

        elif self.command == "paper":
            self.print_robot_chose()
            if self.robot_choice == "rock":
                self.player_won += 1
                print(player)
            else:
                self.robot_won += 1
                print(robot)

        elif self.command == "rock":
            self.print_robot_chose()
            if self.robot_choice == "scissors":
                self.player_won += 1
                print(player)
            else:
                self.robot_won += 1
                print(robot)

        elif self.command == "scissors":
            self.print_robot_chose()
            if self.robot_choice == "paper":
                self.player_won += 1
                print(player)
            else:
                self.robot_won += 1
                print(robot)


class WrongGameName(Exception):
    def __init__(self):
        self.message = "\nPlease choose a valid option: Numbers or Rock-paper-scissors? "
        super().__init__(self.message)


# class GameMenu:
#     def __init__(self):
#         while True:
#             print("\nWhich game would you like to play? ")
#             self.command = input()
#             try:
#                 if self.command == "Numbers":
#                     obj1 = Robogotchi()
#                     break
#                 elif self.command == "Rock-paper-scissors":
#                     RockPaperScissors()
#                     break
#                 else:
#                     raise WrongGameName
#             except WrongGameName as wn:
#                 print(wn)


class WrongMenuEntry(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class Robot:
    def __init__(self):
        self.robot_name = None
        self.lvl_battery = 100
        self.lvl_overheat = 0
        self.lvl_skills = 0
        self.lvl_boredom = 0
        self.command = None
        # stage 4
        self.lvl_rust = 0

        self.set_name()
        self.menu()

    def set_name(self):
        print("How will you call your robot?")
        self.robot_name = input()

    def print_actions(self):
        print(f"\nAvailable interactions with {self.robot_name}:")
        print("exit – Exit")
        print("info – Check the vitals")
        # print(" work - Work")
        print("work – Work")
        print("play – Play")
        # print("oil - Oil")
        print("oil – Oil")
        print("recharge – Recharge")
        print("sleep – Sleep mode")
        # print("learn - Learn skills")
        print("learn – Learn skills")

    def menu(self):
        while True:
            self.print_actions()
            print("\nChoose: ")
            self.command = input()
            try:
                if self.command == "exit":
                    self.exit()
                    break
                elif self.command == "info":
                    self.info()
                    continue
                elif self.command == "recharge":
                    self.recharge()
                    continue
                elif self.command == "sleep":
                    self.sleeping_mode()
                    continue
                elif self.command == "play":
                    if self.play_menu():
                        continue
                    # if self.play_stats():
                    #     continue
                    else:
                        self.exit()
                        break
                elif self.command == "work":
                    if self.work():
                        continue
                    else:
                        self.exit()
                        break
                elif self.command == "oil":
                    self.oil()
                elif self.command == "learn":
                    if self.learn():
                        continue
                    else:
                        self.exit()
                        break
                else:
                    raise WrongMenuEntry("\nInvalid input, try again!")

            # except WrongMenuEntry("\nInvalid input, try again!") as wgn:
            #     print(wgn)
            except WrongMenuEntry as wgn:
                print(wgn)

    def oil(self):
        if self.lvl_rust == 0:
            print(f"{self.robot_name} is fine, no need to oil!")
            return

        if self.is_critical_lvl():
            return 1

        previous_lvl_rust = self.lvl_rust

        self.lvl_rust = self.lvl_rust - 20 if self.lvl_rust > 20 else 0

        print(f"{self.robot_name}'s level of rust was {previous_lvl_rust}."
              f" Now it is {self.lvl_rust}. {self.robot_name} is less rusty!")

    def is_critical_lvl(self):
        if self.lvl_overheat >= 100:
            print(f"The level of overheat reached 100, {self.robot_name} has blown up! Game over. Try again?")
            return 1

        if self.lvl_rust >= 100:
            print(f'{self.robot_name} is too rusty! Game over. Try again?')
            return 1

        if self.lvl_battery <= 0:
            print(f"The level of the battery is 0, {self.robot_name} needs recharging!")
            return 1

        if self.lvl_boredom >= 100:
            print(f'{self.robot_name} is too bored! {self.robot_name} needs to have fun!')
            return 1

    def random_accidents(self):
        # dictionary to randomly choose coefficient and text to print
        rust_action = {f"Oh no, {self.robot_name} stepped into a puddle!": 10,
                       f"Oh, {self.robot_name} encountered a sprinkler!.": 30,
                       f"Guess what! {self.robot_name} fell into the pool!": 50,
                       f"nothing": 0}

        rust_text = random.choice(list(rust_action.keys()))
        rust_factor = rust_action[rust_text]
        return rust_text, rust_factor

    def work(self):
        if self.lvl_skills < 50:
            print(f"{self.robot_name} has got to learn before working!")
            return 1

        previous_lvl_battery = self.lvl_battery
        previous_lvl_rust = self.lvl_rust
        previous_lvl_boredom = self.lvl_boredom
        previous_lvl_overheat = self.lvl_overheat

        rust_text, rust_factor = self.random_accidents()
        self.lvl_rust = self.lvl_rust + rust_factor if self.lvl_rust + rust_factor < 100 else 100
        if rust_text != "nothing":
            print(rust_text)
            print(f"{self.robot_name}'s level of rust was {previous_lvl_rust}. Now it is {self.lvl_rust}.")

        if self.is_critical_lvl():
            print("critical working")
            return 0

        # changes of parameters
        self.lvl_battery = self.lvl_battery -10 if self.lvl_battery > 10 else self.lvl_battery - self.lvl_battery
        self.lvl_boredom = self.lvl_boredom + 10 if self.lvl_boredom < 90 else 100
        self.lvl_overheat = self.lvl_overheat + 10 if self.lvl_overheat < 90 else 100




        # write message what changed
        print(f"{self.robot_name}'s level of boredom was {previous_lvl_boredom}. Now it is {self.lvl_boredom}.")
        print(f"{self.robot_name}'s level of overheat was {previous_lvl_overheat}. Now it is {self.lvl_overheat}.")
        print(f"{self.robot_name}'s level of the battery was {previous_lvl_battery}. Now it is {self.lvl_battery}.")
        print(f"\n{self.robot_name} did well!")


        # level of boredom, overheat, battery.
        return 1

    def learn(self):
        previous_lvl_skills = self.lvl_skills
        previous_lvl_overheat = self.lvl_overheat
        previous_lvl_battery = self.lvl_battery
        previous_lvl_boredom = self.lvl_boredom

        if previous_lvl_skills == 100:
            print(f"There's nothing for {self.robot_name} to learn!")
            return 1

        if self.lvl_battery == 0:
            print(f"The level of the battery is 0, {self.robot_name} needs recharging!")
            return 1

        self.lvl_skills += 10
        # self.lvl_battery -= 10
        self.lvl_battery = self.lvl_battery - 10 if self.lvl_battery > 10 else self.lvl_battery - self.lvl_battery
        self.lvl_overheat += 10

        self.lvl_boredom += 5

        # if self.lvl_overheat >= 100:
        #     print(f"The level of overheat reached 100, {self.robot_name} has blown up! Game over. Try again?")
        #     return 0

        if self.is_critical_lvl():
            return 0

        print(f"{self.robot_name}'s level of skill was {previous_lvl_skills}. Now it is {self.lvl_skills}.")
        print(f"{self.robot_name}'s level of overheat was {previous_lvl_overheat}. Now it is {self.lvl_overheat}.")
        print(f"{self.robot_name}'s level of the battery was {previous_lvl_battery}. Now it is {self.lvl_battery}.")
        print(f"{self.robot_name}'s level of boredom was {previous_lvl_boredom}. Now it is {self.lvl_boredom}.\n")
        print(f"{self.robot_name} has become smarter!")

        return 1

    def play_stats(self):
        previous_lvl_boredom = self.lvl_boredom
        previous_lvl_overheat = self.lvl_overheat

        # --------------------------- double check - 10 or - 20

        self.lvl_boredom = self.lvl_boredom - 10 if self.lvl_boredom >= 10 else self.lvl_boredom - self.lvl_boredom

        # rust_text, rust_factor = self.random_accidents()
        # self.lvl_rust = self.lvl_rust + rust_factor if self.lvl_rust + rust_factor < 100 else 100
        #
        self.lvl_overheat = self.lvl_overheat + 10

        # if self.is_critical_lvl():
        #     return 0

        # if self.lvl_overheat >= 100:
        #     print(f"The level of overheat reached 100, {self.robot_name} has blown up! Game over. Try again?")
        #     return 0

        print(f"{self.robot_name}'s level of overheat was {previous_lvl_overheat}. Now it is {self.lvl_overheat}.")
        print(f"\n{self.robot_name}'s level of boredom was {previous_lvl_boredom}. Now it is {self.lvl_boredom}.")
        print(f"{self.robot_name} is in a great mood")

        return 1

    def play_menu(self):
        while True:

            # print("\nRock-paper-scissors or Numbers? ")
            print("\nwhich game would you like to play?")
            self.command = input()
            # print("self.command", self.command)

            try:
                if self.command.lower() in ["Numbers", "numbers"]:
                    Robogotchi()

                    previous_lvl_rust = self.lvl_rust
                    rust_text, rust_factor = self.random_accidents()
                    self.lvl_rust = self.lvl_rust + rust_factor if self.lvl_rust + rust_factor < 100 else 100
                    if rust_text != "nothing":
                        print(rust_text)
                        print(f"{self.robot_name}'s level of rust was {previous_lvl_rust}. Now it is {self.lvl_rust}.")
                    if self.is_critical_lvl():
                        return 0

                    self.play_stats()

                    break

                elif self.command.lower() in ["Rock-paper-scissors", "rock-paper-scissors"]:
                    RockPaperScissors()

                    previous_lvl_rust = self.lvl_rust
                    rust_text, rust_factor = self.random_accidents()
                    self.lvl_rust = self.lvl_rust + rust_factor if self.lvl_rust + rust_factor < 100 else 100
                    if rust_text != "nothing":
                        print(rust_text)
                        print(f"{self.robot_name}'s level of rust was {previous_lvl_rust}. Now it is {self.lvl_rust}.")
                    if self.is_critical_lvl():
                        return 0

                    self.play_stats()

                    break

                else:
                    raise WrongGameName

            except WrongGameName as wn:
                print(wn)
        return 1

    def recharge(self):
        if self.lvl_boredom == 100:
            print(f"{self.robot_name} is charged!")
            return
        previous_lvl_boredom = self.lvl_boredom
        previous_lvl_overheat = self.lvl_overheat
        previous_lvl_battery = self.lvl_battery

        self.lvl_overheat = self.lvl_overheat - 5 if self.lvl_overheat - 5 > 0 else 0
        self.lvl_battery = self.lvl_battery + 10 if self.lvl_battery + 10 < 100 else 100
        self.lvl_boredom = self.lvl_boredom + 5 if self.lvl_boredom + 5 < 100 else 100

        print(f"{self.robot_name}'s level of overheat was {previous_lvl_overheat}. Now it is {self.lvl_overheat}.")
        print(f"{self.robot_name}'s level of the battery was {previous_lvl_battery}. Now it is {self.lvl_battery}.")
        print(f"{self.robot_name}'s level of boredom was {previous_lvl_boredom}. Now it is {self.lvl_boredom}.")
        print(f"{self.robot_name} is recharged!")

    def sleeping_mode(self):
        previous_lvl_overheat = self.lvl_overheat

        if self.lvl_overheat == 0 and previous_lvl_overheat == 0:
            print(f"{self.robot_name}'s level of overheat was 10. Now it is 0.\n \n{self.robot_name} is cool!")
            return 0

        if self.lvl_battery == 0:
            print(f"The level of the battery is 0, {self.robot_name} needs recharging!")
            return 1

        previous_lvl_overheat = self.lvl_overheat
        self.lvl_overheat = self.lvl_overheat - 20 if self.lvl_overheat > 20 else self.lvl_overheat - self.lvl_overheat

        message = ""
        if self.lvl_overheat == 0:
            message = f'{self.robot_name} is cool'
        else:
            message = f"{self.robot_name} cooled off!"

        print(f"{self.robot_name}'s level of overheat was {previous_lvl_overheat}. Now it is {self.lvl_overheat}.\n \n {message}")
        # print()

    def info(self):
        print(f"{self.robot_name}'s stats are:")
        print(f"battery is {self.lvl_battery},")
        print(f"overheat is {self.lvl_overheat},")
        print(f"skill level is {self.lvl_skills},")
        print(f"boredom is {self.lvl_boredom},")
        print(f"rust is {self.lvl_rust}.")

    def exit(self):
        print("Game over.")


if __name__ == '__main__':
    obj = Robot()
