import csv
from triager import triage_complaint

total = 0
equipment_correct = 0
urgency_correct = 0
hospital_correct = 0
full_correct = 0

with open("complaints.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += 1
        result = triage_complaint(row["complaint"])

        equipment_ok = result.equipment == row["expected_equipment"]
        urgency_ok = result.urgency == row["expected_urgency"]
        hospital_ok = (result.hospital or "") == row["expected_hospital"]

        equipment_correct += equipment_ok
        urgency_correct += urgency_ok
        hospital_correct += hospital_ok
        full_correct += equipment_ok and urgency_ok and hospital_ok

print("\n--- Evaluation Results ---")
print(f"Total complaints: {total}")
print(f"Equipment accuracy: {equipment_correct}/{total} ({equipment_correct/total*100:.1f}%)")
print(f"Urgency accuracy: {urgency_correct}/{total} ({urgency_correct/total*100:.1f}%)")
print(f"Hospital accuracy: {hospital_correct}/{total} ({hospital_correct/total*100:.1f}%)")
print(f"Overall accuracy: {full_correct}/{total} ({full_correct/total*100:.1f}%)")
