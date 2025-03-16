// 在页面加载完成后调用初始化函数
document.addEventListener('DOMContentLoaded', () => {
    initTrendCharts();
    initChart();
});

// 添加 fetchSteelPriceData 函数
async function fetchSteelPriceData() {
    try {
        const response = await fetch('/api/data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching steel price data:', error);
        return [];
    }
}

// 处理数据函数
function processData(data) {
    const dates = [];
    const prices = [];
    for (const variety in data) {
        data[variety].forEach(item => {
            dates.push(item.date);
            prices.push(item.price);
        });
    }
    return { dates, prices };
}

// 配置图表函数
function configureChart(processedData) {
    const { dates, prices } = processedData;
    return {
        title: {
            text: '废钢价格趋势分析图'
        },
        xAxis: {
            type: 'category',
            data: dates
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: prices,
            type: 'line'
        }]
    };
}

// 初始化趋势分析图表
async function initTrendCharts() {
    const data = await fetchSteelPriceData();
    const { dates, prices } = processData(data);
    const option = configureChart({ dates, prices });

    if (option && option.title) {
        option.title.text = '废钢价格趋势分析图'; // 修改标题
    }

    const lineChart = echarts.init(document.getElementById('line-chart'));
    lineChart.setOption(option);

    const areaChart = echarts.init(document.getElementById('area-chart'));
    const areaOption = { ...option };
    areaOption.title.text = '不同品种价格占比变化（面积图）';
    areaOption.series[0].areaStyle = {};
    areaChart.setOption(areaOption);

    const kLineChart = echarts.init(document.getElementById('k-line-chart'));
    const kLineOption = {
        title: {
            text: '价格波动和关键支撑位（K 线图）'
        },
        xAxis: {
            type: 'category',
            data: dates
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [
                [20, 30, 10, 40],
                [30, 40, 20, 50],
                [40, 50, 30, 60],
                [50, 60, 40, 70],
                [60, 70, 50, 80],
                [70, 80, 60, 90],
                [80, 90, 70, 100]
            ],
            type: 'candlestick'
        }]
    };
    kLineChart.setOption(kLineOption);
}

// 初始化图表
async function initChart() {
    const data = await fetchSteelPriceData();
    const processedData = processData(data);
    const option = configureChart(processedData);
    // 使用配置项显示图表
    const chartContainer = document.getElementById('chart-container');
    if (chartContainer) {
        const myChart = echarts.init(chartContainer);
        myChart.setOption(option);
    } else {
        console.error('Element with id "chart-container" not found.');
    }
}