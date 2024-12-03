import { predictSardines } from './api.js';

export function setupFormHandler() {
  const form = document.getElementById('sardineForm');
  const resultDiv = document.getElementById('result');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const temperature = document.getElementById('temperature').value;
    const salinity = document.getElementById('salinity').value;

    try {
      const data = await predictSardines(temperature, salinity);
      if (data.prediction === 1) {
        resultDiv.innerHTML = `<div class="alert alert-success">Sardines are likely to be present.</div>`;
      } else {
        resultDiv.innerHTML = `<div class="alert alert-warning">Sardines are unlikely to be present.</div>`;
      }
    } catch (error) {
      resultDiv.innerHTML = `<div class="alert alert-danger">Error making prediction. Please try again.</div>`;
    }
  });
}
