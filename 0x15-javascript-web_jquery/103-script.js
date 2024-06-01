$(document).ready(() => {
    let inputField = $("#language_code");

    const fetchHello = (val) => {
        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${val}`,
            method: 'GET',
            success: function (data) {
                $('#hello').html(data.hello);
            }
        })
    }

    inputField.on("keydown", function (event) {
        if (event.key === "Enter") {
            fetchHello(inputField.val());
        }
    });

    $('#btn_translate').on('click', () => {
        inputField = $('#language_code')
        fetchHello(inputField.val());
    })
})
