let ourCanvas = $("#ourChart");

let countrties_list = []
let population = []

const chartElement = new Chart(ourCanvas, {
    type: 'bar',
    data: {
        labels: countrties_list,
        datasets: [
            {
                label: 'Популяция в 2019 году',
                data: population,
                backgroundColor: 'rgba(54, 162, 235, 0.4)',
                borderWidth: 1,
                borderRadius: 7,
                borderColor: 'rgba(54, 162, 235, 0.9)'
            }
        ]
    }
});


function getData()
{
    $.ajax({
        url: '/get_data',
        type: 'POST',
        dataType: 'json',
        data: {
            key: '8jdfsd98sdfsd87'
        },
        success: function (data) {
            console.log(data);
            chartElement.data.labels = data['date'];
            chartElement.data.datasets[0].data = data['course'];
            chartElement.update();
        },
        error: function(jqxhr, status, errorMsg) {
            console.log('Ошибка при взаимодействии с сервером: '+errorMsg);
        }
    });
}

// Код, который выполняется после того, как страница загрузилась
$(function() {
    console.log('loading done');
    getData();
});