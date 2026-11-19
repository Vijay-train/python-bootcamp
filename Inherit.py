class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("my name is",self.name)
        print("my age is",self.age)
     
class Student(Person):
    def __init__(self,name,age,marks,subject):
        super().__init__(name,age)
        self.marks = marks
        self.subject = subject

    def PrintMarks(self):
        print("Subject is : ",self.subject)
        print("Marks = ",self.marks)

    def intro(self):
        super().intro()
        print(f"for {self.subject} i got {self.marks}")

    
s1 = Student("Neetu", 17,95,"Python")
s1.intro()

p1 = Person("vijay",25)
p1.intro()

