def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Note: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Note: '{task}' has an unknown priority level"

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    print("\n" + message)

if __name__ == "__main__":
    main()
