$('#btn_translate').click(function() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Use jQuery to fetch data from the specified API with the language code
        $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
            // Update the content of the div with id 'hello' with the fetched translation
            $('#hello').text(data.hello);
        });
});
