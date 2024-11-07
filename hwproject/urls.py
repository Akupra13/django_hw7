from django.contrib import admin
from django.urls import path, include
from hw7_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Корневая страница
    path('hw7_app/', include('hw7_app.urls')),  # маршруты из приложения hw7_app
]
