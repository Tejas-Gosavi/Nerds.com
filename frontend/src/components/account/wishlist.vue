<script setup lang="ts">
import ProfileSidebar from '../common/profileSidebar.vue';

const wishlist: any[] = [];
</script>

<template>
    <div class="row">
        <ProfileSidebar side-bar="wishlist" />
        <div class="col-md-10 col-sm-9 col-10 offset-sm-0 offset-1 d-flex flex-column ps-md-5 ps-sm-4 ps-0 pt-sm-0 pt-4 dataGroup">
            <legend>Wishlist</legend>
            <template v-if="wishlist.length == 0">
                <p class="text-center">Nothing here <i class="bi bi-emoji-frown"></i></p>
            </template>
            <template v-else>
                <div class="row row-cols-lg-4 row-cols-md-3 row-cols-2 g-3 pb-3" id="wishlists-all">
                    <!-- {% for product in wishlist %} -->
                    <div class="col d-flex align-items-stretch" id="{{ product.id }}">
                        <div class="card border-0 shadow-sm">
                            <img src="" class="card-img-top rounded-0 productImg"
                                alt="Image for">
                            <div class="card-body rounded-0 bg-light">
                                <h6 class="card-subtitle text-muted pt-0 pb-2" id="productType"></h6>
                                <h6 class="card-subtitle" style="height: 30px;"><a href=""
                                        id="productTitle"
                                        style="text-decoration: none;"></a>
                                </h6>
                                <div class="card-text pt-3">
                                    <h5 class="text-end">&#8377;<span id="productPrice"></span></h5>
                                    <button class="btn btn-dark w-100 p-lg-2 p-sm-1 p-1 addToCart"
                                        value="}">Add to cart</button>
                                    <button
                                        class="btn btn-outline-danger w-100 mt-2 p-lg-2 p-sm-1 p-1 addToWishlist fromList"
                                        value="">Remove</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- {% endfor %} -->
                </div>
            </template>
        </div>
    </div>
</template>