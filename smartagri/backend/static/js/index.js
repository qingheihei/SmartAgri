var realTimeData = {
    "count": 0,
    "start_time": "",
    "air_temp": [],
    "air_humid": [],
    "air_co2": [],
    "air_light": [],
    "soil_temp": [],
    "soil_humid": [],
    "soil_ec": []
};
var all_types = [];

function loadData() {
    var all_url = "http://18.181.92.6:8888/api/v1/sensorvalues/";
    $.ajax({
        url: all_url,
        type: 'GET',
        async: false,
        dataType: 'json',
        success: function (data, status) {
            realTimeData["count"] = data["count"];
            realTimeData["start_time"] = data.data[0].created_at;
            realTimeData["air_temp"] = data.data.filter(obj => obj.sensor_name === "air_temp_1");
            realTimeData["air_humid"] = data.data.filter(obj => obj.sensor_name === "air_humid_1");
            realTimeData["air_co2"] = data.data.filter(obj => obj.sensor_name === "air_co2_1");
            realTimeData["air_light"] = data.data.filter(obj => obj.sensor_name === "air_light_1");
            realTimeData["soil_temp"] = data.data.filter(obj => obj.sensor_name === "soil_temp_1");
            realTimeData["soil_humid"] = data.data.filter(obj => obj.sensor_name === "soil_humid_1");
            realTimeData["soil_ec"] = data.data.filter(obj => obj.sensor_name === "soil_ec_1");
            
            console.log(realTimeData);
        }
    });

    reloadChart(realTimeData);
    return realTimeData;
}

function reloadChart(realTimeData) {
    document.getElementById("sum").getElementsByTagName("li")[0].innerHTML = realTimeData["count"];
    document.getElementById("sum").getElementsByTagName("li")[1].innerHTML = calDays(realTimeData["start_time"].replace(/-|T|:/g, ''));
}

function calDays(data) {
    var date = data.toString();
    var year = date.substring(0, 4);
    var month = date.substring(4, 6);
    var day = date.substring(6, 8);
    var d1 = new Date(year + '/' + month + '/' + day);
    var dd = new Date();
    var y = dd.getFullYear();
    var m = dd.getMonth() + 1;
    var d = dd.getDate();
    var d2 = new Date(y + '/' + m + '/' + d);
    var iday = parseInt(d2 - d1) / 1000 / 60 / 60 / 24;
    return iday;
}

window.onload = function () {
    loadData();
}

setInterval(function () {
    loadData();
}, 30000);

// .line .chart
(function () {
    var category_index = 0;
    var categoryData = [{
        catagory: "temp",
        data: realTimeData["air_temp"].map((obj) => obj.value),
        time: realTimeData["air_temp"].map((obj) => obj.created_at)
    }, {
        catagory: "humid",
        data: realTimeData["air_humid"].map((obj) => obj.value),
        time: realTimeData["air_humid"].map((obj) => obj.created_at)
    }]
    var myChart = echarts.init(document.querySelector(".line .chart"));
    var option = {
        color: '#ed3f35',
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            textStyle: {
                color: "#4c9bfd"
            },
            right: "10%"
        },
        grid: {
            top: '20%',
            left: '3%',
            right: '4%',
            bottom: '3%',
            show: true,
            borderColor: '#012f4a',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [],
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfd",
            },
            axisLine: {
                show: false
            }
        },
        yAxis: {
            type: 'value',
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfd",
            },
            axisLine: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: "#012f4a"
                }
            }
        },
        series: {
            name: 'raspi01',
            type: 'line',
            smooth: true,
            data: []
        }
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () {
        myChart.resize();
    })

    $('.line h2').on('click', 'a', function () {
        category_index = $(this).index();
        var dataObj = categoryData[$(this).index()];
        option.series.data = dataObj.data;
        myChart.setOption(option);
    });

    setInterval(function () {
        categoryData[0].data = realTimeData["air_temp"].map((obj) => obj.value);
        categoryData[0].time = realTimeData["air_temp"].map((obj) => obj.created_at);
        categoryData[1].data = realTimeData["air_humid"].map((obj) => obj.value);
        categoryData[1].time = realTimeData["air_humid"].map((obj) => obj.created_at);
        myChart.setOption({
            xAxis: {
                data: categoryData[category_index].time
            },
            series: {
                name: 'raspi01',
                data: categoryData[category_index].data
            }
        });
    }, 10000);
})();

// ".line2 .chart"
(function () {
    var myChart = echarts.init(document.querySelector(".line2 .chart"));
    var option = {
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            top: "0%",
            right: "10%",
            textStyle: {
                color: "rgba(255,255,255,0.5)",
                fontSize: "12"
            }
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        grid: {
            left: '10',
            top: "30",
            right: '10',
            bottom: '10',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            data: [],
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,6)",
                    fontSize: 12
                }
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.2)"
                }
            }
        }],
        yAxis: [{
            type: 'value',
            axisTick: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.1)"
                }
            },
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,0.6)",
                    fontSize: 12
                }
            },
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.1)"
                }
            }
        }],
        series: {
            name: 'raspi01',
            type: 'line',
            smooth: true,
            lineStyle: {
                color: "#00d887",
                width: 2,
            },
            areaStyle: {
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [{
                        offset: 0,
                        color: "rgba(0,216,135,0.4)"
                    }, {
                        offset: 0.8,
                        color: "rgba(0,216,135,0.1)"
                    }],
                    false
                ),
                shadowColor: "rgba(0,0,0,0.1)"
            },
            symbol: "circle",
            symbolSize: 5,
            itemStyle: {
                color: "#00d887",
                borderColor: "rgba(221,220,107,0.1)",
                borderWidth: 12
            },
            showSymbol: false,
            data: []
        }
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () {
        myChart.resize();
    })

    setInterval(function () {
        var value_list = realTimeData["air_light"].map((obj) => obj.value);
        var time_list = realTimeData["air_light"].map((obj) => obj.created_at);

        myChart.setOption({
            xAxis: {
                data: time_list
            },
            series: {
                name: 'raspi01',
                data: value_list
            }
        });
    }, 10000);

})();

// ".pie .chart"
(function () {
    var myChart = echarts.init(document.querySelector(".pie .chart"));
    option = {
        tooltip: {
            formatter: "{a} <br/>{c} {b}"
        },
        toolbox: {
            show: true,
            feature: {
                restore: {
                    show: true
                }
            }
        },
        series: [{
            name: 'CO2',
            type: 'gauge',
            min: 0,
            max: 1400,
            radius: '100%',
            axisLine: {
                lineStyle: {
                    width: 10
                }
            },
            axisTick: {
                length: 15,
                lineStyle: {
                    color: 'auto'
                }
            },
            splitLine: {
                length: 20,
                lineStyle: {
                    color: 'auto'
                }
            },
            title: {
                offsetCenter: [0, '-30%'],
                textStyle: {
                    fontWeight: 'bolder',
                    fontSize: 14,
                    color: "rgba(221,220,107,0.9)",
                    fontStyle: 'italic'
                }
            },
            detail: {
                textStyle: {
                    fontWeight: 'bolder',
                    fontSize: 14
                }
            },
            data: [{
                value: 40,
                name: 'ppm'
            }]
        }]
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () {
        myChart.resize();
    })

    setInterval(function () {
        var value_list = realTimeData["air_co2"].map((obj) => obj.value);
        option.series[0].data[0].value = value_list[value_list.length-1];
        myChart.setOption(option, true);
    }, 10000);
})();

// ".bar .chart"
(function () {
    var category_index = 0;
    var categoryData = [{
        catagory: "temp",
        data: realTimeData["soil_temp"].map((obj) => obj.value),
        time: realTimeData["soil_temp"].map((obj) => obj.created_at)
    }, {
        catagory: "humid",
        data: realTimeData["soil_humid"].map((obj) => obj.value),
        time: realTimeData["soil_humid"].map((obj) => obj.created_at)
    }]
    var myChart = echarts.init(document.querySelector(".bar .chart"));
    var option = {
        color: ["#00f2f1"],
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            textStyle: {
                color: "#4c9bfd"
            },
            right: "10%"
        },
        grid: {
            left: '3%',
            top: '10px',
            right: '0%',
            bottom: '3%',
            show: true,
            borderColor: '#012f4a',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [],
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfd",
            },
            axisLine: {
                show: false
            }
        },
        yAxis: {
            type: 'value',
            axisTick: {
                show: false
            },
            axisLabel: {
                color: "#4c9bfd",
            },
            axisLine: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: "#012f4a"
                }
            }
        },
        series: {
            name: 'raspi01',
            type: 'line',
            smooth: true,
            data: []
        }
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () {
        myChart.resize();
    })
    $('.bar h2').on('click', 'a', function () {
        category_index = $(this).index();
        var dataObj = categoryData[$(this).index()];
        option.series.data = dataObj.data;
        myChart.setOption(option);
    });

    setInterval(function () {
        categoryData[0].data = realTimeData["soil_temp"].map((obj) => obj.value);
        categoryData[0].time = realTimeData["soil_temp"].map((obj) => obj.created_at);
        categoryData[1].data = realTimeData["soil_humid"].map((obj) => obj.value);
        categoryData[1].time = realTimeData["soil_humid"].map((obj) => obj.created_at);

        myChart.setOption({
            xAxis: {
                data: categoryData[category_index].time
            },
            series: {
                name: 'raspi01',
                data: categoryData[category_index].data
            }
        });
    }, 10000);
})();

// ".bar2 .chart"
(function () {
    var myChart = echarts.init(document.querySelector(".bar2 .chart"));
    var option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            top: "0%",
            right: "10%",
            textStyle: {
                color: "rgba(255,255,255,0.5)",
                fontSize: "12"
            }
        },
        grid: {
            left: '10',
            top: "30",
            right: '10',
            bottom: '10',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            data: [],
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,6)",
                    fontSize: 12
                }
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.2)"
                }
            }
        }],
        yAxis: [{
            type: 'value',
            axisTick: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.1)"
                }
            },
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,0.6)",
                    fontSize: 12
                }
            },
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,0.1)"
                }
            }
        }],
        series: {
            name: 'raspi01',
            type: 'line',
            smooth: true,
            lineStyle: {
                color: "#0184d5",
                width: 2,
            },
            areaStyle: {
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [{
                        offset: 0,
                        color: "rgba(1, 132, 213, 0.4)"
                    }, {
                        offset: 0.8,
                        color: "rgba(1, 132, 213, 0.1)"
                    }],
                    false
                ),
                shadowColor: "rgba(0,0,0,0.1)"
            },
            symbol: "circle",
            symbolSize: 5,
            itemStyle: {
                color: "#0184d5",
                borderColor: "rgba(221,220,107,0.1)",
                borderWidth: 12
            },
            showSymbol: false,
            data: []
        }
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () {
        myChart.resize();
    })

    setInterval(function () {
        var value_list = realTimeData["soil_ec"].map((obj) => obj.value);
        var time_list = realTimeData["soil_ec"].map((obj) => obj.created_at);

        myChart.setOption({
            xAxis: {
                data: time_list
            },
            series: {
                name: 'raspi01',
                data: value_list
            }
        });
    }, 10000);
})();

