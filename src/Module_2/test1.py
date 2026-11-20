from dataclasses import dataclass

@dataclass
class Employee:
    empName: str
    empId: int
    empDepartment: str

employee = Employee("Bibhu",76557,"Testing")

print(employee.empId)