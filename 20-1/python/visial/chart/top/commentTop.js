(function() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('commentNumTop'));

    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '评论人数Top20'
        },
        tooltip: {},
        toolbox: {
            // y: 'bottom',
            feature: {
                saveAsImage: {
                    pixelRatio: 2
                }
            }
        },
        legend: {
            data:['销量']
        },
        xAxis: {
            data: window.COMMENT_TOP_NAMES
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: window.COMMENT_TOP_VALUES
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
})();