class Student:

    # static variables declaration
    sumGrades = 0
    sumAge = 0
    countStudents = 0

    def __init__(self, grade, age):
        
        self.grade = grade
        self.age = age
        Student.sumGrades += grade
        Student.sumAge += age
        Student.countStudents += 1

    @classmethod
    def gradeAvg(class_level):
        print(Student.sumGrades / Student.countStudents)
    
    @classmethod
    def ageAvg(class_level):
        print(Student.sumAge / Student.countStudents)




s1 = Student(90, 15)
s2 = Student(80, 16)
s3 = Student(100, 14)
s4 = Student(70, 13)

Student.gradeAvg()
Student.ageAvg()