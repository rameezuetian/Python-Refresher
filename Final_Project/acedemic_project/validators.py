from exception import invalidStudentRecord , MissingFieldError

def validate_student_record(row):
    if not row["name"]:
        raise MissingFieldError("Student name is missing.")
    
    marks = int(row["marks"])

    late_days = int(row["late_days"])

    if marks < 0  or marks > 100:
        raise invalidStudentRecord("Invalid Marks")
    
    if late_days < 0 :
        raise invalidStudentRecord("Late Days cannot be negative")