// Smooth scroll for nav links
document.querySelectorAll('.nav-links a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Scroll to top smoothly when clicking the logo
const logo = document.querySelector('.logo');
if (logo) {
  logo.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Animate "Start Now" button on hover
const startBtn = document.querySelector('.btn-start');
if (startBtn) {
  startBtn.addEventListener('mouseenter', () => {
    startBtn.style.transform = 'scale(1.05)';
    startBtn.style.boxShadow = '0 8px 20px rgba(0, 119, 182, 0.2)';
  });

  startBtn.addEventListener('mouseleave', () => {
    startBtn.style.transform = 'scale(1)';
    startBtn.style.boxShadow = 'none';
  });
}
