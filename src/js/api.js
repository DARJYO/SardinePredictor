export async function predictSardines(temperature, salinity) {
  try {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        temperature,
        salinity,
      }),
    });
    return await response.json();
  } catch (error) {
    console.error('Error predicting sardines:', error);
    throw error;
  }
}
