from classes import Student, Teacher

print("\n*** Witaj w programie do obsługi bazy szkolnej! ***")

# students_objects = []
# teachers_objects = []
# list_of_school_classes = []

students_objects = [Student("Jan", "Kowalski", "1B"),
                    Student("Marek", "Wójcik", "1B"),
                    Student("Jan", "Kot", "2B")]

teachers_objects = [Teacher("Paweł", "Kozioł", "biologia", ["1B", "2B", "3B"], "2B"),
                    Teacher("Benek", "Ben", "geografia", ["2B", "3B", "4B"])]

list_of_school_classes = ["1B", "2B", "3B", "4B"]

while True:
    user_choice_main_menu = input("Wpisz jedną z poniższych opcji:\n"
                                  "1 - utwórz\n"
                                  "2 - zarządzaj\n"
                                  "3 - koniec\n")

    if user_choice_main_menu == "utwórz" or user_choice_main_menu == "1":
        while True:
            user_choice_create_menu = input("Wybierz typ profilu, który chcesz utworzyć:\n"
                                            "1 - uczeń\n"
                                            "2 - nauczyciel\n"
                                            "3 - wychowawca\n"
                                            "4 - koniec\n")

            if user_choice_create_menu == "uczeń" or user_choice_create_menu == "1":
                print("** Dodawanie profilu ucznia **")
                first_name_from_user = input("Podaj imię: ")
                last_name_from_user = input("Podaj nazwisko: ")
                school_class_from_user = input("Podaj klasę: ")

                students_objects.append(Student(first_name_from_user, last_name_from_user, school_class_from_user))
                print(f"Łączna liczba uczniów to {len(students_objects)}.")

                # Dodanie klasy szkolnej do listy klas szkolnych
                if students_objects[-1].school_class not in list_of_school_classes:
                    list_of_school_classes.append(students_objects[-1].school_class)

            elif user_choice_create_menu == "nauczyciel" or user_choice_create_menu == "2":
                print("** Dodawanie profilu nauczyciela **")
                first_name_from_user = input("Podaj imię: ")
                last_name_from_user = input("Podaj nazwisko: ")
                school_subject_from_user = input("Podaj przedmiot szkolny: ")

                list_school_classes_from_user = []
                while True:
                    list_school_classes_from_user.append(input("Podaj klasy (w celu przerwania naciśnij enter): "))
                    if list_school_classes_from_user[-1] == "":
                        if len(list_school_classes_from_user) == 1:
                            list_school_classes_from_user.pop()
                            print("Wymagane jest dodanie co najmniej jednej klasy.")
                        else:
                            list_school_classes_from_user.pop()
                            break

                teachers_objects.append(Teacher(first_name_from_user, last_name_from_user, school_subject_from_user,
                                                list_school_classes_from_user))
                print(f"Łączna liczba nauczycieli to {len(teachers_objects)}.")
                # print(f"Nauczyciele: {teachers_objects[0].first_name}")

                # Dodanie klas szkolnych do listy klas szkolnych
                for school_class in teachers_objects[-1].school_classes:
                    if school_class not in list_of_school_classes:
                        list_of_school_classes.append(school_class)

            elif user_choice_create_menu == "wychowawca" or user_choice_create_menu == "3":
                print("** Dodawanie profilu wychowawcy **")
                print("Lista nauczycieli: ")
                help_numbers_teachers = []
                for index, teachers in enumerate(teachers_objects, start=1):
                    print(f"{index} - {teachers.first_name} {teachers.last_name}")
                    help_numbers_teachers.append(index)

                class_tutor_from_user = int(input("Wpisz numer nauczyciela, któremu chcesz nadać status wychowawcy: "))
                if class_tutor_from_user not in help_numbers_teachers:
                    print("Należy wybrać numer nauczyciela.")
                    continue

                if teachers_objects[class_tutor_from_user - 1].class_tutor_of:
                    print(f"Wybrany nauczyciel jest już wychowawcą klasy "
                          f"{teachers_objects[class_tutor_from_user - 1].class_tutor_of}.")
                    user_answer = input("Czy chcesz ją nadpisać? (y/n) ")
                    if user_answer == "y":
                        pass
                    elif user_answer == "n":
                        pass
                    else:
                        print("Niewłaściwe polecenie.")

                print("Lista klas: ")
                print(teachers_objects[class_tutor_from_user - 1].school_classes)
                tutor_class_of_from_user = input(f"Wpisz klasę, której wychowawcą będzie "
                                                 f"{teachers_objects[class_tutor_from_user - 1].first_name} "
                                                 f"{teachers_objects[class_tutor_from_user - 1].last_name}: ")
                if tutor_class_of_from_user not in teachers_objects[class_tutor_from_user - 1].school_classes:
                    print("Należy wybrać klasę, którą uczy nauczyciel.")
                for teachers in teachers_objects:
                    if tutor_class_of_from_user == teachers.class_tutor_of:
                        print("Wybrana klasa ma już wychowawcę.")
                        break

                teachers_objects[class_tutor_from_user - 1].class_tutor_of = tutor_class_of_from_user

                print(f"Nauczycielowi {teachers_objects[class_tutor_from_user - 1].first_name} "
                      f"{teachers_objects[class_tutor_from_user - 1].last_name} nadano status wychowawcy klasy "
                      f"{tutor_class_of_from_user}.")

            elif user_choice_create_menu == "koniec" or user_choice_create_menu == "4":
                break

            else:
                print("Niepoprawne polecenie.")

    elif user_choice_main_menu == "zarządzaj" or user_choice_main_menu == "2":
        while True:
            user_choice_display_menu = input("Wybierz opcję, którą chcesz wyświetlić:\n"
                                             "1 - klasa\n"
                                             "2 - uczeń\n"
                                             "3 - nauczyciel\n"
                                             "4 - wychowawca\n"
                                             "5 - koniec\n")

            if user_choice_display_menu == "klasa" or user_choice_display_menu == "1":
                string_classes = str(list_of_school_classes).replace("'", "")
                print(f"Lista klas do wyboru: {string_classes}")
                display_school_class_from_user = input("Podaj klasę, której dane chcesz wyświetlić: ")
                number_of_students_the_class = 0
                for student in students_objects:
                    if display_school_class_from_user == student.school_class:
                        number_of_students_the_class += 1
                        print(f"{number_of_students_the_class}. {student.first_name} {student.last_name}")
                if number_of_students_the_class == 0:
                    print("Nie ma żadnych uczniów w tej klasie w danym spisie.")

                is_tutor_class = False
                tutor_class_first_name = None
                tutor_class_last_name = None
                for teacher in teachers_objects:
                    if display_school_class_from_user == teacher.class_tutor_of:
                        is_tutor_class = True
                        tutor_class_first_name = teacher.first_name
                        tutor_class_last_name = teacher.last_name

                if is_tutor_class:
                    print(f"\nWychowawcą danej klasy jest {tutor_class_first_name} {tutor_class_last_name}.\n")
                else:
                    print(f"\nNie ma wychowawcy dla klasy {display_school_class_from_user} w danym spisie!\n")

            elif user_choice_display_menu == "uczeń" or user_choice_display_menu == "2":
                help_numbers_students = []
                print("Lista uczniów: ")
                for index, student in enumerate(students_objects, start=1):
                    print(f"{index}. {student.first_name} {student.last_name}")
                    help_numbers_students.append(index)
                display_student_from_user = input("Wybierz numer ucznia, którego dane chcesz wyświetlić: ")
                display_student_from_user = int(display_student_from_user)
                for index, teacher in enumerate(teachers_objects):
                    if students_objects[display_student_from_user - 1].school_class in teacher.school_classes:
                        print(f"{index + 1}. {str(teacher.school_subject).capitalize()} z {teacher.first_name} "
                              f"{teacher.last_name}")
                    else:
                        print("Nie ma zajęć danego ucznia w spisie.")

            elif user_choice_display_menu == "nauczyciel" or user_choice_display_menu == "3":
                help_numbers_teachers = []
                print("Lista nauczycieli: ")
                for index, teacher in enumerate(teachers_objects, start=1):
                    print(f"{index}. {teacher.first_name} {teacher.last_name}")
                    help_numbers_teachers.append(index)
                display_teacher_from_user = input("Wybierz numer nauczyciela, którego dane chcesz wyświetlić: ")
                display_teacher_from_user = int(display_teacher_from_user)
                if teachers_objects[display_teacher_from_user - 1].school_classes:
                    print(f"Lista klas nauczyciela: {teachers_objects[display_teacher_from_user - 1].school_classes}")
                else:
                    print(f"Nie ma klas danego nauczyciela w spisie.")

            elif user_choice_display_menu == "wychowawca" or user_choice_display_menu == "4":
                help_numbers_tutors = []
                print("Lista wychowawców: ")
                for index, teacher in enumerate(teachers_objects, start=1):
                    if teacher.class_tutor_of:
                        print(f"{index}. {teacher.first_name} {teacher.last_name}")
                        help_numbers_tutors.append(index)

                if help_numbers_tutors:
                    display_tutor_from_user = input("Wybierz numer wychowawcy, którego dane chcesz wyświetlić: ")
                    display_tutor_from_user = int(display_tutor_from_user)
                    students_of_tutor = 0
                    for student in students_objects:
                        if student.school_class in teachers_objects[display_tutor_from_user - 1].school_classes:
                            print(f"{students_of_tutor + 1}. {student.first_name} {student.last_name}")
                            students_of_tutor += 1
                    if students_of_tutor == 0:
                        print("Nie ma ucznia w danym spisie, którego prowadzi podany wychowawca.")
                else:
                    print(f"Nie ma wychowawcy w danym spisie.")

            elif user_choice_display_menu == "koniec" or user_choice_display_menu == "5":
                break

            else:
                print("Niepoprawne polecenie.")

    elif user_choice_main_menu == "koniec" or user_choice_main_menu == "3":
        break

    else:
        print("Niepoprawne polecenie.")
