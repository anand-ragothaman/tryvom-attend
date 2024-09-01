$(document).ready(function () {
    new DataTable('#example', {
        layout: {
            topStart: {
                buttons: ['copy', 'excel', 'pdf', 'colvis', 'csv', 'print']
            }
        }
    });

    // $.ajax({
    //     url: "test.html",
    //     context: document.body
    // }).then(function (respond) {
    //     $(this).addClass("done");
    // }).catch(function (error) {

    // });

    // $("form [required]").parent().find('label').addClass('req-star')

    // $(".custom-file [required]").parent().prev('label').addClass('req-star')

    // $('.required').parent().find('label').addClass('req-star')

    // $('.req-star').each(function () {
    //     $(this).append($('<span>').addClass('text-danger').text("*"));
    // });

    ClassicEditor
        .create(document.querySelector('#ckeditor'), {
            toolbar: [
                'heading', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'link', '|',
                'bulletedList', 'numberedList', 'blockQuote', '|',
                'undo', 'redo', '|',
                'insertTable', 'mediaEmbed', '|',
                'alignment', 'outdent', 'indent', '|',
                'imageUpload', 'fontColor', 'fontBackgroundColor', '|',
                'codeBlock', 'htmlEmbed'
            ]
        })
        .catch(error => {
            console.error(error);
        });



});


