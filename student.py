class Student:
    school="Akirachix"
    def __init__(self,name ,age,country,first_name,last_name):
        self.name=name
        self.age=age
        self.country=country
        self.first_name= first_name
        self.last_name=last_name
    def greet(self):
        return f"Hello {self.name} from {self.country}.Welcome to {self.school}"
    def full_name(self):
        return f"your full name is {self.first_name} {self.last_name}"
    def initials(self):
        return f"your initials is {self.first_name[0]}.{self.last_name[0]}"