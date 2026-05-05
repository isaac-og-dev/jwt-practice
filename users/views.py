from .models import User, Teacher
from .serializers import UsersSerializer, TeacherSerializer
from rest_framework import viewsets

class UsersViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for the User model, providing CRUD operations.
    list - GET /users/ - List all users
    create - POST /users/ - Create a new user
    retrieve - GET /users/{id}/ - Retrieve a specific user by ID
    update - PUT /users/{id}/ - Update a specific user by ID
    partial_update - PATCH /users/{id}/ - Partially update a specific user by ID
    destroy - DELETE /users/{id}/ - Delete a specific user by ID
    '''
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    

class TeacherViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for the Teacher model, providing CRUD operations.
    list - GET /teachers/ - List all teachers
    create - POST /teachers/ - Create a new teacher
    retrieve - GET /teachers/{id}/ - Retrieve a specific teacher by ID
    update - PUT /teachers/{id}/ - Update a specific teacher by ID
    partial_update - PATCH /teachers/{id}/ - Partially update a specific teacher by ID
    destroy - DELETE /teachers/{id}/ - Delete a specific teacher by ID
    '''
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
