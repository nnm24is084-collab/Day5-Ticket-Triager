import csv
from triager import triage_complaint

with open("complaints.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    with open("accuracy.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["complaint", "expected_urgency", "predicted_urgency", "result"])

        for row in reader:
            result = triage_complaint(row["complaint"])
            status = "PASS" if result.urgency == row["expected_urgency"] else "FAIL"

            writer.writerow([
                row["complaint"],
                row["expected_urgency"],
                result.urgency,
                status
            ])

            if status == "FAIL":
                print("Incorrect prediction found!")
                print("Complaint:", row["complaint"])
                print("Expected:", row["expected_urgency"])
                print("Predicted:", result.urgency)

print("accuracy.csv saved successfully!")
