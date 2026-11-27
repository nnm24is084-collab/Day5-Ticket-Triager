from pydantic import BaseModel
from typing import Optional, Literal
import re
import json


class ComplaintOutput(BaseModel):
    equipment: str
    urgency: Literal["Low", "Medium", "High", "Critical"]
    hospital: Optional[str] = None
    next_action: str


def triage_complaint(complaint: str) -> ComplaintOutput:

    text = complaint.lower()

    # Equipment detection
    if "oxygen" in text or "spo2" in text:
        equipment = "Oxygen Monitor"
    elif "ventilator" in text:
        equipment = "Ventilator"
    elif "pump" in text:
        equipment = "Infusion Pump"
    elif "ecg" in text or "electrocardiogram" in text:
        equipment = "ECG Machine"
    elif "x-ray" in text or "xray" in text:
        equipment = "X-Ray Machine"
    elif "defibrillator" in text:
        equipment = "Defibrillator"
    else:
        equipment = "Unknown Equipment"

    # Urgency detection
    if "routine" in text:
        urgency = "Low"

    elif any(word in text for word in [
        "life-threatening", "patient affected", "emergency",
        "critical", "stopped", "not working", "shutting down"
    ]):
        urgency = "Critical"

    elif any(word in text for word in [
        "urgent", "alarm", "overheating", "failure",
        "broken", "malfunction"
    ]):
        urgency = "High"

    elif any(word in text for word in [
        "issue", "problem", "error", "fault", "complaint"
    ]):
        urgency = "Medium"

    else:
        urgency = "Low"

    # Hospital name detection
    match = re.search(
        r"(?:at|in)\s+([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*){0,4}\s+Hospital)",
        complaint
    )

    hospital = match.group(1) if match else None

    # Next action
    if urgency == "Critical":
        next_action = "Immediate technician dispatch and escalate to biomedical team."
    elif urgency == "High":
        next_action = "Dispatch technician urgently for inspection and repair."
    elif urgency == "Medium":
        next_action = "Schedule technician inspection."
    else:
        next_action = "Log complaint and monitor equipment."

    return ComplaintOutput(
        equipment=equipment,
        urgency=urgency,
        hospital=hospital,
        next_action=next_action
    )


if __name__ == "__main__":
    complaint = input("Enter equipment complaint: ")

    result = triage_complaint(complaint)

    print("\n--- Triage Result ---")
    print(result.model_dump_json(indent=2))


