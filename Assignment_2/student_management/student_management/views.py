from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm

# Student List View
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    else:
        students = Student.objects.all()
    
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    students_page = paginator.get_page(page_number)

    return render(request, 'student_management_app/student_list.html', {'students': students_page})

# Student Detail View
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_management_app/student_detail.html', {'student': student})

# Add Student View
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_management_app/add_student.html', {'form': form})

# Edit Student View
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_management_app/edit_student.html', {'form': form, 'student': student})
