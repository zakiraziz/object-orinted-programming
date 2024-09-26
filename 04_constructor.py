class Employee:
    language = "python" #this is a class attribute
    salary = 120000
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language =language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary
        is {self.salary}")

        

        @staticmethod
        def greet():
            print("Good morning")

zakir = Employee("zakir", 13000, "javascript")
# zakir.name = "zakir"
print(zakir.name, zakir.salary, zakir.language)


harry = Employee()
