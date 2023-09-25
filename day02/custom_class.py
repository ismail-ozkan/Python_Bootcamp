import numbers

class Employee:

    is_human = True # similar to static variable of Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self._name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self._name} is working')

    #toString method
    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'
        #return f'name: {self.name}, job_title: {self.job_title}'


employee1 = Employee()

#print(employee1.__name) -> it's not accessible. it's because __name means that private variable isn't accessible out of the class
print(employee1._name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee("taha")
print(employee1._name)

employee3 = Employee("kerem", "SDET")
print(employee2.job_title)
print(employee2.salary)

employee4 = Employee("ismail", "SDET", 60000)
print(employee3.salary)

#print(Employee.name)
print(employee1.is_human)
print(employee2.planet)

employee3.work()
employee1.work()
print(employee1)
print(employee2)
print(employee3)

# In Python there are 3 access modifiers
# __name is private
# _name is protected (accessible from subclass, inheritance)
# name is public

# __init__ has two underscore before and after its name, because it's special method for this class

# __dict__ method returns all attributes of the object in key-value format
