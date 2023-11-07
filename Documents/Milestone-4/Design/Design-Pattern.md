# Reusable Design Patterns

## Data Models

Each data model should look something like this:

```python
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    github = models.URLField(max_length=200, blank=True, null=True)
    server = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.user.username
```

## General Purpose Views

Each data model should have a List, Detail, Create, Update, and Delete view.

They could look something like this:

__List View__ (Display a list of all students):
    - URL: `/students/`
    - View Function: `student_list`
    - Template: `student_list.html`

```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
```

__Detail View__ (Display details of a single student):
    - URL: `/students/<student_id>/`
    - View Function: `student_detail`
    - Template: `student_detail.html`

```python
from django.shortcuts import render, get_object_or_404
from .models import Student

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})
```

__Create View__ (Create a new student):
    - URL: `/students/create/`
    - View Function: `student_create`
    - Template: `student_form.html`

```python
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
```

__Update View__ (Edit an existing student's information):
    - URL: `/students/<student_id>/update/`
    - View Function: `student_update`
    - Template: `student_form.html`

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})
```

__Delete View__ (Delete a student):
    - URL: `/students/<student_id>/delete/`
    - View Function: `student_delete`
    - Template: Not applicable

```python
from django.shortcuts import redirect, get_object_or_404
from .models import Student

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')
```

## URLs and Templates
