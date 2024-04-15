document.addEventListener('DOMContentLoaded', function () {
    // Parse the forecast data from the Django template
    // Assuming forecastData is already assigned in the HTML before this script tag
    const parsedData = JSON.parse(forecastData);

    // Map the parsed data to the format Chart.js expects
    const chartLabels = parsedData.map(data => data.timestamp);
    const chartData = parsedData.map(data => data.energy_consumption);

    // Get the context of the canvas element
    const ctx = document.getElementById('forecastChart').getContext('2d');

    // Create the chart
    const forecastChart = new Chart(ctx, {
        type: 'line', // Line chart type
        data: {
            labels: chartLabels, // The timestamps
            datasets: [{
                label: 'Forecasted Energy Consumption',
                data: chartData, // The forecasted energy consumption data
                borderColor: 'rgb(75, 192, 192)', // The color of the line
                tension: 0.1 // The smoothness of the line
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time', // Make sure this matches the format of your timestamps
                    time: {
                        unit: 'day', // The unit of time on the x-axis
                        tooltipFormat: 'll', // The date format of the tooltip
                        displayFormats: {
                            'day': 'MMM D' // Display format of the labels on x-axis
                        }
                    },
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    beginAtZero: false, // If false, scale starts at the lowest value; if true, it starts at 0
                    title: {
                        display: true,
                        text: 'Energy Consumption (kWh)'
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y.toFixed(2) + ' kWh';
                        }
                    }
                }
            }
        }
    });
});
