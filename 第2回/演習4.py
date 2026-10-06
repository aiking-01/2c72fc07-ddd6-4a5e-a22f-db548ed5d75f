class Person:
    def __init__(self, lname, fname, num):
        self.lastname = lname
        self.firstname = fname
        self.age = num

    def print_person(self):
        print("First Name: ", self.lastname)
        print("Last Name: ", self.firstname)
        print("Age: ", self.age)