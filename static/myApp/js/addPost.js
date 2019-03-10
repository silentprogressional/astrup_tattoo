function clickFunc() {
    var title = $("textarea#title").val();
    var category = $("textarea#category").val();
    var start = $("textarea#start").val();
    var main = $("textarea#main").val();
    var image = document.getElementById("file-id").files[0].name;

    $.ajax({
        url: "/addPost",
        type: "POST",
        data: {
            title: title,
            category: category,
            start: start,
            main: main,
            image: image,
        },
        cache: false,
        success: function () {
            // Enable button & show success message
            $("#success-alert").show();
            setTimeout(function () {
                window.location.replace("/blogPage");
            }, 2000);


        },
        error: function () {
            // Fail message
            $("#fail-alert").show();

        },
    })
}