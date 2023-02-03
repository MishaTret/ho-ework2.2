import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.alive = True

    def feed(self):
        print(f'{self.name} is eating.')
        self.hunger -= 5
        self.happiness += 2

    def play(self):
        print(f'{self.name} is playing.')
        self.hunger += 2
        self.happiness += 5

    def rest(self):
        print(f'{self.name} is resting.')
        self.hunger += 2
        self.happiness += 2

    def check_status(self):
        if self.hunger < 0:
            print(f'{self.name} has died of starvation.')
            self.alive = False
        elif self.happiness < 0:
            print(f'{self.name} has died of sadness.')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger: {self.hunger}')
        print(f'Happiness: {self.happiness}')

    def live_day(self, day):
        day_str = f'Day {day} of {self.name}\'s life'
        print(f"{day_str:=^50}")
        action_num = random.randint(1, 3)
        if action_num == 1:
            self.feed()
        elif action_num == 2:
            self.play()
        elif action_num == 3:
            self.rest()
        self.check_status()
        self.end_of_day()

pet = Pet(name='Fluffy')
for day in range(365):
    if pet.alive == False:
        break
    pet.live_day(day)
