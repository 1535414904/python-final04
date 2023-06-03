const canvas = document.getElementById('myChart');
const data = {
    labels: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
    datasets: [{
        label: '交通事故次數',
        data: [12, 19, 3, 5, 2, 3, 3, 3, 3, 3, 3, 3],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
    }]
};
const ctx = canvas.getContext('2d');
new Chart(ctx, {
    type: 'line',
    data: data,
});




const bcc = document.getElementById('b');
const bd = {
    labels: ['一月', 'February', 'March', 'April', 'May', 'June', 'June', 'June', 'June'],
    datasets: [{
        label: 'Sample Data',
        data: [12, 19, 3, 5, 2, 3],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
    }]
};
const bc = bcc.getContext('2d');
new Chart(bc, {
    type: 'line',
    data: bd,
});

