class Employee:
    language = "python" #this is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary
        is {self.salary}")

        @staticmethod
        def greet():
            print("Good morning")

zakir = Employee()
# zakir.language = "javascript" # this is a z class atribute
zakir.greet()
zakir.getInfo()
# Employee.getInfo(zakir)
