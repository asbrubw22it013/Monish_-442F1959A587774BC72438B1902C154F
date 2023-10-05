class Student:  
    def __init__(self, name, roll_number, cgpa): 
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa 

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: (student.cgpa, student.name), reverse=True)
    return sorted_students

students = [ 
    Student("monish", "2222k0150", 9.8),
    Student("ashok", "2222k0142", 9.7),
    Student("kavinath", "2222k0156", 8.0),
    Student("ram", "2222k0152", 9.0)  
]
sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll_number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))

