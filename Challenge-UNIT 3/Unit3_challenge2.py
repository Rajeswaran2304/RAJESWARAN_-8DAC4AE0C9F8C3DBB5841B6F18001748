def sort_students(students):

  sorted_students = sorted(students, key=lambda student: student.cgpa, reverse=True)

  return sorted_students


class Student:
  def __init__(self, name: str, roll_number: str, cgpa: float):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


students = [
        Student("SUDHAR", "9876543210", 9.0),
        Student("PREM", "1234567890", 9.5),
        Student("RAJESH", "0987654321", 8.5),
        Student("SANTHOSH", "0987654321", 9.9),
        Student("PRAKASH", "0987654321", 8.9),
        Student("AKASH", "0987654321", 7.5),
        Student("PRASANTH", "0987654321", 6.5)

        ]


sorted_students = sort_students(students)
for student in sorted_students:
  print(f"NAME : {student.name}  , ROLL NUM : ({student.roll_number})    ,CGPA : {student.cgpa}")


