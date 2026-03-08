import csv
from models import Student
from validators import validate_student_record
from exception import invalidStudentRecord, MissingFieldError
from decorators import log_activity , timer

@log_activity
@timer
def load_students(file_path):

    students = []

    with open(file_path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:

                validate_student_record(row)

                student = Student(
                    int(row["id"]),
                    row["name"],
                    int(row["marks"]),
                    int(row["late_days"])
                )

                students.append(student)

            except (invalidStudentRecord, MissingFieldError) as e:

                print("Invalid record:", e)

    return students