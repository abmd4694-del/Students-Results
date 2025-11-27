from django.contrib import admin
from .models import Student, Course, Teacher, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'phone', 'enrollment_date']
    list_filter = ['enrollment_date']
    search_fields = ['student_id', 'first_name', 'last_name', 'email']
    date_hierarchy = 'enrollment_date'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'credits', 'semester']
    list_filter = ['semester', 'credits']
    search_fields = ['course_code', 'course_name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'user', 'phone', 'department']
    list_filter = ['department']
    search_fields = ['employee_id', 'user__username', 'user__first_name', 'user__last_name']
    filter_horizontal = ['courses']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'marks', 'grade', 'exam_date', 'created_by']
    list_filter = ['grade', 'exam_date', 'course']
    search_fields = ['student__student_id', 'student__first_name', 'student__last_name', 'course__course_code']
    date_hierarchy = 'exam_date'
    readonly_fields = ['created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set created_by on creation
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
