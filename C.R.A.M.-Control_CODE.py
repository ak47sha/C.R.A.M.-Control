# Task Storage List
task_list = []


def get_assessment_weight(assessment_type):
    """Maps user text input to background weight values using a simple dictionary."""
    weights = {
        "periodic test": 5.0,
        "quarterly exam": 5.0,
        "alternative assessment": 4.5,
        "aa": 4.5,
        "major performance task": 4.5,
        "major project": 4.0,
        "portfolio": 4.0,
        "long test": 3.5,
        "laboratory report": 3.0,
        "practical exam": 3.0,
        "class presentation": 2.5,
        "group reporting": 2.5,
        "short quiz": 2.0,
        "summative quiz": 2.0,
        "seatwork": 1.5,
        "in-class activity": 1.5,
        "recitation": 1.2,
        "oral participation": 1.2,
        "homework": 1.0,
        "daily assignment": 1.0,
    }
    cleaned_type = assessment_type.strip().lower()
    return weights.get(cleaned_type, 1.0)


def calculate_priority_score(task):
    """Calculates priority score using urgency, assessment weight, and hours."""
    days = task["days"]

    if days <= 0:
        urgency_score = 100.0
    else:
        urgency_score = (1.0 / days) * 40.0

    weight_score = get_assessment_weight(task["type"]) * 10.0
    workload_score = task["hours"] * 2.0

    total_score = urgency_score + weight_score + workload_score
    return round(total_score, 2)


def display_agenda():
    """Filters, sorts, and displays the final prioritized study schedule."""
    pending_tasks = []
    for task in task_list:
        if task["status"] != "Completed":
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("\nNo pending assignments! All caught up.")
        return

    # Sort tasks in descending order of priority score
    sorted_agenda = sorted(
        pending_tasks, key=calculate_priority_score, reverse=True
    )

    print("\n" + "=" * 80)
    print("          C.R.A.M. CONTROL: PRIORITIZED STUDY AGENDA          ")
    print("=" * 80)
    print(
        f"{'PRIORITY':<10} | {'SUBJECT':<18} | {'TASK TITLE':<22} | {'TYPE':<16} | {'DUE IN':<8} | {'EST. HR'}"
    )
    print("-" * 80)

    total_study_time = 0.0

    for task in sorted_agenda:
        score = calculate_priority_score(task)

        if task["days"] <= 0:
            due_str = "TODAY"
        else:
            due_str = str(task["days"]) + " day(s)"

        print(
            f"{score:<10.2f} | {task['subject'][:18]:<18} | {task['title'][:22]:<22} | "
            f"{task['type'][:16]:<16} | {due_str:<8} | {task['hours']} hrs"
        )
        total_study_time += task["hours"]

    print("-" * 80)
    print(
        f"TOTAL ESTIMATED STUDY TIME REQUIRED: {round(total_study_time, 2)} HOURS\n"
    )


# --- INTERACTIVE USER INPUT LOOP ---

print("=== WELCOME TO C.R.A.M. CONTROL ===")
print("Log your active assignments to generate your prioritized agenda.\n")

while True:
    print("--- Enter Task Details ---")
    title = input("Task Title: ")
    subject = input("Subject Name: ")
    assessment_type = input(
        "Assessment Type (e.g., Periodic Test, Long Test, Homework): "
    )
    days_remaining = int(input("Days Remaining Until Due: "))
    estimated_hours = float(input("Estimated Study Hours Needed: "))

    # Package input into a dictionary task record
    task = {
        "title": title,
        "subject": subject,
        "type": assessment_type,
        "days": days_remaining,
        "hours": estimated_hours,
        "status": "Pending",
    }

    task_list.append(task)
    print(f"\nTask '{title}' logged successfully!")

    user_choice = (
        input("\nWould you like to log another task? (yes/no): ")
        .strip()
        .lower()
    )
    if user_choice not in ["yes", "y"]:
        break
    print()

# Generate agenda from user inputs
display_agenda()