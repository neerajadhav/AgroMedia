function preview_image(event) 
{
 var reader = new FileReader();
 reader.onload = function()
 {
  var output = document.getElementById('output_image');
  output.src = reader.result;
 }
 reader.readAsDataURL(event.target.files[0]);
}

$('.like-form').submit(function(e){
    e.preventDefault();

    const post_id = $(this).attr('id');

    const likeText = $(`.like-btn${post_id}`).text();
    const trim = $.trim(likeText);

    const url = $(this).attr('action');

    let res;
    const likes = $(`.like-count${post_id}`).text();
    const trimcount = parseInt(likes);
    
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'post_id': post_id,
            // 'likeText': trim,
            // 'likes': trimcount
        },
        success: function(response){
                // $(`.like-count${post_id}`).text(data.likes);
                // $(`.like-btn${post_id}`).text(data.likeText);
                if(trim === '🤍'){
                    $(`.like-count${post_id}`).text(trimcount + 1);
                    $(`.like-btn${post_id}`).text('❤');
                }
                else{
                    $(`.like-count${post_id}`).text(trimcount - 1);
                    $(`.like-btn${post_id}`).text('🤍');
                }
        },
        error: function(error){
            console.log(error);
        }
    });
});