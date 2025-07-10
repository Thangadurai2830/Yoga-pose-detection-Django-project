from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
import base64
import json
import os
from django.core.files.storage import default_storage

# ✅ Home page
def index(request):
    return render(request, 'index.html')


# ✅ Upload and detect pose from file upload
def upload_pose(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('poseImage')
        if uploaded_file:
            # Save the uploaded image
            file_path = default_storage.save(f"uploads/{uploaded_file.name}", uploaded_file)
            image_url = default_storage.url(file_path)

            # Placeholder AI result (replace with real model later)
            predicted_pose = "Tree Pose"
            feedback = "Great balance! Try to keep your spine straight."

            return render(request, 'result.html', {
                'pose_name': predicted_pose,
                'pose_feedback': feedback,
                'pose_image_url': image_url
            })
        else:
            return render(request, 'pose_detection.html', {'error': 'No file uploaded.'})
    
    return render(request, 'pose_detection.html')


# ✅ Handle camera-based image (base64 image from JS)
@csrf_exempt
def analyze_pose(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            image_data = data['image'].split(',')[1]  # Remove base64 header
            image = Image.open(BytesIO(base64.b64decode(image_data)))

            # 🧠 ML prediction logic placeholder
            predicted_pose = "Warrior Pose"

            return JsonResponse({"success": True, "pose": predicted_pose})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({"success": False, "error": "Invalid request"})


# ✅ Optional direct result view (not used by upload currently)
def result(request):
    return render(request, 'result.html')
