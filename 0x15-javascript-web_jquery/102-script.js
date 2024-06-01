$(document).ready(() => {
    $('#btn_translate').on('click', () => {
        let val = '';
        val = $('#language_code').val();
        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${val}`,
            method: 'GET',
            success: function (data) {
                $('#hello').html(data.hello);
            },

             error: function (err) {
                console.log(err);
            }
        })
    })
})
