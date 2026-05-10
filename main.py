from typing import List
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    cnic: str

    def __str__(self):
        return f"{self.name}, {self.age}, {self.cnic}"

@dataclass
class Class:
    title: str
    students: List[Student]

    def __str__(self):
        return f"{self.title}, {[st.name for st in self.students]}"


zainab = Student(name="Zainab Siddiq", age=22, cnic="345768684756")
sundas = Student(name="Sundas", age=22, cnic="375687487563")

zainab2 = Student(name="Zainab Siddiq", age=22, cnic="345768684756")

sundas1 = Student(name="Sundas", age=22, cnic="375687487563")


clss = Class(title="Software Engineering", students=[zainab, sundas, zainab2, sundas1])
print(clss)
