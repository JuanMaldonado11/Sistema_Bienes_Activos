console.log(JSON.parse(usuarios_dict));

    var chart = c3.generate({
        bindto: '#visitor',
        data: {
            columns: JSON.parse(usuarios_dict),

            type: 'donut',
            onclick: function (d, i) { },
            onmouseover: function (d, i) { },
            onmouseout: function (d, i) { }
        },
        donut: {
            label: {
                show: false
            },
            title: "Visitantes",
            width: 20,

        },

        legend: {
            hide: true
            //or hide: 'data1'
            //or hide: ['data1', 'data2']
        },
        color: {
            pattern: ['#eceff1', '#745af2', '#26c6da', '#1e88e5']
        }
    });