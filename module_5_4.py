class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name  # имя
        self.number_of_floors = number_of_floors  # кол-во этажей

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"Такого этажа не существует.")
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return f"Ожидаемый тип данных `House`, принят {type(other)}"

    # ----- Сложение -----
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    # ----- Вычитание -----
    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __rsub__(self, value):
        if isinstance(value, int):
            return self.__sub__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __isub__(self, value):
        if isinstance(value, int):
            return self.__sub__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    # ----- Умножение -----
    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
            return self
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __rmul__(self, value):
        if isinstance(value, int):
            return self.__mul__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __imul__(self, value):
        if isinstance(value, int):
            return self.__mul__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    # ----- Деление -----
    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors /= value
            return self
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __rtruediv__(self, value):
        if isinstance(value, int):
            return self.__truediv__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"

    def __itruediv__(self, value):
        if isinstance(value, int):
            return self.__truediv__(value)
        else:
            return f"Ожидаемый тип данных `int`, принят {type(value)}"


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
