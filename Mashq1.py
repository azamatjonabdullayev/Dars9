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