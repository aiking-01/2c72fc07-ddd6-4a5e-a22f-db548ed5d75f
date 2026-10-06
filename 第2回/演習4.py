class Person:
    def __init__(self, lname, fname, num):
        self.lastname = lname
        self.firstname = fname
        self.age = num

    def print_person(self):
        print("Last Name: ", self.lastname)
        print("First Name: ", self.firstname)
        print("Age: ", self.age)