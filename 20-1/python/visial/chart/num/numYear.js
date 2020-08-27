(function() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('numYear'));

    // 指定图表的配置项和数据
    option = {
        title: {
            text: '2010-2020数量变化'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['总量', '中国大陆', '港澳台', '印度', '美国', '韩国', '日本']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
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
            data: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: '总量',
                type: 'line',
                stack: '总量',
                data: window.NUM_YEAR_TOTAL
            },
            {
                name: '中国大陆',
                type: 'line',
                data: window.NUM_YEAR_CN
            },{
                name: '港澳台',
                type: 'line',
                data: window.NUM_YEAR_GAT
            },
            {
                name: '印度',
                type: 'line',
                data: window.NUM_YEAR_IND
            },
            {
                name: '美国',
                type: 'line',
                data: window.NUM_YEAR_USA
            },
            {
                name: '韩国',
                type: 'line',
                data: window.NUM_YEAR_KOR 
            },
            {
                name: '日本',
                type: 'line',
                data: window.NUM_YEAR_JAP
            }
        ],
        color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
    };
    

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
})();