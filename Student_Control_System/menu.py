import actions
import data

def menu_student_control_system ():
    data_students = []
    option = 0
    while option != 9:
        print("===================================")
        print("|              Menu               |")
        print("|---------------------------------|")
        print("| 1. Enter student information    |")
        print("| 2. View student information     |")
        print("| 3. View the top 3 students      |")
        print("| 4. View average rating          |")
        print("| 5. Export the data to CSV       |")
        print("| 6. Import CSV data              |")
        print("| 7. Remove students              |")
        print("| 8. View failed students         |")
        print("| 9. Exit the system              |")
        print("===================================")

        try:
            option = int(input("Option: "))
        except ValueError as error:
            print(f"\n{error}")
            input("Press Enter to continue: ")
            print()
            continue

        print()
        if option == 1:
            actions.enter_student_information(data_students)

        elif option == 2:
            actions.view_student_information(data_students)

        elif option == 3:
            actions.view_the_top_3_students(data_students)

        elif option == 4:
            actions.view_average_rating(data_students)

        elif option == 5:
            data.export_to_csv(data_students)

        elif option == 6:
            data.import_from_csv(data_students)

        elif option == 7:
            actions.remove_students(data_students)

        elif option == 8:
            actions.view_failed_students(data_students)

        elif option == 9:
            print("Good bye!")
            exit()
        
        else:
            print("Invalid option. please choose a number between 1 and 9.")
            
        if option != 9:
            input("Press Enter to continue: ")
            print()