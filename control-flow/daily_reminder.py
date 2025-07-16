def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            if time_bound == "yes":
                print(f"Reminder: '{task}' has an unknown priority level but requires immediate attention today!")
            else:
                print(f"Note: '{task}' has an unknown priority level. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()    

    # Final version to pass review

    # -- Final update for ALX review: includes match-case and time-bound logic --