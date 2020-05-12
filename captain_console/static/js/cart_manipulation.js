$(document).ready(function() {
    $(".btn-cart").on("click", function(e)
    {
        e.preventDefault();
        let addressValue = $(this).attr("id");
        add_item_to_cart(addressValue);
        //remove_item_from_cart(addressValue, 1);
    })
    $(".btn-remove-from-cart").on("click", function(e)
    {
        e.preventDefault();
        let addressValue = $(this).attr("id");
        remove_item_from_cart(addressValue, 1);
    })
});

function add_item_to_cart(product_id)
{
    $.ajax({
       url: "/add_to_cart?product_id=" + product_id,
        type:"GET",
        success: function(resp)
        {
            console.log(resp.data);
        },
        error: function(xhr, status, error)
        {
            console.error(error);
        }
    });
}

function remove_item_from_cart(product_id, amount=1)
{
    $.ajax({
       url: "/remove_from_cart?product_id=" + product_id + "&amount=" + amount,
        type:"GET",
        success: function(resp)
        {
            console.log(resp.data);
        },
        error: function(xhr, status, error)
        {
            console.error(error);
        }
    });
}