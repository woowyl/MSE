(function() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('scoreNumTop'));

    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '评分人数Top20'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: "30%"
        },
        toolbox: {
            // y: 'bottom',
            feature: {
                saveAsImage: {
                    pixelRatio: 2
                }
            }
        },
        legend: {
            data:['评分人数']
        },
        xAxis: [
            {
                type: 'value',
                name: '评论人数',
                min: 300000
            },
            {
                type: 'value',
                name: '分数',
                min: 5
            },
        ],
        yAxis: {
            data: window.SCORE_NUM_TOP_NAMES,
            inverse: true,
            axisPointer: {
                type: 'shadow'
            }
        },
        series: [{
            name: '评分人数',
            type: 'bar',
            data: window.SCORE_NUM_TOP_VALUES,
            label: {
                show: true,
                position: 'right'
            },
        },{
            name: '分数',
            type: 'line',
            data: [9.0, 8.9, 8.7, 8.1, 8.3, 6.6, 7.1, 8.1, 7.6, 6.7, 9.1, 8.3, 7.2, 8.1, 7.6, 8.7, 7.0, 8.6, 7.2, 7.2],
            xAxisIndex: 1,
            label: {
                show: true,
                position: 'right'
            },
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
})();