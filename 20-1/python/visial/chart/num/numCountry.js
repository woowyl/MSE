(function() {
    (function() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('numCountry'));
    
        // 指定图表的配置项和数据
        option = {
            color: ['#3398DB'],
            tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                }
            },
            toolbox: {
                // y: 'bottom',
                feature: {
                    saveAsImage: {
                        pixelRatio: 2
                    }
                }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [
                {
                    type: 'category',
                    data: [ '美国','中国大陆', '日本','英国', '法国','德国' ,'印度', '韩国','港澳台',  '意大利',  ],
                    axisTick: {
                        alignWithLabel: true
                    }
                }
            ],
            yAxis: [
                {
                    type: 'value'
                }
            ],
            series: [
                {
                    name: '发片量',
                    type: 'bar',
                    barWidth: '60%',
                    data: window.NUM_COUNTRY
                }
            ]
        };
        
    
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    })();
})();