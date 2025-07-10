// result.js

// Get elements from the DOM
const poseNameEl = document.getElementById('detected-pose-name');
const poseImageEl = document.querySelector('.pose-image');
const poseFeedbackEl = document.querySelector('.pose-feedback');

// Try to retrieve pose data from sessionStorage (optional fallback)
const poseName = sessionStorage.getItem("poseName");
const poseFeedback = sessionStorage.getItem("poseFeedback");
const poseImage = sessionStorage.getItem("poseImage");

// If values exist in sessionStorage, override DOM content
if (poseName && poseFeedback && poseImage) {
  poseNameEl.textContent = poseName;
  poseFeedbackEl.textContent = poseFeedback;
  poseImageEl.src = poseImage;
} else {
  // If server-rendered values already exist (via Django), do nothing
  // Optionally fallback if needed
  if (!poseNameEl.textContent || poseNameEl.textContent.trim() === '') {
    poseNameEl.textContent = "Pose Not Found";
  }
  if (!poseFeedbackEl.textContent || poseFeedbackEl.textContent.trim() === '') {
    poseFeedbackEl.textContent = "We couldn't detect your pose. Please try again.";
  }
  if (!poseImageEl.src || poseImageEl.src.trim() === '') {
    poseImageEl.src = "/static/assets/no-pose.png";
  }
}
