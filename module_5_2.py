class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # имя
        self.number_of_floors = number_of_floors  # кол-во этажей

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"Такого этажа не существует.")
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


elbrHouse = House("ЖК Эльбрус", 30)
elbrHouse.go_to(4)
elbrHouse.go_to(31)
print(len(elbrHouse))
print(str(elbrHouse))
