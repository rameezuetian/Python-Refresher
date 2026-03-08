import asyncio
import datetime

from loader import load_students
from processor import generate_summary
from reports import generate_report, save_report


async def async_load_students(file_path):

    print("Loading students...")
    students = load_students(file_path)

    await asyncio.sleep(1)

    return students


async def async_process_students(students):

    print("Processing records...")
    summary = generate_summary(students)

    await asyncio.sleep(1)

    return summary


async def async_generate_report(summary):

    print("Generating report...")

    report = {
        "timestamp": datetime.datetime.now(),
        "summary": summary
    }

    await asyncio.sleep(1)

    return report


async def main():

    students = await async_load_students("data/students.csv")

    summary = await async_process_students(students)

    print(summary)

    report =  generate_report(summary)

    print("\nAcademic Report")
    print(report)

    save_report(report)


asyncio.run(main())