class Student:
    def __init__(self, ism: str, fam: str, kurs: int):
        self.name = ism
        self.familiya = fam
        self.course = kurs

    def borish(self):
        print(f"{self.name} har kuni 20 minut kech qoladi.")

    def kelish(self):
        print(f"{self.name} har kuni darslardan qochadi")


student1 = Student("Azamat", "Abdullayev", 3)

print(student1.kelish())


class Laptop:
    def __init__(self,brand:str, model: str, memory: int, mem_type: str, ram: int):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.mem_type = mem_type
        self.ram = ram

    def information(self):
        print(f"Brand: {self.brand}")
