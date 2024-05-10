function adjustResumeContainerWidth() {
    var resumeContainer = document.querySelector('.resume-container');
    if (window.innerWidth <= 768) {
        resumeContainer.style.width = '100%';
    } 
}
adjustResumeContainerWidth();
document.addEventListener('DOMContentLoaded', function() {
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target);
        }
    });
});

document.querySelectorAll('.fade-in').forEach(section => {
    observer.observe(section);
});
});
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
    });
});
});
var themes = ['onyx', 'ebony', 'twilight', 'midnight', 'shadow'];
var currentThemeIndex = -1;
function toggleTheme() {
    currentThemeIndex = (currentThemeIndex + 1) % themes.length;
    var theme = themes[currentThemeIndex];
    document.body.className = theme;
}
