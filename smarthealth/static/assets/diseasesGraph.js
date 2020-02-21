var ctx = document.getElementById('diseasesBarGraph').getContext('2d');
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
            label: ['Fever'],
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
            label: ['Flue'],
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
            label: ['Flue'],
            data: [50, 19, 3, 5, 2, 6, 23, 52, 52, 5, 67, 29],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
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