class invalidSalary(Exception):
    pass

class invalidAge(Exception):
    pass

def calSalary(salary):
    if salary <= 0:
        raise invalidSalary("Invalid Salary Processed")

    print("Salary: ", salary)

def calAge(age):
    if age <= 0:
        raise invalidAge("Invalid Age Entered")

    print("Age: ", age)

try:
    calSalary(100)
    calAge(-1)
except invalidSalary as error:
    print("Error: ",error)
except invalidAge as error:
    print("Error: ",error)
