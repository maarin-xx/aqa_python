
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import random
from faker import Faker
fake = Faker()

# Базовий клас для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиці) за допомогою класу
class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    start_year_of_study = Column(Integer)

class Course(Base):

    __tablename__ = 'Course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_of_hours = Column(Integer)

class StudentCourse(Base):

    __tablename__ = 'StudentCourse'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("Student.id"))
    course_id = Column(Integer, ForeignKey("Course.id"))
    start_date = Column(DateTime)
    score = Column(Integer)

def create_model():
    Base.metadata.create_all(engine)

def create_5_courses():
    # Створюємо об'єкт сесії
    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання нового курсу
    courses = ["Math", "English", "History", "Science", "Art"]
    for course_name in courses:
        course = Course(name=course_name, number_of_hours = random.randint(1, 100))
        session.add(course)
    session.commit()
    # Відповідає INSERT INTO users (name, age) VALUES ('John', 30);

def create_20_students():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання нового курсу
    i = 1
    while i <= 20:
        student = Student(name = fake.name(), date_of_birth = fake.date_of_birth(), start_year_of_study = random.randint(2021, 2026))
        session.add(student)
        i = i + 1
    session.commit()

def assign_students_to_courses():
    Session = sessionmaker(bind=engine)
    session = Session()

    all_students= session.query(Student).all()
    # SQL аналог: SELECT * FROM Student;
    all_courses = session.query(Course).all()


    student_course = set()

    while len(student_course) < 20:
        student = random.choice(all_students)
        course = random.choice(all_courses)

        pair = (student.id, course.id)

        if pair not in student_course:
            student_course.add(pair)

            student_course_db = StudentCourse(
                student_id=student.id,
                course_id=course.id,
                start_date=fake.date_time(),
                score=random.randint(0, 100)
            )

            session.add(student_course_db)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()

"""Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
 Переконайтеся, що ці зміни коректно відображаються у базі даних."""

def insert_student(course_id):
    # Додавання нового student
    Session = sessionmaker(bind=engine)
    session = Session()

    new_student = Student(
        name=fake.name(),
        date_of_birth=fake.date_of_birth(),
        start_year_of_study=random.randint(2021, 2026)
    )

    session.add(new_student)
    session.commit()

    new_student_course = StudentCourse(
        student_id=new_student.id,
        course_id=course_id,
        start_date=fake.date_time(),
        score=random.randint(0, 100)
    )

    session.add(new_student_course)
    session.commit()

    session.close()

"""
Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, 
зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
"""

def all_students_on_courses(course_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    all_students = (
        session.query(Student)
        .join(StudentCourse)
        .filter(StudentCourse.course_id == course_id)
        .all()
    )

    session.close()
    return all_students

def courses_of_student(student_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(Student.name, Course.name)
        .join(StudentCourse, Student.id == StudentCourse.student_id)
        .join(Course, Course.id == StudentCourse.course_id)
        .filter(Student.id == student_id)
        .all()
    )

    session.close()
    return result

"""Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, 
а також видалення студентів з бази даних.
"""

def update_student(student_id, new_name):
    Session = sessionmaker(bind=engine)
    session = Session()

    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        student.name = new_name
        session.commit()

    session.close()

def delete_student(student_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(StudentCourse).filter(
        StudentCourse.student_id == student_id
    ).delete()

    session.query(Student).filter(
        Student.id == student_id
    ).delete()

    session.commit()
    session.close()


DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
create_model() #створення бази
create_5_courses()
create_20_students()
assign_students_to_courses()
insert_student(3)

students = all_students_on_courses(3)

print("All students on course_id = 3:")

for student in students:
    print(student.id, student.name)


courses = courses_of_student(1)

print("Courses of student_id = 1:")

for student_name, course_name in courses:
    print(student_name, "-", course_name)


update_student(1, "John Updated")


delete_student(1)







