function addMessage(messageTag, message) {
    alertBox = $('#alert');
    $(alertBox).removeAttr('class');
    $(alertBox).addClass("alert alert-dismissible " + messageTag);
    $(alertBox).find('.alert-text').text(message);
    $(alertBox).removeAttr('hidden');
}

$(document).ready(function () {
    $(".addToCart").click(function (e) {
        productId = $(this).val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/cart/add",
            data: {
                productId: productId,
            },
            dataType: "json",
            success: function (response) {
                if (response.addToCartCode == 0) {
                    product = $("#content").find('#' + productId);
                    productImg = $(product).find(".productImg").attr("src");
                    productType = $(product).find("#productType").text();
                    productTitle = $(product).find("#productTitle").text();
                    productPrice = $(product).find("#productPrice").text();

                    cartProductClone = $("#productTemplate").clone(true);
                    $(cartProductClone).find('#product-img').attr("src", productImg);
                    $(cartProductClone).find('#product-title').text(productTitle);
                    $(cartProductClone).find('#product-price').text(productPrice);
                    $(cartProductClone).find('.cartRemove').attr("id", "remove-" + productId);
                    $(cartProductClone).attr("id", productId);
                    $(cartProductClone).removeAttr('hidden');
                    $("#cartList").append(cartProductClone);

                    subTotal = parseInt($("#cartSubtotal").text());
                    $(".subtotal").text(subTotal + parseInt(productPrice));

                    $("#cartCount").text(parseInt($("#cartCount").text()) + 1);

                    subTotal = parseInt($("#cartSubtotal").text());
                    deliveryCharge = $("#deliveryOption option:selected").val();
                    $("#total").text(parseInt(subTotal) + parseInt(deliveryCharge));

                    if (subTotal == 0) {
                        window.location.reload();
                    } else {
                        addMessage("alert-success", "Added to Cart");
                        $("#checkoutBtn").removeClass("disabled");
                    }
                } else {
                    addMessage("alert-warning", "Already in Cart");
                }
            },
            error: function (xhr, errmsg, err) {
                window.location.reload();
            }
        });

    });
    $(".cartRemove").click(function () {
        productId = $(this).attr("id").slice(7);
        product = $("#cartList").find('#' + productId);

        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/cart/delete",
            data: {
                productId: productId,
            },
            dataType: "json",
            success: function (response) {
                if (response.deleteFromCartCode == 0) {
                    productPrice = $(product).find("#product-price").text();
                    subTotal = parseInt($("#cartSubtotal").text());
                    $(".subtotal").text(subTotal - parseInt(productPrice));
                    $("#cartList").find("#" + productId).remove();
                    $("#checkoutCartList").find("#" + productId).remove();
                    $("#cartCount").text(parseInt($("#cartCount").text()) - 1);

                    subTotal = parseInt($("#cartSubtotal").text());
                    deliveryCharge = $("#deliveryOption option:selected").val();
                    $("#total").text(parseInt(subTotal) + parseInt(deliveryCharge));

                    subTotal = parseInt($("#cartSubtotal").text());
                    if (subTotal == 0) {
                        window.location.reload();
                    } else {
                        addMessage("alert-warning", "Removed from Cart");
                        $("#checkoutBtn").removeClass("disabled");
                    }
                } else {
                    addMessage("alert-warning", "Not in Cart to Remove");
                }
            },
            error: function (xhr, errmsg, err) {
                window.location.reload();
            }
        });

    });

    $(".addToWishlist").click(function () {
        let temp = $(this).hasClass("fromList");
        let productId = $(this).val();
        $.ajax({
            type: "POST",
            url: "/add-to-wishlist",
            data: {
                productId: productId,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.toWishlistCode != 2) {
                    if (temp) {
                        $("#wishlist #" + productId).remove();
                    }
                    if (response.toWishlistCode == 0) {
                        messageTag = "alert-warning"
                        message = "Removed from Wishlist"
                        $(".addToWishlist").text("Add to Wishlist");
                    } else {
                        messageTag = "alert-success"
                        message = "Added to Wishlist"
                        $(".addToWishlist").text("Remove from Wishlist");
                    }
                    addMessage(messageTag, message);
                } else {
                    addMessage("alert-info", "Please Log In to add in wishlist");
                }
            },
            error: function (xhr, errmsg, err) {
                window.location.reload();
            }
        });
    });

    $("#logInbtn").click(function () {

        clearInitialCSS("logInbtn");

        $.ajax({
            type: "POST",
            url: "/account/login",
            data: {
                email: $("#loginEmail").val(),
                password: $("#loginPassword").val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.logInCode == 0) {
                    window.location.reload();
                    addMessage("alert-success", "Successfully logged in!");
                } else if (response.logInCode == 1) {
                    $("#collapseOne").find(".invalid-email").show();
                    $("#loginEmail").focus();
                    $("#loginEmail").addClass("invalid");
                } else if (response.logInCode == 2) {
                    $("#collapseOne").find(".invalid-password").show();
                    $("#loginPassword").focus();
                    $("#loginPassword").addClass("invalid");
                } else if (response.logInCode == 3) {
                    $("#collapseOne").find(".invalid-email2").show();
                    $("#loginEmail").focus();
                    $("#loginEmail").addClass("invalid");
                }
            }
        });

    });

    $("#signUpbtn").click(function () {

        clearInitialCSS("signUpbtn");

        $.ajax({
            type: "POST",
            url: "/account/signup",
            data: {
                email: $("#signupEmail").val(),
                password1: $("#signupPassword1").val(),
                password2: $("#signupPassword2").val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.signUpCode == 0) {
                    window.location.reload();
                    addMessage("alert-success", "Successfully signed up!");
                } else if (response.signUpCode == 1) {
                    $("#collapseTwo").find(".invalid-password2").show();
                    $("#signupPassword1").addClass("invalid");
                    $("#signupPassword2").addClass("invalid");
                } else if (response.signUpCode == 2) {
                    $("#collapseTwo").find(".invalid-password").show();
                    $("#signupPassword1").focus();
                    $("#signupPassword1").addClass("invalid");
                    $("#signupPassword2").addClass("invalid");
                } else if (response.signUpCode == 3) {
                    $("#collapseTwo").find(".invalid-email").show();
                    $("#signupEmail").focus();
                    $("#signupEmail").addClass("invalid");
                }
            }
        });
    });

    $("#logOutBtn").click(function () {
        $.ajax({
            type: "POST",
            url: "/account/logout",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.logOutCode == 0) {
                    addMessage("alert-success", "Successfully logged out!");
                    window.location.reload();
                }
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    /////// Prevent closing from click inside dropdown
    document.querySelectorAll('.dropdown-menu').forEach(function (element) {
        element.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    })
});

function clearInitialCSS(field) {
    switch (field) {

        case "logInbtn":
            $("#collapseOne #loginEmail").removeClass("invalid");
            $("#collapseOne #loginPassword").removeClass("invalid");
            $("#collapseOne .invalid-email").hide();
            $("#collapseOne .invalid-email2").hide();
            $("#collapseOne .invalid-password").hide();
            break;

        case "signUpbtn":
            $("#collapseTwo #signupEmail").removeClass("invalid");
            $("#collapseTwo #signupPassword1").removeClass("invalid");
            $("#collapseTwo #signupPassword2").removeClass("invalid");
            $("#collapseTwo .invalid-email").hide();
            $("#collapseTwo .invalid-password").hide();
            $("#collapseTwo .invalid-password2").hide();
            break;

        case "savePersonalData":
            $("#profile #firstName").removeClass("invalid");
            $("#profile #lastName").removeClass("invalid");
            $("#profile #phoneNumber").removeClass("invalid");
            $("#profile .firstName").hide();
            $("#profile .lastName").hide();
            $("#profile .phoneNumber").hide();
            break;

        case "saveChangePassword":
            $("#profile #oldPassword").removeClass("invalid");
            $("#profile #newPassword").removeClass("invalid");
            $("#profile #newPassword2").removeClass("invalid");
            $("#profile .invalid-oldPassword").hide();
            $("#profile .invalid-newPassword").hide();
            $("#profile .invalid-newPassword2").hide();
            $("#profile .invalid-newPassword3").hide();
            $("#profile .oldPassword").hide();
            $("#profile .newPassword").hide();
            $("#profile .newPassword2").hide();
            break;

        case "saveShippingAddress":
            $("#address #buildingName").removeClass("invalid");
            $("#address #streetName").removeClass("invalid");
            $("#address #landmark").removeClass("invalid");
            $("#address #townCity").removeClass("invalid");
            $("#address #state").removeClass("invalid");
            $("#address #district").removeClass("invalid");

            $("#address .buildingName").hide();
            $("#address .streetName").hide();
            $("#address .landmark").hide();
            $("#address .townCity").hide();
            $("#address .state").hide();
            $("#address .district").hide();
            break;
        default:
            break;
    }
}