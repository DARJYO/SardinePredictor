document.getElementById('sardineForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const temperature = document.getElementById('temperature').value;
    const salinity = document.getElementById('salinity').value;

    fetch('https://your-backend-url.com/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            temperature: temperature,
            salinity: salinity,
        }),
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        if (data.prediction === 1) {
            resultDiv.innerHTML = `<div class="alert alert-success">Sardines are likely to be present.</div>`;
        } else {
            resultDiv.innerHTML = `<div class="alert alert-warning">Sardines are unlikely to be present.</div>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

