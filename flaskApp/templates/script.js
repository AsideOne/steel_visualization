// 获取图表容器元素
const chartContainer = document.getElementById('chart-container');
// 初始化 ECharts 实例
const myChart = echarts.init(chartContainer);

// 从后端 API 获取数据
async function fetchSteelPriceData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
}

// 处理数据，提取日期和价格
function processData(data) {
    const dates = data.map(item => item.date);
    const prices = data.map(item => item.price);
    return { dates, prices };
}

// 配置 ECharts 选项
function configureChart(dates, prices) {
    const option = {
        title: {
            text: '废钢价格走势图',
            left: 'center'
        },
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            type: 'category',
            data: dates
        },
        yAxis: {
            type: 'value',
            name: '价格（元/吨）'
        },
        series: [
            {
                name: '废钢价格',
                type: 'line',
                data: prices
            }
        ]
    };
    return option;
}

// 初始化图表
async function initChart() {
    const data = await fetchSteelPriceData();
    const { dates, prices } = processData(data);
    const option = configureChart(dates, prices);
    // 使用配置项显示图表
    myChart.setOption(option);
}

// 调用初始化图表函数
initChart();

// 窗口大小改变时，自适应调整图表大小
window.addEventListener('resize', function () {
    myChart.resize();
});