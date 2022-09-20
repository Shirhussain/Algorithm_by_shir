from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


shir = Student("Shir")
elon = Student("Elon")

shir.take_exam(100)
print(shir.grades)
print(elon.grades)

# now you see that elone didn't took exame but have the grade
# the proble is with the list [] which is mutable we have have None instad by defulat.


# do not use any mutable in parametet
class Student:
    # def __init__(self, name: str, grades: List[int] = None):
    # or make it optional
    def __init__(self, name: str, grades: Optional[List[int]] = None):

        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


shir = Student("Shir")
elon = Student("Elon")

shir.take_exam(100)
print(shir.grades)
print(elon.grades)
