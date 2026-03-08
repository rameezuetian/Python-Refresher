import datetime
def generate_report(summary):

    timestamp = datetime.datetime.now()

    report = f"""
ACADEMIC PORTAL REPORT
----------------------

Total Students : {summary['total_students']}
Failed Students: {summary['total_failed_students']}
Total Fine     : {summary['total_fine']}

Generated At: {timestamp}
"""

    return report


def save_report(report):

    filename = f"reports/report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write(report)

    print("Report saved:", filename)