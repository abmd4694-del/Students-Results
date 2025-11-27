from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Avg, Count
from .models import Student, Course, Teacher, Result
from .forms import StudentForm, CourseForm, ResultForm


def home(request):
    """Home page view"""
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_results': Result.objects.count(),
    }
    return render(request, 'results/home.html', context)


def login_view(request):
    """Login view for teachers/admins"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'results/login.html')


@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def dashboard(request):
    """Dashboard view for logged-in users"""
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_results': Result.objects.count(),
        'recent_results': Result.objects.select_related('student', 'course').order_by('-created_at')[:10],
    }
    return render(request, 'results/dashboard.html', context)


def student_list(request):
    """List all students with search functionality"""
    search_query = request.GET.get('search', '')
    students = Student.objects.all()
    
    if search_query:
        students = students.filter(
            Q(student_id__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    context = {
        'students': students,
        'search_query': search_query,
    }
    return render(request, 'results/student_list.html', context)


def student_detail(request, student_id):
    """View student details and their results"""
    student = get_object_or_404(Student, student_id=student_id)
    results = Result.objects.filter(student=student).select_related('course')
    gpa = student.calculate_gpa()
    
    context = {
        'student': student,
        'results': results,
        'gpa': gpa,
    }
    return render(request, 'results/student_detail.html', context)


@login_required
def student_create(request):
    """Create a new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.get_full_name()} created successfully!')
            return redirect('student_detail', student_id=student.student_id)
    else:
        form = StudentForm()
    
    return render(request, 'results/student_form.html', {'form': form, 'action': 'Create'})


@login_required
def student_edit(request, student_id):
    """Edit an existing student"""
    student = get_object_or_404(Student, student_id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.get_full_name()} updated successfully!')
            return redirect('student_detail', student_id=student.student_id)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'results/student_form.html', {'form': form, 'action': 'Edit', 'student': student})


@login_required
def student_delete(request, student_id):
    """Delete a student"""
    student = get_object_or_404(Student, student_id=student_id)
    
    if request.method == 'POST':
        student_name = student.get_full_name()
        student.delete()
        messages.success(request, f'Student {student_name} deleted successfully!')
        return redirect('student_list')
    
    return render(request, 'results/student_confirm_delete.html', {'student': student})


def course_list(request):
    """List all courses"""
    courses = Course.objects.all()
    return render(request, 'results/course_list.html', {'courses': courses})


@login_required
def course_create(request):
    """Create a new course"""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, f'Course {course.course_name} created successfully!')
            return redirect('course_list')
    else:
        form = CourseForm()
    
    return render(request, 'results/course_form.html', {'form': form, 'action': 'Create'})


@login_required
def result_create(request):
    """Create a new result entry"""
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.created_by = request.user
            result.save()
            messages.success(request, f'Result for {result.student.get_full_name()} in {result.course.course_name} created successfully!')
            return redirect('student_detail', student_id=result.student.student_id)
    else:
        form = ResultForm()
    
    return render(request, 'results/result_form.html', {'form': form})


@login_required
def result_edit(request, result_id):
    """Edit an existing result"""
    result = get_object_or_404(Result, id=result_id)
    
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            result = form.save()
            messages.success(request, f'Result updated successfully!')
            return redirect('student_detail', student_id=result.student.student_id)
    else:
        form = ResultForm(instance=result)
    
    return render(request, 'results/result_form.html', {'form': form, 'result': result})


@login_required
def result_delete(request, result_id):
    """Delete a result"""
    result = get_object_or_404(Result, id=result_id)
    student_id = result.student.student_id
    
    if request.method == 'POST':
        result.delete()
        messages.success(request, 'Result deleted successfully!')
        return redirect('student_detail', student_id=student_id)
    
    return render(request, 'results/result_confirm_delete.html', {'result': result})


def search_results(request):
    """Search for student results"""
    search_query = request.GET.get('search', '')
    results = []
    
    if search_query:
        results = Result.objects.filter(
            Q(student__student_id__icontains=search_query) |
            Q(student__first_name__icontains=search_query) |
            Q(student__last_name__icontains=search_query) |
            Q(course__course_code__icontains=search_query) |
            Q(course__course_name__icontains=search_query)
        ).select_related('student', 'course')
    
    context = {
        'results': results,
        'search_query': search_query,
    }
    return render(request, 'results/search_results.html', context)
