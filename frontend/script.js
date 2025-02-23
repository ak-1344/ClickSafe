document.getElementById('urlForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var url = document.getElementById('urlInput').value;
    var threatLevel = Math.random();
    var result, color;
    
    if (threatLevel < 0.6) {
        result = 'Low Risk';
        color = '#4CAF50';
    } else if (threatLevel < 0.9) {
        result = 'Medium Risk';
        color = '#FFC107';
    } else {
        result = 'High Risk';
        color = '#FF5252';
    }

    document.getElementById('urlInput').style.borderColor = color;
    
    // Update the result container
    document.getElementById('resultContainer').classList.remove('hidden');
    document.getElementById('urlStatus').textContent = 'URL: ' + url;
    document.getElementById('threatLevel').textContent = 'Risk Level: ' + result + ' (Threat Score: ' + threatLevel.toFixed(2) + ')';
});

// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});