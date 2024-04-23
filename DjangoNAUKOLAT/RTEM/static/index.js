document.addEventListener("DOMContentLoaded", () => {
    const chartData = prepareChartData(globalChartData);
    initializeAreaChart(chartData);
    initializeBarChart(chartData);
});

function prepareChartData(data) {
    return data.map(item => ({
        x: new Date(item.timestamp).getTime(), // Convert timestamp to millisecond representation
        y: item.energy_consumption,
        device_id: item.device_id
    }));
}

function initializeAreaChart(chartData) {
    const options = {
        chart: {
            id: "areaChart",
            type: "area",
            height: 230,
            foreColor: "#ccc",
            toolbar: {
                autoSelected: "pan",
                show: false
            }
        },
        colors: ["#00BAEC"],
        stroke: {
            width: 3
        },
        grid: {
            borderColor: "#555",
            clipMarkers: false,
            yaxis: {
                lines: {
                    show: false
                }
            }
        },
        dataLabels: {
            enabled: false
        },
        fill: {
            gradient: {
                enabled: true,
                opacityFrom: 0.55,
                opacityTo: 0
            }
        },
        markers: {
            size: 5,
            colors: ["#000524"],
            strokeColor: "#00BAEC",
            strokeWidth: 3
        },
        series: [{
            data: chartData
        }],
        tooltip: {
            theme: "dark",
            x: {
                format: "dd MMM yyyy"
            },
            y: {
                formatter: (val, { seriesIndex, dataPointIndex, w }) =>
                    `Consumption: ${val}<br>Device ID: ${w.config.series[seriesIndex].data[dataPointIndex].device_id}`
            }
        },
        xaxis: {
            type: "datetime"
        },
        yaxis: {
            min: 0,
            tickAmount: 4
        }
    };

    const chart = new ApexCharts(document.querySelector("#chart-area"), options);
    chart.render();
}

function initializeBarChart(chartData) {
    const options = {
        chart: {
            id: "barChart",
            height: 130,
            type: "bar",
            foreColor: "#ccc",
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
                    min: new Date("2020-01-01").getTime(),
                    max: new Date("2020-01-31").getTime()
                }
            }
        },
        colors: ["#FF0080"],
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
                theme: "dark",
                x: {
                    format: "dd MMM yyyy"
                },
                y: {
                    formatter: (val, { seriesIndex, dataPointIndex, w }) =>
                        `Consumption: ${val}<br>Device ID: ${w.config.series[seriesIndex].data[dataPointIndex].device_id}`
            }
        },
        yaxis: {
            tickAmount: 2
        }
    };

    const chart = new ApexCharts(document.querySelector("#chart-bar"), options);
    chart.render();
}