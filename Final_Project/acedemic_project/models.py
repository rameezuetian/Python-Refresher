from config  import PASS_MARK , FINE_RATE
class Student:

    def __init__(self, student_id, name, marks, late_days):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.late_days = late_days

    def is_failed(self):
        return self.marks < PASS_MARK

    def calculate_fine(self):
        return self.late_days * FINE_RATE

    def __str__(self):
        return f"Student {self.name} | Marks: {self.marks} | Late Days: {self.late_days}"