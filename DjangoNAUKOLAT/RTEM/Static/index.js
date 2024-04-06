document.addEventListener("DOMContentLoaded", function() {
    // This maps your data to the format ApexCharts expects.
    var chartData = globalChartData.map(item => {
        return {
            x: new Date(item.timestamp).getTime(), // Convert timestamp to the date's millisecond representation
            y: item.energy_consumption
        };
    });

    // Configuration for the first chart (Area Chart)
    var options1 = {
        chart: {
            id: "chart2",
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
            data: chartData // Use the processed chartData here
        }],
        tooltip: {
            theme: "dark"
        },
        xaxis: {
            type: "datetime" // Ensuring the x-axis is treated as datetime
        },
        yaxis: {
            min: 0,
            tickAmount: 4 // Customize based on your data range
        }
    };

    // Initialize the first chart with the specified options
    var chart1 = new ApexCharts(document.querySelector("#chart-area"), options1);
    chart1.render();

    // Configuration for the second chart (Bar Chart)
    var options2 = {
        chart: {
            id: "chart1",
            height: 130,
            type: "bar",
            foreColor: "#ccc",
            brush: {
                target: "chart2",
                enabled: true
            },
            selection: {
                enabled: true,
                fill: {
                    color: "#fff",
                    opacity: 0.4
                },
                xaxis: {
                    // Adjust these dates based on your dataset or desired window
                    min: new Date("2020-01-01").getTime(),
                    max: new Date("2020-01-31").getTime()
                }
            }
        },
        colors: ["#FF0080"],
        series: [{
            data: chartData // Use the same chartData for consistency
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
            type: "datetime", // Ensuring the x-axis is treated as datetime
            tooltip: {
                enabled: false
            }
        },
        yaxis: {
            tickAmount: 2 // Customize based on your data range
        }
    };

    // Initialize the second chart with the specified options
    var chart2 = new ApexCharts(document.querySelector("#chart-bar"), options2);
    chart2.render();
});
