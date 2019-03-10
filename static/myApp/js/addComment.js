function clickFunc() {
    var url_string = window.location.href;
    var url = new URL(url_string);
    var postid = url.searchParams.get("postid");
    var comment = $("textarea#comment").val();
    var name = $("textarea#name").val();
    $.ajax({
        url: "/addComment",
        type: "POST",
        data: {
            comment: comment,
            name: name,
            postid: postid,

        },
        cache: false,
        success: function () {
            // Enable button & show success message
            $("#success-alert").show();
            setTimeout(function () {
                location.reload();
            }, 2000);

        },
        error: function () {
            // Fail message
            $("#fail-alert").show();
        },
    })
}