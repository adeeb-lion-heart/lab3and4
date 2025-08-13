# from django.contrib import admin
# from django.urls import path,include
from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('edit',views.edit,name="edit"),
    path('add',views.add,name="add"),
    path('show',views.show,name="show"),
    path('table',views.table,name="table"),
    

]
