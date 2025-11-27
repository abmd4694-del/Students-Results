from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    """Student model to store student information"""
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    enrollment_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    
    class Meta:
        ordering = ['student_id']
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def calculate_gpa(self):
        """Calculate overall GPA for the student"""
        results = self.result_set.all()
        if not results:
            return 0.0
        
        total_points = sum([r.get_grade_point() for r in results])
        return round(total_points / len(results), 2)


class Course(models.Model):
    """Course model to store course information"""
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.IntegerField(default=3)
    semester = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['course_code']
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Teacher(models.Model):
    """Teacher model linked to Django User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='teachers')
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"


class Result(models.Model):
    """Result model to store student exam results"""
    GRADE_CHOICES = [
        ('A+', 'A+ (90-100)'),
        ('A', 'A (85-89)'),
        ('A-', 'A- (80-84)'),
        ('B+', 'B+ (75-79)'),
        ('B', 'B (70-74)'),
        ('B-', 'B- (65-69)'),
        ('C+', 'C+ (60-64)'),
        ('C', 'C (55-59)'),
        ('D', 'D (50-54)'),
        ('F', 'F (0-49)'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    exam_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-exam_date']
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student.student_id} - {self.course.course_code} - {self.grade}"
    
    def save(self, *args, **kwargs):
        """Auto-calculate grade based on marks"""
        if self.marks >= 90:
            self.grade = 'A+'
        elif self.marks >= 85:
            self.grade = 'A'
        elif self.marks >= 80:
            self.grade = 'A-'
        elif self.marks >= 75:
            self.grade = 'B+'
        elif self.marks >= 70:
            self.grade = 'B'
        elif self.marks >= 65:
            self.grade = 'B-'
        elif self.marks >= 60:
            self.grade = 'C+'
        elif self.marks >= 55:
            self.grade = 'C'
        elif self.marks >= 50:
            self.grade = 'D'
        else:
            self.grade = 'F'
        
        super().save(*args, **kwargs)
    
    def get_grade_point(self):
        """Return grade point for GPA calculation"""
        grade_points = {
            'A+': 4.0, 'A': 3.7, 'A-': 3.3,
            'B+': 3.0, 'B': 2.7, 'B-': 2.3,
            'C+': 2.0, 'C': 1.7, 'D': 1.0, 'F': 0.0
        }
        return grade_points.get(self.grade, 0.0)
