// Form submission handler
document.getElementById('urlForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const url = document.getElementById('urlInput').value;
    
    if (!url) {
        alert('Please enter a URL!');
        return;
    }

    try {
        // Show loading spinner while waiting for response
        document.getElementById('loadingSpinner').classList.remove('hidden');

        // Send URL to backend for analysis
        const response = await fetch('http://localhost:5000/check-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        // Hide loading spinner once response is received
        document.getElementById('loadingSpinner').classList.add('hidden');

        if (response.ok) {
            // Set border color based on risk level
            let color;
            switch (data.risk) {
                case 'Low Risk':
                    color = '#4CAF50';
                    break;
                case 'Medium Risk':
                    color = '#FFC107';
                    break;
                case 'High Risk':
                    color = '#FF5252';
                    break;
                default:
                    color = '#ccc';
            }

            document.getElementById('urlInput').style.borderColor = color;

            // Show and update result container
            document.getElementById('resultContainer').classList.remove('hidden');
            document.getElementById('urlStatus').textContent = `URL: ${data.url}`;
            document.getElementById('threatLevel').textContent = `Risk Level: ${data.risk} (Threat Score: ${data.threatScore})`;
        } else {
            alert(data.error || 'Failed to analyze URL');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong! Please try again.');
    }
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
