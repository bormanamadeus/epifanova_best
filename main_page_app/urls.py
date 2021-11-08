from django.urls import path
from main_page_app.views import index


urlpatterns = [
    path('<int:theme_id>/', index, name='ph_theme'),
    path('', index, name='ph_main'),
]
