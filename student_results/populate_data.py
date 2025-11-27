"""
Django Shell Script to Populate Sample Data
Run this with: python manage.py shell < populate_data.py
Or copy-paste into: python manage.py shell
"""

from django.contrib.auth.models import User
from results.models import Student, Course, Teacher, Result
from datetime import date, timedelta
import random

print("=" * 60)
print("Starting Data Population...")
print("=" * 60)

# Clear existing data (optional - comment out if you want to keep existing data)
print("\n1. Clearing existing data...")
Result.objects.all().delete()
Teacher.objects.all().delete()
Course.objects.all().delete()
Student.objects.all().delete()
User.objects.filter(is_superuser=False).delete()
print("✓ Existing data cleared")

# Create Courses
print("\n2. Creating Courses...")
courses_data = [
    {
        'course_code': 'CS101',
        'course_name': 'Introduction to Computer Science',
        'description': 'Fundamentals of programming and computer science concepts',
        'credits': 4,
        'semester': 'Fall 2024'
    },
    {
        'course_code': 'CS201',
        'course_name': 'Data Structures and Algorithms',
        'description': 'Advanced data structures, algorithms, and complexity analysis',
        'credits': 4,
        'semester': 'Fall 2024'
    },
    {
        'course_code': 'CS301',
        'course_name': 'Database Management Systems',
        'description': 'Relational databases, SQL, and database design principles',
        'credits': 3,
        'semester': 'Fall 2024'
    },
    {
        'course_code': 'CS302',
        'course_name': 'Web Development',
        'description': 'Full-stack web development with modern frameworks',
        'credits': 3,
        'semester': 'Fall 2024'
    },
    {
        'course_code': 'MATH201',
        'course_name': 'Discrete Mathematics',
        'description': 'Mathematical foundations for computer science',
        'credits': 3,
        'semester': 'Fall 2024'
    },
    {
        'course_code': 'CS401',
        'course_name': 'Artificial Intelligence',
        'description': 'Machine learning, neural networks, and AI applications',
        'credits': 4,
        'semester': 'Spring 2025'
    },
    {
        'course_code': 'CS402',
        'course_name': 'Software Engineering',
        'description': 'Software development lifecycle, testing, and project management',
        'credits': 3,
        'semester': 'Spring 2025'
    },
]

courses = []
for course_data in courses_data:
    course = Course.objects.create(**course_data)
    courses.append(course)
    print(f"  ✓ Created: {course.course_code} - {course.course_name}")

print(f"✓ Created {len(courses)} courses")

# Create Students
print("\n3. Creating Students...")
students_data = [
    {
        'student_id': 'STU001',
        'first_name': 'Emily',
        'last_name': 'Johnson',
        'email': 'emily.johnson@university.edu',
        'phone': '+1-555-0101',
        'date_of_birth': date(2002, 3, 15),
        'address': '123 Oak Street, Springfield, IL 62701'
    },
    {
        'student_id': 'STU002',
        'first_name': 'Michael',
        'last_name': 'Chen',
        'email': 'michael.chen@university.edu',
        'phone': '+1-555-0102',
        'date_of_birth': date(2001, 7, 22),
        'address': '456 Maple Avenue, Springfield, IL 62702'
    },
    {
        'student_id': 'STU003',
        'first_name': 'Sarah',
        'last_name': 'Williams',
        'email': 'sarah.williams@university.edu',
        'phone': '+1-555-0103',
        'date_of_birth': date(2002, 11, 8),
        'address': '789 Pine Road, Springfield, IL 62703'
    },
    {
        'student_id': 'STU004',
        'first_name': 'David',
        'last_name': 'Martinez',
        'email': 'david.martinez@university.edu',
        'phone': '+1-555-0104',
        'date_of_birth': date(2001, 5, 30),
        'address': '321 Elm Boulevard, Springfield, IL 62704'
    },
    {
        'student_id': 'STU005',
        'first_name': 'Jessica',
        'last_name': 'Anderson',
        'email': 'jessica.anderson@university.edu',
        'phone': '+1-555-0105',
        'date_of_birth': date(2002, 9, 17),
        'address': '654 Cedar Lane, Springfield, IL 62705'
    },
    {
        'student_id': 'STU006',
        'first_name': 'James',
        'last_name': 'Taylor',
        'email': 'james.taylor@university.edu',
        'phone': '+1-555-0106',
        'date_of_birth': date(2001, 12, 3),
        'address': '987 Birch Drive, Springfield, IL 62706'
    },
    {
        'student_id': 'STU007',
        'first_name': 'Olivia',
        'last_name': 'Brown',
        'email': 'olivia.brown@university.edu',
        'phone': '+1-555-0107',
        'date_of_birth': date(2002, 4, 25),
        'address': '147 Walnut Street, Springfield, IL 62707'
    },
    {
        'student_id': 'STU008',
        'first_name': 'Daniel',
        'last_name': 'Garcia',
        'email': 'daniel.garcia@university.edu',
        'phone': '+1-555-0108',
        'date_of_birth': date(2001, 8, 14),
        'address': '258 Spruce Avenue, Springfield, IL 62708'
    },
    {
        'student_id': 'STU009',
        'first_name': 'Soubin',
        'last_name': 'Wilson',
        'email': 'sw@university.edu',
        'phone': '8882223344',
        'date_of_birth': date(2002, 1, 19),
        'address': '369 Ash Road, Springfield, IL 62709'
    },
    {
        'student_id': 'STU010',
        'first_name': 'Aryan',
        'last_name': 'W',
        'email': 'AW@university.edu',
        'phone': '+12567349810',
        'date_of_birth': date(2001, 6, 28),
        'address': '741 Hickory Boulevard, Springfield, IL 62710'
    },
]

students = []
for student_data in students_data:
    student = Student.objects.create(**student_data)
    students.append(student)
    print(f"  ✓ Created: {student.student_id} - {student.get_full_name()}")

print(f"✓ Created {len(students)} students")

# Create Teacher Users and Teachers
print("\n4. Creating Teachers...")
teachers_data = [
    {
        'username': 'prof.smith',
        'email': 'robert.smith@university.edu',
        'first_name': 'Robert',
        'last_name': 'Smith',
        'employee_id': 'TEACH001',
        'phone': '+1-555-1001',
        'department': 'Computer Science',
        'course_codes': ['CS101', 'CS201']
    },
    {
        'username': 'prof.davis',
        'email': 'jennifer.davis@university.edu',
        'first_name': 'Jennifer',
        'last_name': 'Davis',
        'employee_id': 'TEACH002',
        'phone': '+1-555-1002',
        'department': 'Computer Science',
        'course_codes': ['CS301', 'CS302']
    },
    {
        'username': 'prof.thompson',
        'email': 'william.thompson@university.edu',
        'first_name': 'William',
        'last_name': 'Thompson',
        'employee_id': 'TEACH003',
        'phone': '+1-555-1003',
        'department': 'Mathematics',
        'course_codes': ['MATH201']
    },
    {
        'username': 'prof.rodriguez',
        'email': 'maria.rodriguez@university.edu',
        'first_name': 'Maria',
        'last_name': 'Rodriguez',
        'employee_id': 'TEACH004',
        'phone': '+1-555-1004',
        'department': 'Computer Science',
        'course_codes': ['CS401', 'CS402']
    },
]

teachers = []
for teacher_data in teachers_data:
    # Create Django User
    user = User.objects.create_user(
        username=teacher_data['username'],
        email=teacher_data['email'],
        password='teacher123',  # Default password
        first_name=teacher_data['first_name'],
        last_name=teacher_data['last_name']
    )
    
    # Create Teacher profile
    teacher = Teacher.objects.create(
        user=user,
        employee_id=teacher_data['employee_id'],
        phone=teacher_data['phone'],
        department=teacher_data['department']
    )
    
    # Assign courses
    for course_code in teacher_data['course_codes']:
        course = Course.objects.get(course_code=course_code)
        teacher.courses.add(course)
    
    teachers.append(teacher)
    print(f"  ✓ Created: {teacher.employee_id} - {user.get_full_name()} (username: {teacher_data['username']}, password: teacher123)")

print(f"✓ Created {len(teachers)} teachers")

# Create Results
print("\n5. Creating Results...")
exam_date_base = date(2024, 11, 1)

results_count = 0
for student in students:
    # Each student takes 4-6 random courses
    num_courses = random.randint(4, 6)
    student_courses = random.sample(courses, num_courses)
    
    for idx, course in enumerate(student_courses):
        # Generate realistic marks with some variation
        base_mark = random.randint(55, 95)
        marks = round(base_mark + random.uniform(-5, 5), 2)
        marks = max(0, min(100, marks))  # Ensure 0-100 range
        
        # Find a teacher who teaches this course
        teacher_for_course = Teacher.objects.filter(courses=course).first()
        created_by_user = teacher_for_course.user if teacher_for_course else teachers[0].user
        
        # Create result
        exam_date = exam_date_base + timedelta(days=idx * 7)
        
        result = Result.objects.create(
            student=student,
            course=course,
            marks=marks,
            exam_date=exam_date,
            created_by=created_by_user,
            remarks=f"Exam completed on {exam_date.strftime('%B %d, %Y')}"
        )
        results_count += 1
        print(f"  ✓ {student.student_id} - {course.course_code}: {marks:.2f} ({result.grade})")

print(f"✓ Created {results_count} results")

# Display Summary
print("\n" + "=" * 60)
print("DATA POPULATION COMPLETED!")
print("=" * 60)
print(f"\n📊 Summary:")
print(f"  • Courses Created: {Course.objects.count()}")
print(f"  • Students Created: {Student.objects.count()}")
print(f"  • Teachers Created: {Teacher.objects.count()}")
print(f"  • Results Created: {Result.objects.count()}")

print(f"\n👥 Teacher Login Credentials:")
print("  " + "-" * 50)
for teacher_data in teachers_data:
    print(f"  Username: {teacher_data['username']}")
    print(f"  Password: teacher123")
    print(f"  Name: {teacher_data['first_name']} {teacher_data['last_name']}")
    print(f"  Department: {teacher_data['department']}")
    print("  " + "-" * 50)

print(f"\n🎓 Sample Student GPAs:")
print("  " + "-" * 50)
for student in students[:5]:  # Show first 5 students
    gpa = student.calculate_gpa()
    print(f"  {student.student_id} - {student.get_full_name()}: GPA {gpa}")

print("\n✅ You can now login to the admin panel or application!")
print("   Visit: http://localhost:8000")
print("=" * 60)
