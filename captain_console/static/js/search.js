$(document).ready(function () {
    //
    $("#btn-search").on("click", function(e)
    {
        e.preventDefault();
        let search_string = $("#inp-search").val();
        console.log(search_string)
        location.href = "/products/?search=" + search_string;
    })

    // Update search bar, if we were searching for something
    let searchParams = new URLSearchParams(window.location.search)
    if(searchParams.has("search"))
    {
        $("#inp-search").val(searchParams.get("search"));
    }
})