from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                     # ✅ Home page
    path('upload/', views.upload_pose, name='upload_pose'), # ✅ Upload image page
    path('analyze-pose/', views.analyze_pose, name='analyze_pose'), # ✅ Webcam capture API
    path('result/', views.result, name='result'),           # ✅ Optional direct result page
]
