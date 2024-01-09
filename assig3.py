class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_info(self, name=None, age=None, address=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

person = Person("Ammu", 15, "Eravakkad")


person.display_info()


person.update_info(age=22)


person.update_info(address="kochi,vennala")


person.display_info()
