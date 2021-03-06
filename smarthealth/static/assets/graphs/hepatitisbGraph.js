var ctx = document.getElementById('hepatitisbGraph').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ],
        datasets: [{
            label: ['Mabalacat'],
            data: [50, 19, 3, 5, 2, 6, 23, 52, 52, 5, 67, 29],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        },
        {
            label: ['Angeles'],
            data: [50, 19, 3, 5, 2, 6, 23, 52, 52, 5, 67, 29],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        },
        {
            label: ['San Fernando'],
            data: [50, 19, 3, 5, 2, 6, 23, 52, 52, 5, 67, 29],
            backgroundColor: [
                'rgba(12, 243, 97, 0.2)',
            ],
            borderColor: [
                'rgba(12, 243, 97, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});