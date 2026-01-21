# Student Dataclass
from dataclasses import dataclass

@dataclass   # Need to define data type for dataclass
class Student:
    name: str
    school_id: str
    gpa: float

# String Method
    def __str__(self):
        return f'Name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}'

# Main Method
def main():
    alex = Student("Alex", 'abc123', 3.5)
    print(alex.name)
    alex.gpa = 2.5
    print(alex)
    sarah = Student("Sarah", 'zyx098', 2.7)
    print(sarah.school_id)
    print(sarah)

main()