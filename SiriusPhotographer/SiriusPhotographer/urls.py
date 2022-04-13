
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('personalArea', include("personalArea.urls"))

#     потом закоментить
#     path('', include("main.urls"))



]