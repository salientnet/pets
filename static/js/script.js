$(document).ready(function() {
    $('#pet_table').DataTable();

    $('#id_birthday').datepicker({
        dateFormat: 'yy-mm-dd',
        maxDate: '0'
    });

    // Delete Action
    $('#deleteModal').on('show.bs.modal', function(e) {
        $(this).find('#delete').attr('href', $(e.relatedTarget).data('href'));
    });

    $('#delete').click(function(e) {
        e.preventDefault();
        var handler = $(this).attr('href');
        $.post(handler);
        document.location.reload();
    });

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#signup_form').bootstrapValidator({
        fields: {
            password1: {
                validators: {
                    identical: {
                        field: 'password2',
                        message: 'The password and its confirm are not the same'
                    }
                }
            },
            password2: {
                validators: {
                    identical: {
                        field: 'password1',
                        message: 'The password and its confirm are not the same'
                    }
                }
            },
        }
    });
});
