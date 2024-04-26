
document.addEventListener("DOMContentLoaded", () => {
    const chartData = prepareChartData(globalChartData);
    initializeAreaChart(chartData);
    initializeBarChart(chartData, "chart-bar", "Energy Consumption Over Time");
    initializeComboChart(chartData);
});

function prepareChartData(data) {
    return data.map(item => ({
        x: new Date(item.timestamp).getTime(),
        y: parseFloat(item.energy_consumption),
        device_id: item.device_id
    }));
}

function initializeAreaChart(chartData) {
    const options = {
        chart: {
            id: "areaChart",
            type: "area",
            height: '100%',
            width: '100%',
            foreColor: "#333",
            toolbar: {
                autoSelected: "zoom"
            }
        },
        colors: ["#007BFF"], // Bootstrap primary color
        stroke: {
            curve: 'smooth',
            width: 2
        },
        grid: {
            borderColor: "#e7e7e7",
            yaxis: {
                lines: {
                    show: true
                }
            }
        },
        dataLabels: {
            enabled: false
        },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.7,
                opacityTo: 0.9,
                stops: [0, 100]
            }
        },
        markers: {
            size: 0
        },
        series: [{
            name: 'Energy Consumption',
            data: chartData
        }],
        tooltip: {
            theme: "dark",
            x: {
                format: "dd MMM yyyy"
            },
            y: {
                formatter: function (value) {
                    return `${value} kWh`;
                }
            },
            z: {
                formatter: function (value, { series, seriesIndex, dataPointIndex }) {
                    return `Device ID: ${series[seriesIndex].data[dataPointIndex].device_id}`;
                }
            }
        },
        xaxis: {
            type: "datetime",
            tickAmount: 6
        },
        yaxis: {
            title: {
                text: 'Energy Consumption (kWh)'
            }
        },
        responsive: [{
            breakpoint: 768,
            options: {
                chart: {
                    height: 350
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    const chart = new ApexCharts(document.querySelector("#chart-area"), options);
    chart.render();
}

function initializeBarChart(chartData) {
    const options = {
        chart: {
            id: "barChart",
            height: 300,
            type: "bar",
            foreColor: "#333",
            brush: {
                target: "areaChart",
                enabled: true
            },
            selection: {
                enabled: true,
                fill: {
                    color: "#fff",
                    opacity: 0.4
                },
                xaxis: {
                    min: new Date(chartData[0].x).getTime(),
                    max: new Date(chartData[chartData.length - 1].x).getTime()
                }
            }
        },
        colors: ["#28a745"], // Bootstrap success color
        series: [{
            data: chartData
        }],
        stroke: {
            width: 2
        },
        grid: {
            borderColor: "#444"
        },
        markers: {
            size: 0
        },
        xaxis: {
            type: "datetime",
            tooltip: {
                enabled: false
            }
        },
        yaxis: {
            tickAmount: 2
        }
    };

    const chart = new ApexCharts(document.querySelector("#chart-bar"), options);
    chart.render();
}
function initializeComboChart(chartData, elementId) {
    const options = {
        chart: {
            type: 'line',
            stacked: false,
            height: 350,
            toolbar: {
                show: true
            }
        },
        stroke: {
            width: [0, 2, 5],
            curve: 'smooth'
        },
        plotOptions: {
            bar: {
                columnWidth: '50%'
            }
        },
        series: [{
            name: 'Bar',
            type: 'bar',
            data: chartData
        }, {
            name: 'Line',
            type: 'line',
            data: chartData
        }],
        xaxis: {
            type: 'datetime'
        },
        yaxis: {
            title: {
                text: 'Energy Consumption (kWh)'
            }
        }
    };

    var chart = new ApexCharts(document.querySelector(`#${elementId}`), options);
    chart.render();
}
