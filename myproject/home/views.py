from django.shortcuts import render

from .data import students, teachers

# Create your views here.
def index(request):
    return render(request,'index.html')
def edit(request):
    student={

        "name":"adeeb"
        ,"age":22,
        "mark":[89,99,78],
    }
    return render(request,'edit.html',student)
def add(request):
    return render(request,'add.html')
def show(request):
    return render(request,'show.html')


def table(request):
    show = request.GET.get('show', 'students')  # القيمة الافتراضية: طلاب
    if show == 'teachers':
        context = {"records": teachers, "title": "بيانات المعلمين", "type": "teachers"}
    else:
        context = {"records": students, "title": "بيانات الطلاب", "type": "students"}
    return render(request, 'table.html', context)
