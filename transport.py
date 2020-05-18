class Transport:
    def __init__(self, name, type, color, speed):
        self.name = name
        self.type = type
        self.color = color
        self.speed = speed

    def acceleration(self, acceleration):
        self.speed += acceleration
        return self.speed


class Train(Transport):
    def __init__(self, name='Train', type='Ground', color='Yellow', speed=50, cargo=1):
        super().__init__(name, type, color, speed)
        self.cargo = cargo

    def __str__(self):
        return 'name = {}, type = {}, color = {}, speed = {}, heavy load = {}'\
            .format(self.name, self.type, self.color, self.speed, self.cargo)

    def heavy_load(self, heavy):
        self.cargo += heavy
        return self.cargo


class Plane(Transport):
    def __init__(self, name='Plane', type='Air', color='Black', speed=230):
        super().__init__(name, type, color, speed)

    def __str__(self):
        return 'name = {}, type = {}, color = {}, speed = {}'\
            .format(self.name, self.type, self.color, self.speed)

    def people(self, people):
        if people < 10:
            return 'Это грузовой(спец. назначения) самолёт'
        elif people > 700:
            return 'Это большой пасс. самолёт'
        elif people > 1378:  # Airbus A380
            return 'Ошибка! Самолёта такой вместимости не существует'
        else:
            return 'Это средний самолёт'


train = Train()
print(train)
train.acceleration(20)
print(train)
train.heavy_load(2)
print(train)

plane = Plane()
print(plane)
plane.acceleration(100)
print(plane)
print(plane.people(1110))
