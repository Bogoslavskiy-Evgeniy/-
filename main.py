class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __aver_grade(self):
        val_grade = self.grades.values()
        val = []
        for i in val_grade:
            val.extend(i)
            av_gr = round(sum(val)/len(val), 1)
        return av_gr
        
    def __str__(self):
        return f'Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за домашние задания: {Student.__aver_grade(self)}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}'
    
    def __lt__(self, other):
        if self.__aver_grade() < other.__aver_grade():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__aver_grade() > other.__aver_grade():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__aver_grade() == other.__aver_grade():
            return True
        else:
            return False
         
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __average_grade(self):
        value_grade = self.grades.values()
        value = []
        for i in value_grade:
            value.extend(i)
            aver_gr = round(sum(value)/len(value), 1)
        return aver_gr
        
    def __str__(self):
        return f'Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за лекции: {Lecturer.__average_grade(self)}' 
        
    def __lt__(self, other):
        if self.__average_grade() < other.__average_grade():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__average_grade() > other.__average_grade():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__average_grade() == other.__average_grade():
            return True
        else:
            return False        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

lecturer1 = Lecturer('Александр', 'Сидоров')
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Роман', 'Жуков')
lecturer2.courses_attached = ['Java', 'Git']

reviewer1 = Reviewer('Петр', 'Смолов')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Алексей', 'Попов')
reviewer2.courses_attached = ['Git', 'Java']

student1 = Student('Иван', 'Иванов', 'м')
student1.finished_courses = ['C++']
student1.courses_in_progress = ['Python', 'Java', 'Git']

student2 = Student('Мария', 'Петрова', 'ж')
student2.finished_courses = ['Kotlin']
student2.courses_in_progress = ['Java', 'Git', 'Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 6)

reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Git', 6)

student1.rate_lect(lecturer1, 'Python', 8)
student1.rate_lect(lecturer2, 'Java', 7)
student1.rate_lect(lecturer2, 'Git', 4)

student2.rate_lect(lecturer1, 'Python', 10)
student2.rate_lect(lecturer2, 'Java', 9)
student2.rate_lect(lecturer2, 'Git', 8)

list_students = [student1, student2]
list_lecturers = [lecturer1, lecturer2]
def average_rating_st(list_students, course):
    raiting = []
    for student in list_students:
        if course in student.grades.keys():
            raiting.append(student.grades[course])
    av_rait = []
    for i in raiting:
        av_rait.extend(i)
    aver_raiting = round(sum(av_rait)/len(av_rait), 1)
    return aver_raiting     

def average_rating_lect(list_lecturers, course):
    raiting_lect = []
    for lecturer in list_lecturers:
        if course in lecturer.grades.keys():
            raiting_lect.append(lecturer.grades[course])
    av_rait_lect = []
    for i in raiting_lect:
        av_rait_lect.extend(i)
    aver_raiting_lect = round(sum(av_rait_lect)/len(av_rait_lect), 1)
    return aver_raiting_lect 

print(average_rating_st(list_students, 'Git'))
print()
print(average_rating_lect(list_lecturers, 'Java'))
print()        
print (str(student1))
print()
print (str(student2))
print()
print (str(lecturer1))
print()
print (str(lecturer2))
print()
print (str(reviewer1))
print()
print (str(reviewer2))
print()
print(student1 < student2)
print()
print(student1 > student2)
print()
print(student1 == student2)
print()
print(lecturer1 < lecturer2)
print()
print(lecturer1 > lecturer2)
print()
print(lecturer1 == lecturer2)
print()