"""Job application tracker, step 1: add applications and list them.

Data lives in applications.csv, one row per application.
"""
import csv
import sys
from datetime import date
from pathlib import Path

DATA_FILE = Path("applications.csv")
FIELDS = ["company", "role", "date_applied", "status"]


def load_applications():
    """Read every row from the CSV file into a list of dictionaries."""
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open(newline="") as f:
        return list(csv.DictReader(f))


def save_applications(applications):
    """Write the full list back to the CSV file."""
    with DATA_FILE.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(applications)


def add_application(company, role):
    applications = load_applications()
    applications.append({
        "company": company,
        "role": role,
        "date_applied": date.today().isoformat(),
        "status": "applied",
    })
    save_applications(applications)
    print(f"Added: {role} at {company}")


def list_applications():
    applications = load_applications()
    if not applications:
        print("No applications yet.")
        return
    for app in applications:
        print(f"{app['date_applied']}  {app['company']:<20} {app['role']:<25} [{app['status']}]")


def main():
    args = sys.argv[1:]  # everything typed after "python3 tracker.py"
    if args[:1] == ["add"] and len(args) == 3:
        add_application(args[1], args[2])
    elif args[:1] == ["list"]:
        list_applications()
    else:
        print('Usage:\n  python3 tracker.py add "Company" "Role"\n  python3 tracker.py list')


if __name__ == "__main__":
    main()
