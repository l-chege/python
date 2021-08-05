class Employee:
    # instance attributes
    def __init__(self, name, age, position, year):
        self.name = name
        self.age = age
        self.position = position
        self.year_joined = year

    def print_details(self):
        print(f'Employees datails:  \n Name: {self.name} \n Age: {self.age} \n Position: {self.position} \n Year joined: {self.year_joined}')
    # instance method
    def speak(self, sound="Love my job"):
        return f"{self.name} says {sound}"


class Employee1(Employee):
    employee_1 = Employee("Device Opiyo", 21, "Manager", 2001)
    employee_1.print_details()
    print(employee_1.speak())


class Employee2(Employee):
    employee_2 = Employee("Fredrick  Ngula", 20, "Assistant Manager", 2002)
    employee_2.print_details()
    print(" Strictly doing my duty to my best")


class Employee3(Employee):
    employee_3 = Employee("Laura Chege", 19,"Secreatary", 2006)
    employee_3.print_details()
    def speak(self, sound="Always be punctual"):
        return super().speak(sound)
    print(employee_3.speak())
