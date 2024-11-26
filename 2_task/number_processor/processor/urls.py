from django.urls import path
from .views import NumberProcessorView

urlpatterns = [
    path('process-number/', NumberProcessorView.as_view(), name='process-number'),
]
