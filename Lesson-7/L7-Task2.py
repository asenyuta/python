# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_consumption_coat(self):
        return self.V / 6.5 + 0.5

    def get_consumption_suit(self):
        return self.H * 2 + 0.3

    @property
    def get_consumption(self):
        return str(f'Общий расход: {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.consumption_coat = self.V / 6.5 + 0.5

    def get_consumption(self):
        return self.consumption_coat

    def __str__(self):
        return str(f'Расход на пальто {self.consumption_coat}')


class Suit(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.consumption_suit = self.H * 2 + 0.3

    def get_consumption(self):
        return self.consumption_suit

    def __str__(self):
        return str(f'Расход на костюм {self.consumption_suit}')

coat1 = Coat(5, 10)
suit1 = Suit(5, 10)
c1=Clothes(5,10)
print(coat1)
print(suit1)
print(coat1.get_consumption())
print(suit1.get_consumption())
#print(c1.get_consumption())
