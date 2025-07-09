from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedImage
from .forms import UploadForm
from .utils import detect_ai_image

def home(request):
    return render(request, 'pixeltruth_app/home.html')

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image_path = image.image.path
            confidence = detect_ai_image(image_path)
            image.ai_confidence = confidence
            image.is_ai = confidence > 60  # or whatever threshold you want
            image.save()

            # redirect to results page or process here
            return redirect('results', image_id=image.id)
    else:
        form = UploadForm()
    return render(request, 'pixeltruth_app/upload.html', {'form': form})


def results(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)
    return render(request, 'pixeltruth_app/results.html', {'image': image})


#multiple recent uploaded images
def recent_results(request):
    images = UploadedImage.objects.order_by('-id')[:10]  # last 10 images
    return render(request, 'pixeltruth_app/recent_results.html', {'images': images})
