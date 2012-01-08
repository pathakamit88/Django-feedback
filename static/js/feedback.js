$(document).ready(function(){
    var text = '<a name="anc_feedback" id ="id_anc_feedback" class="cls_feedback thickbox" title="Submit Your Feedback" ' +
        'href="/feedback/feedback_form/?height=405&width=480"></a>'
    $('body').prepend(text);
});

function submit_feedback(){
    var name = $('#id_feedback_name').val();
    var email = $('#id_feedback_email').val();
    var contact_no = $('#id_feedback_contact_number').val();
    var type = $('#id_feedback_type :selected').val();
    var text = $('#id_feedback').val();

    var data = {
        'feedback_name': name,
        'feedback_email': email,
        'feedback_contact_number': contact_no,
        'feedback_type': type,
        'feedback': text
    };
    jQuery.ajax({
        url: '/feedback/submit/',
        type: "POST",
        dataType : 'TEXT',
        data: data,
        success: function(res){
            if (res == 'Thanks for submitting your suggestion.'){
//                tb_remove();
                $('#feedback_div').html(res);
                tb_show('Feedback Submitted', '#TB_inline?height=50&width=200&inlineId=feedback_div');
            }else{
                $('#feedback_div').html(res);
            }
        }
    });

}















$(document).ajaxSend(function(event, xhr, settings) {
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
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});