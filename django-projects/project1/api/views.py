from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from student.models import Student



class StudentViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer


# Create your views here.
