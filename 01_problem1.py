class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("zakir", 120000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = programmer("Harry", 120000, 245001)
print(r.name, r.salary, r.pin, r.company)
