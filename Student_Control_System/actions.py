import data


def is_valid_name(name):
    if not name.strip(): 
        return False, "The name cannot be empty."
    if any(char.isdigit() for char in name):
        return False, "The name cannot contain numbers."
    return True, ""


def is_valid_section(section):
    section = section.strip()
    if len(section) < 2: 
        return False, "The section must have at least 2 characters (e.g: 10A)."
    if not section[:-1].isdigit() or not section[-1].isalpha(): 
        return False, "The section must be in a valid format (e.g: 11B)"
    return True, ""


def student_exists(data_students, name, section):
    for student in data_students:
        if (student["Name"].strip().lower() == name.strip().lower() and student["Section"].strip().upper() == section.strip().upper()):
            return True
    return False


def get_note(subject):
    while True:
        try:
            note = float(input(f"Enter the {subject} note: "))
            if 0 <= note <= 100:
                return note
            print()
            print("Invalid note. Please enter a value between 0 and 100.")
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")


def enter_student_information(data_students):
    try:
        student_counter = int(input("Enter the number of students: "))
        if student_counter <= 0:
            print("Please enter a number greater than 0.")
            return

        while student_counter != 0:
            print("-"*60)
            while True:
                name = input("Enter the student's full name: ")
                valid, msg = is_valid_name(name)
                if valid:
                    break
                print()
                print(f"Error: {msg}.")
            
            while True:
                section = input("Enter the student section (example: 11B): ")
                valid, msg = is_valid_section(section)
                if valid:
                    break
                print()
                print(f"Error: {msg}.")

            if student_exists(data_students, name, section):
                print(f"Error: There is already a student named {name} in the section {section.upper()}.")
                student_counter -= 1
                continue

            spanish_note = get_note("spanish")
            english_note = get_note("english")
            social_note = get_note("social")
            sciences_note = get_note("sciences")
            student_counter -= 1

            student = {
                "Name":name,
                "Section":section.upper(),
                "Notes":{
                    "Spanish_note":spanish_note,
                    "English_note":english_note,
                    "Social_note":social_note,
                    "Sciences_note":sciences_note,
                    }
                }

            data_students.append(student)
        
    except Exception as error:
        print(f"An unexpected error ocurred: {error}.")
        return


def view_student_information(data_students):
    if not data_students:
        print("There are no registered students.")
        return

    print("Student information:")
    for student in data_students:
        print("-"*60)
        print(f"Name: {student["Name"]}")
        print(f"Section: {student["Section"]}")
        print(f"Spanish note: {student["Notes"]["Spanish_note"]}")
        print(f"English note: {student["Notes"]["English_note"]}")
        print(f"Social note: {student["Notes"]["Social_note"]}")
        print(f"Sciences note: {student["Notes"]["Sciences_note"]}")


def view_the_top_3_students(data_students):
    if not data_students:
        print("There are no registered students.")
        return

    students_with_avg = []
    for student in data_students:
        average = (student["Notes"]["Spanish_note"]+student["Notes"]["English_note"]
                +student["Notes"]["Social_note"]
                +student["Notes"]["Sciences_note"]) / 4
        
        students_with_avg.append({
            "Name": student["Name"],
            "Section": student["Section"],
            "Average": average
        })

        top_3 = sorted(students_with_avg, key=lambda x: x["Average"], reverse=True)[:3]

    print("Top 3 student:")
    print("-" * 60)
    for index, student in enumerate(top_3, 1):
        print(f"Top {index}: {student["Name"]}, section {student["Section"]} with an average of {student["Average"]}.")


def view_average_rating(data_students):
    if not data_students:
        print("There are no registered students.")
        return
    
    averages = 0

    for student in data_students:
        average_student = (student["Notes"]["Spanish_note"]
                +student["Notes"]["English_note"]
                +student["Notes"]["Social_note"]
                +student["Notes"]["Sciences_note"]) / 4
        
        averages += average_student

    total_average = averages / len(data_students)

    print("Average rating")
    print("-"*60)
    print(f"The average among all students is {total_average}.")


def remove_students(data_students):
    if not data_students:
        print("There are no registered students.")
        return
    
    remove_student = input("Enter the student's full name: ").strip()
    remove_section = input("Enter the student's section: ").strip().upper()

    for index, student in enumerate(data_students):
        if remove_student.lower() == student["Name"].lower() and remove_section == student["Section"]:
            confirmation = input("Are you sure you want to eliminate the student?(Yes/No): ").strip()
            if confirmation.lower() == "yes":
                data_students.pop(index)
                print("Student eliminated.")
            else:
                print("Operation cancelled.")
            return
        
    print("The student's name does not match any in the record.")


def view_failed_students(data_students):
    if not data_students:
        print("There ar no registered students.")
        return
    
    subject_names = {
        "Spanish_note": "Spanish",
        "English_note": "English",
        "Social_note": "Social",
        "Sciences_note": "Sciences"
    }

    failed_found = False

    print("Failed students:")
    for student in data_students:
        failed_subjects = {
            subject: note
            for subject, note in student["Notes"].items()
            if note < 60
        }

        if failed_subjects:
            failed_found = True
            print("-" * 60)
            print(f"Name: {student["Name"]}")
            print(f"Section: {student["Section"]}")
            print("Failed subjects:")
            for subject, note in failed_subjects.items():
                print(f" - {subject_names[subject]}: {note}")

    if not failed_found:
        print("-" * 60)
        print("No students have failed any subject.")