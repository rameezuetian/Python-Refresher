from decorators import log_activity
def get_failed_student(students):
    failed = []

    for s in students:
        if s.is_failed():
            failed.append(s)
    return failed



def calculate_total_fine(students):
    total = 0
    for s in students:
        total +=s.calculate_fine()

    return total

@log_activity
def generate_summary(students):
    failed_student = get_failed_student(students)
    calculate_fine = calculate_total_fine(students)

    summary = {
        "total_students" : len(students),
        "total_failed_students": len(failed_student),
        "total_fine" : calculate_fine
    }
    return summary