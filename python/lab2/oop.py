'''Question 1 (OOP – Check you know the Basics):
Create an Employee class (from memory) with some sensible attributes and a single simple method.
Save it in a file called payroll.py. Create a new file monthlyPayroll.py and from this check that you
know how to create an object, access it’s attributes and invoke it’s methods. How would you create
an ‘Academic’ class to inherit from the employee class? Put a __str__ function in both. What happens
if you invoke the __str__ function from the Academic class? What is this called in OOP? Can you set
one of the attributes as private? How would you override this is you used a double underscore?'''

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title
    def __str__(self):
        return f"{self.name}, {self.title}"


class Academic(Employee):
    def __str__(self):
        return f"{self.title}, {self.name}"


p1 = Employee("Dialga", "Accountant")
p2 = Academic("Palkia", "Auditor")
print(p1)
print(p2)

    