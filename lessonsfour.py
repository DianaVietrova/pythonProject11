import random

class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House(food=100, mess=0)

    def get_car(self, brand_list):
        self.car = Auto(brand_list)

    def get_job(self, job_list):
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
            return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day_text = f" Today is day {day} of {self.name}'s life "
        print(f"{day_text:=^50}", "\n")

        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")

        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")

        car_indexes = f"{self.car.brand} car indexes "
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            print("You need to get a car first.")
            return False
        if self.job is None:
            print("You need to get a job first.")
            return False

        self.days_indexes(day)
        dice = random.randint(1, 4)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

    def interact_with_friend(self, friend):
        action = random.choice(["talk", "hang_out", "help"])
        if action == "talk":
            print(f"{self.job} разговаривает с другом {friend.name}.")
            self.gladness += 5
        elif action == "hang_out":
            print(f"{self.job} встречается с другом {friend.name}.")
            self.money -= 20
            self.gladness += 10
        elif action == "help":
            print(f"{self.job} помогает другу {friend.name}.")
            friend.gladness += 5
            self.money -= 10
            self.gladness -= 5


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self, food, mess):
        self.mess = mess
        self.food = food


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class Friend:
    def __init__(self, name):
        self.name = name
        self.gladness = 50

    def interact_with_human(self, human):
        action = random.choice(["talk", "hang_out", "help"])
        if action == "talk":
            print(f"{self.name} разговаривает с другом {human.name}.")
            self.gladness += 5
        elif action == "hang_out":
            print(f"{self.name} встречается с другом {human.name}.")
            human.money -= 20
            self.gladness += 10
        elif action == "help":
            print(f"{self.name} помогает другу {human.name}.")
            human.gladness += 5
            human.money -= 10
            self.gladness -= 5


job_list = {
    "Java developer": {
        "salary": 50,
        "gladness_less": 10
    },
    "Python developer": {
        "salary": 40,
        "gladness_less": 3
    },
    "C++ developer": {
        "salary": 45,
        "gladness_less": 25
    },
    "Rust developer": {
        "salary": 70,
        "gladness_less": 1
    },
}

brands_of_car = {
    "BMW": {
        "fuel": 100,
        "strength": 100,
        "consumption": 6
    },
    "Lada": {
        "fuel": 50,
        "strength": 40,
        "consumption": 10
    },
    "Volvo": {
        "fuel": 70,
        "strength": 150,
        "consumption": 8
    },
    "Ferrari": {
        "fuel": 80,
        "strength": 120,
        "consumption": 14
    },
}

nick = Human(name="Nick")
diana = Friend(name="Diana")

for day in range(1, 8):
    if not nick.live(day):
        break
    nick.get_home()
    if nick.car is None:
        nick.get_car(brands_of_car)
    if nick.job is None:
        nick.get_job(job_list)
    nick.live(day)
    nick.interact_with_friend(diana)
    diana.interact_with_human(nick)
