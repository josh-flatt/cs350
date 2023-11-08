# Reusable Design Patterns

To create a design pattern for Django data models, general-purpose views, URLs, and templates for the example "Student" data model, you can follow the MVC (Model-View-Controller) pattern that Django is built upon. Here's how you can design this pattern:

## Data Models

```python
# models.py
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming there's a User model for authentication.
    course = models.CharField(max_length=100)
    github = models.URLField(blank=True, null=True)
    server = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
```

## General Purpose Views

Here are Django views for the general-purpose operations on the "Student" data model: List, Detail, Create, Update, and Delete.

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm  # You would need to create a form for the 'Student' model.

# List View
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Detail View
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

# Create View
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Update View
def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete View
def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
```

## URLs and Templates

### URLs

Define URL patterns that map to the views you created.

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:student_id>/update/', views.student_update, name='student_update'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
]
```

### Templates

Here's an example of a Django template for the "student_list" view. This template will render a list of students:

```html
<!-- student_list.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>Student List</h2>
  <table class="table">
    <thead>
      <tr>
        <th>Username</th>
        <th>Course</th>
        <th>Email</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {% for student in students %}
        <tr>
          <td>{{ student.user.username }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.email }}</td>
          <td>
            <a href="{% url 'student_detail' student.id %}">Detail</a> |
            <a href="{% url 'student_update' student.id %}">Edit</a> |
            <a href="{% url 'student_delete' student.id %}">Delete</a>
          </td>
        </tr>
      {% empty %}
        <tr>
          <td colspan="4">No students found.</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
  <a href="{% url 'student_create' %}" class="btn btn-primary">Create Student</a>
{% endblock %}
```

In this template:

- We extend a base template using `{% extends 'base.html' %}` to provide a consistent layout.
- Inside the `content` block, we display the title and create an HTML table to show the list of students.
- We use a for loop `{% for student in students %}` to iterate through the list of students and display their information in the table rows.
- For each student, we display their username, course, email, and provide links to the "Detail," "Edit," and "Delete" actions, which are linked to the appropriate views.
- If there are no students in the list, we display a message stating "No students found."
- Finally, we include a link to the "Create Student" view using a button with a link.

You would create similar templates for the other views (e.g., `student_detail.html`, `student_form.html`, and `student_confirm_delete.html`) based on the requirements and desired layout of your application.

Create templates for rendering the views. You should have templates named 'student_list.html,' 'student_detail.html,' 'student_form.html,' and 'student_confirm_delete.html' for each corresponding view.

By following this design pattern, you can create a Django application that handles CRUD operations on the "Student" data model, providing a clear structure for data models, views, URLs, and templates.
