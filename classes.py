class Student:
    def __init__(self, first_name, last_name, school_class):
        print(f"Utworzono profil ucznia! {first_name} {last_name} z klasy {school_class}.")
        self.first_name = first_name
        self.last_name = last_name
        self.school_class = school_class


class Teacher:
    def __init__(self, first_name, last_name, school_subject, school_classes, class_tutor_of=None):
        print(f"Utworzono profil nauczyciela! {first_name} {last_name} uczy przedmiotu {school_subject}.")
        print(f"Lista klas nauczyciela to: {school_classes}")
        self.first_name = first_name
        self.last_name = last_name
        self.school_subject = school_subject
        self.school_classes = school_classes
        self.class_tutor_of = class_tutor_of
