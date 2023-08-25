# students_objects = []
# teachers_objects = []

print("\n*** Witaj w programie do obsługi bazy szkolnej! ***")


class Student:
    def __init__(self, first_name, last_name, school_class):
        print(f"Utworzono profil ucznia! {first_name} {last_name} z klasy {school_class}.")
        self.first_name = first_name
        self.last_name = last_name
        self.school_class = school_class


class Teacher:
    def __init__(self, first_name, last_name, school_subject, school_classes, is_class_tutor=False,
                 which_class_tutor=None):
        print(f"Utworzono profil nauczyciela! {first_name} {last_name} uczy przedmiotu {school_subject}.")
        print(f"Lista klas nauczyciela to: {school_classes}")
        self.first_name = first_name
        self.last_name = last_name
        self.school_subject = school_subject
        self.school_classes = school_classes
        self.is_class_tutor = is_class_tutor
        self.which_class_tutor = which_class_tutor


students_objects = []
teachers_objects = [Teacher("Paweł", "Kozioł", "biologia", ["1B", "2B", "3B"]), Teacher("Benek", "Ben", "geografia",
                                                                                        ["3B", "4B"])]


while True:
    user_choice_main_menu = input("Wpisz jedną z poniższych opcji:\n"
                                  "1. utwórz\n"
                                  "2. zarządzaj\n"
                                  "3. koniec\n")

    if user_choice_main_menu == "utwórz":
        while True:
            user_choice_create_menu = input("Wybierz typ profilu, który chcesz utworzyć:\n"
                                            "1. uczeń\n"
                                            "2. nauczyciel\n"
                                            "3. wychowawca\n"
                                            "4. koniec\n")

            if user_choice_create_menu == "uczeń":
                print("** Dodawanie profilu ucznia **")
                first_name_from_user = input("Podaj imię: ")
                last_name_from_user = input("Podaj nazwisko: ")
                school_class_from_user = input("Podaj klasę: ")

                students_objects.append(Student(first_name_from_user, last_name_from_user, school_class_from_user))
                number_of_students = len(students_objects)
                print(f"Łączna liczba uczniów to {number_of_students}.")

            elif user_choice_create_menu == "nauczyciel":
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
                number_of_teachers = len(teachers_objects)
                print(f"Łączna liczba nauczycieli to {number_of_teachers}.")
                # print(f"Nauczyciele: {teachers_objects[0].first_name}")

            elif user_choice_create_menu == "wychowawca":
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
                teachers_objects[class_tutor_from_user - 1].is_class_tutor = True

                print("Lista klas: ")
                print(teachers_objects[class_tutor_from_user - 1].school_classes)
                which_tutor_class_from_user = input(f"Wpisz klasę, której wychowawcą będzie "
                                                    f"{teachers_objects[class_tutor_from_user - 1].first_name} "
                                                    f"{teachers_objects[class_tutor_from_user - 1].last_name}: ")
                if which_tutor_class_from_user not in teachers_objects[class_tutor_from_user - 1].school_classes:
                    print("Należy wybrać klasę, którą uczy nauczyciel.")
                    teachers_objects[class_tutor_from_user - 1].is_class_tutor = False
                    continue
                for teachers in teachers_objects:
                    if which_tutor_class_from_user == teachers.which_class_tutor:
                        print("Wybrana klasa ma już wychowawcę.")
                        break

                teachers_objects[class_tutor_from_user - 1].which_class_tutor = which_tutor_class_from_user

                print(f"Nauczycielowi {teachers_objects[class_tutor_from_user - 1].first_name} "
                      f"{teachers_objects[class_tutor_from_user - 1].last_name} nadano status wychowawcy klasy "
                      f"{which_tutor_class_from_user}.")
