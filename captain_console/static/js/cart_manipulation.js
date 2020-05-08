$(document).ready(function() {
    $(".btn-cart").on("click", function(e)
    {
        e.preventDefault();
        let addressValue = $(this).attr("id");
        add_item_to_cart(addressValue);
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
    /*let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product_id);
    localStorage.setItem('cart', JSON.stringify(cart));
    console.log(cart);*/
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
    /*let cart = JSON.parse(localStorage.getItem('cart'));
    let products = cart.filter(x => x !== product_id);
    localStorage.setItem('products', JSON.stringify(products));*/
}