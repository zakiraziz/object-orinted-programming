class Employee:
    language = "py" #this is a class attribute
    salary = 250000


zakir = Employee()
zakir.name = "zakir" # this is a z class atribute
print(zakir.name, zakir.language, zakir.salary)

rohan = Employee()
rohan.name = "rohan Roro Robison" # this is a z class atribute
print(rohan.name, rohan.language, rohan.salary)

# Here name is object attribute and salary and language are attributes as they directly belong to the class
