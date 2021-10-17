class Animals:
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_young_with_milk(self):
            print('кормит детенышей молоком')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')  
    def left_foot_forward(self):
        print('левая нога впереди')
    def right_foot_forward(self):
        print('правая нога впереди')
    def left_foot_back(self):
        print('левая нога назади')
    def right_foot_back(self):
        print('правая нога назади')
    def dance(self):
        self.right_foot_forward()
        self.left_foot_back()
        self.left_foot_forward()
        self.right_foot_back()
reginald = Giraffes()
reginald.dance()


Добавьте в класс Giraffes функции, при вызове которых жираф переставлял бы правую или левую ногу вперед либо назад. Назвать их можно так: left_foot_forward, left_foot_back, right_foot_forward
и right_foot_back. Функция, которая ставит левую ногу жирафа вперед, может выглядеть примерно так:
>>> def left_foot_forward(self):
print('левая нога впереди')
Теперь создайте функцию dance, которая научит Реджинальда танцевать (вызывая четыре только что созданные функции для передвижения ног). В результате должен получиться несложный танец:
>>> reginald = Giraffes()
>>> reginald.dance()
левая нога впереди
левая нога сзади
правая нога впереди
правая нога сзади
левая нога сзади
правая нога сзади
правая нога впереди
левая нога впереди
