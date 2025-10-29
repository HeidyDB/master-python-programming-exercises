### DON'T modify this code ###
#herencia y polimorfismo

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        return f"{self.name} is studying for {hours} hours."
    

        
### DON'T modify the code above ###
        
### ↓ Your code here ↓ ###
class HighSchoolStudent(Student):  # Add the parent class inside the parenthesis
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)
        self.specialization = specialization

    def study(self, hours):
        return f"{self.name} is a high school student specializing in {self.specialization} and is studying for {hours} hours for exams."
class CollegeStudent(Student): # hereda de Student
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)
        self.major = major
    def introduce(self):
        return f"Hi there Iam {self.name}, a college student majoring in {self.major} "

    def study(self, hours):
        return f"{self.name} is a college student majoring in {self.major} and is studying for {hours} hours for exams."
    
    def attend_lecture(self, topic):
        return f"{self.name} is attending a lecture on {topic}."



# Creating an instance of HighSchoolStudent
high_school_student = HighSchoolStudent("John", 16, 85, "Science")
print(high_school_student.introduce())  # We can call this method thanks to inheritance 
print(high_school_student.study(4))

collage_student = CollegeStudent("Ana", 20, 90, "Computer Science")
print(collage_student.introduce())  # We can call this method thanks to inheritance
print(collage_student.study(5))
print(collage_student.attend_lecture("Data Structures"))