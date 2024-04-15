document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('forecastChart').getContext('2d');
    const forecastChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: forecastData.labels, // Ensure these labels are moment.js compatible date strings
            datasets: [{
                label: 'Forecasted Energy Consumption',
                data: forecastData.data,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        parser: moment.ISO_8601, // Use ISO_8601 for universal parsing of date strings or specify your custom format
                        tooltipFormat: 'll HH:mm', // Adjust if needed
                        unit: 'hour'
                    },
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    beginAtZero: false,
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
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += context.parsed.y.toFixed(2) + ' kWh';
                            }
                            return label;
                        }
                    }
                }
            }
        }
    });
});
