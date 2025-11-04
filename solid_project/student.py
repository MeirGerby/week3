class Student:
    """store the student's data"""
    def __init__(self, name: str, grades: list[int]):
        self.name: str = name
        self.grades: list[int] = grades

    def __str__(self):
        return (f'----------\n'
                f'Name: {self.name}\n'
                f'Grades: {self.grades}\n'
                f'----------\n')


class GradeCalculator:
    """
    calculate the student's average
    return: the name of student and the average
    """
    print("GradeCalculator Class: check what exactly should I need to do")
    @staticmethod
    def average_grade(grades):
        return sum(grades) / len(grades)



