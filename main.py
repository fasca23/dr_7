text = ' Домашнее задание к лекции 7 '
print(text.center(50, "%"))
text = ' Задание 1-4 '
print(text.center(50))
from pprint import pprint
###################################
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Студент\n Имя = {self.name}\n Фамилия = {self.surname}\n Средняя оценка за лекции: = {self.average():0.1f}\n Курсы в процессе изучения: {self.p_courses()}\n Завершенные курсы: {self.f_courses()}'

        return res

    def p_courses(self):
        courses_progress = ", ".join(self.courses_in_progress)
        return courses_progress

    def f_courses(self):
        courses_finished = ", ".join(self.finished_courses)
        return courses_finished

    def average (self):
        t = []
        f = []
        for k, v in self.grades.items():
            t.append(v)
        for i in t:
            f.extend(i)
        sr = sum(f)/len(f) 
        return sr
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Это сравнивать нельзя!\n'
        lt = self.average() < other.average()
        if lt == True:
            lt_res = f'У {self.name} {self.surname} меньше средняя оценка чем у {other.name} {other.surname}\n'
        else: lt_res = f'У {self.name} {self.surname} больше средняя оценка чем у {other.name} {other.surname}\n'
        return lt_res
    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Это сравнивать нельзя!\n'
        eq = self.average() == other.average()
        if eq == True:
            eq_res = f'У {self.name} {self.surname} средняя оценка равна средней оценке {other.name} {other.surname}\n'
        else: eq_res = f'У {self.name} {self.surname} средняя оценка НЕ равна средней оценке {other.name} {other.surname}\n'
        return eq_res
###################################    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
###################################   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
    def __str__(self):
        res = f' Лектор\n Имя = {self.name}\n Фамилия = {self.surname}\n Средняя оценка за лекции: = {self.average():0.1f}'
        return res
    
    def average (self):
        t = []
        f = []
        for k, v in self.grades.items():
            t.append(v)
        for i in t:
            f.extend(i)
        sr = sum(f)/len(f) 
        return sr

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это сравнивать нельзя!\n'
        lt = self.average() < other.average()
        if lt == True:
            lt_res = f'У {self.name} {self.surname} меньше средняя оценка чем у {other.name} {other.surname}\n'
        else: lt_res = f'У {self.name} {self.surname} больше средняя оценка чем у {other.name} {other.surname}\n'
        return lt_res
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это сравнивать нельзя!\n'
        eq = self.average() == other.average()
        if eq == True:
            eq_res = f'У {self.name} {self.surname} средняя оценка равна средней оценке {other.name} {other.surname}\n'
        else: eq_res = f'У {self.name} {self.surname} средняя оценка НЕ равна средней оценке {other.name} {other.surname}\n'
        return eq_res
###################################
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f' Проверяющий\n Имя = {self.name}\n Фамилия = {self.surname}'
        return res
###################################
# Новые объекты класса Student 
student_1 = Student('Владимир', 'Каменев', 'муж.')
student_2 = Student('Иван', 'Пупкин', 'муж.')

student_1.courses_in_progress += ['Английский для программистов','Основы языка Python','Git-система контроля версий']
student_1.finished_courses += ['Английский для программистов']
student_2.courses_in_progress += ['Английский для программистов','Основы языка Python']

# Новые объекты класса Lecturer
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_2 = Lecturer('Алёна', 'Батицкая')
lecturer_3 = Lecturer('Виктор', 'Иванов')

lecturer_1.courses_attached += ['Основы языка Python']
lecturer_1.courses_attached += ['Git-система контроля версий']
lecturer_2.courses_attached += ['Git-система контроля версий']
lecturer_3.courses_attached += ['Английский для программистов']
lecturer_3.courses_attached += ['Git-система контроля версий']

student_1.rate_hw(lecturer_1, 'Основы языка Python', 10)
student_1.rate_hw(lecturer_1, 'Основы языка Python', 10)
student_2.rate_hw(lecturer_1, 'Основы языка Python', 10)
student_1.rate_hw(lecturer_3, 'Английский для программистов', 10)
student_1.rate_hw(lecturer_2, 'Git-система контроля версий', 10)
student_1.rate_hw(lecturer_3, 'Git-система контроля версий', 8)
student_1.rate_hw(lecturer_1, 'Git-система контроля версий', 9)

# Новые объекты класса Reviewer
super_reviewer = Reviewer('Man', 'Super')
super_reviewer.courses_attached += ['Основы языка Python']
super_reviewer.courses_attached += ['Git-система контроля версий']
super_reviewer.courses_attached += ['Английский для программистов']
 
super_reviewer.rate_hw(student_1, 'Основы языка Python', 9)
super_reviewer.rate_hw(student_1, 'Основы языка Python', 4)
super_reviewer.rate_hw(student_2, 'Основы языка Python', 8)
super_reviewer.rate_hw(student_1, 'Git-система контроля версий', 7)
super_reviewer.rate_hw(student_2, 'Git-система контроля версий', 6)
super_reviewer.rate_hw(student_1, 'Английский для программистов', 4)
super_reviewer.rate_hw(student_2, 'Английский для программистов', 5)

#Списки лекторов и студентов
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def average_students (student, courses):
    s=0
    for i in student:
        if isinstance(i, Student) and courses in i.grades:
            s += sum(i.grades[courses])/len(i.grades[courses])
        else: 
            print('Ошибка при вводе данных')
    so = s/len(student)
    print(f'Средняя оценка студентов курса {courses}: {so:0.1f}')

def average_lecturer (lecturer, courses):
    s=0
    for i in lecturer:
        if isinstance(i, Lecturer) and courses in i.grades:
            s += sum(i.grades[courses])/len(i.grades[courses])
        else: 
            print('Ошибка при вводе данных')
    so = s/len(lecturer)
    print(f'Средняя оценка лекторов курса {courses}: {so:0.1f}')

#Итог
print(super_reviewer)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(lecturer_3)
print()
print(student_1)
print()
print(student_2)
print()
print(student_2 < student_1)
print()
print(student_2 > student_1)
print(student_2 < student_1)
print(student_2 == student_1)
print()
print(lecturer_2 > lecturer_1)
print(student_2 < lecturer_1)
print(lecturer_2 > lecturer_3)
print(lecturer_2 == lecturer_3)
print()
average_students(student_list, 'Основы языка Python')
print()
average_lecturer(lecturer_list, 'Git-система контроля версий')
print()
print()