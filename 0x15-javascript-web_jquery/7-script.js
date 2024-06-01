$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        success: function (data) {
            $('#character').html(data.name)
        },

         error: function (err) {
                console.log(err);
        }
    });
})
