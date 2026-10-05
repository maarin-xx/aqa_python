
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
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
    DATABASE_URL = "sqlite:///students.db"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def create_5_courses():
    # Створюємо об'єкт сесії
    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання нового курсу
    i = 1
    courses = ["Math", "English", "History", "Science", "Art"]
    for course_name in courses:
        course = Course(id = i, name=course, number_of_hours = random.randint(1, 100))
        session.add(course)
        i = i + 1
    session.commit()
    # Відповідає INSERT INTO users (name, age) VALUES ('John', 30);

def create_20_students():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Додавання нового курсу
    i = 1
    while i <= 20:
        student = Student(id = i, name = fake.name(), date_of_birth = fake.date_of_birth(), start_year_of_study = random.randint(2021, 2026))
        session.add(student)
        i = i + 1
    session.commit()


create_model() #створення бази
create_5_courses()
create_20_students()



