// Get DOM elements
const startCameraBtn = document.getElementById('start-camera');
const capturePoseBtn = document.getElementById('capture-pose');
const videoPreview = document.getElementById('video-preview');
const poseCanvas = document.getElementById('pose-canvas');
const fileInput = document.getElementById('pose-upload');

let videoStream = null;

// Start the webcam stream
startCameraBtn?.addEventListener('click', async () => {
  try {
    videoStream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: false
    });
    videoPreview.srcObject = videoStream;
    videoPreview.style.display = 'block';
  } catch (error) {
    alert('❌ Unable to access the camera. Please allow permission.');
    console.error('Camera Error:', error);
  }
});

// Capture pose image from video stream
capturePoseBtn?.addEventListener('click', () => {
  if (!videoStream) {
    alert('⚠️ Please start the camera first.');
    return;
  }

  const canvas = poseCanvas;
  const ctx = canvas.getContext('2d');

  // Set canvas size to match video
  canvas.width = videoPreview.videoWidth;
  canvas.height = videoPreview.videoHeight;

  // Draw the current video frame onto the canvas
  ctx.drawImage(videoPreview, 0, 0, canvas.width, canvas.height);

  alert('📸 Pose captured! You can now analyze this pose manually or build further upload support.');
});

// Preview uploaded image on canvas
fileInput?.addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (e) {
    const img = new Image();
    img.onload = function () {
      poseCanvas.width = img.width;
      poseCanvas.height = img.height;

      const ctx = poseCanvas.getContext('2d');
      ctx.drawImage(img, 0, 0, img.width, img.height);
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
});
