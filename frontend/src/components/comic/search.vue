<script setup lang="ts">
import ComicGrid from '../common/comicGrid.vue';

</script>

<template>
    <form action="" method="GET">
        <div class="row">
            <div class="col-lg-4 pb-lg-0 col-md-12 pb-3">
                <div class="form-group">
                    <!-- {% render_field search_form.form.title__icontains class+="form-control" placeholder="Comic Title, keyword, etc" %} -->
                </div>
            </div>
            <div class="col">
                <div class="form-group">
                    <!-- {% render_field search_form.form.brand class+="form-control" %} -->
                </div>
            </div>
            <div class="col">
                <div class="form-group">
                    <!-- {% render_field search_form.form.comic_type class+="form-control" %} -->
                </div>
            </div>
        </div>
        <div class="row pt-3 d-flex align-items-end">
            <div class="col">
                <div class="input-group form-group">
                    <div class="input-group-text">&#8377;</div>
                    <!-- {% render_field search_form.form.price__gte class+="form-control" placeholder="Min. Price" %} -->
                </div>
            </div>
            <div class="col">
                <div class="input-group form-group">
                    <div class="input-group-text">&#8377;</div>
                    <!-- {% render_field search_form.form.price__lte class+="form-control" placeholder="Max. Price" %} -->
                </div>
            </div>
            <div class="col-lg-4 pt-lg-0 col-md-12 pt-3">
                <div class="form-group">
                    <button class="btn btn-primary w-100">Search</button>
                </div>
            </div>
        </div>
    </form>
    <!-- <div class="row row-cols-lg-5 row-cols-md-4 row-cols-sm-3 row-cols-2 g-3 pt-5">
        {% for product in products %}
        <div class="col d-flex align-items-stretch" id="{{ product.id }}">
            <div class="card border-0 shadow-sm">
                <img src="{{ product.main_image.url }}" class="card-img-top rounded-0 productImg"
                    alt="Image for {{ product.title | title }}">
                <div class="card-body rounded-0 bg-light">
                    <h6 class="card-subtitle text-muted pt-0 pb-2" id="productType">{{ product.brand.brand_title }}</h6>
                    <h6 class="card-subtitle" style="height: 30px;"><a href="{{ product.get_absolute_url }}"
                            id="productTitle"
                            style="text-decoration: none;">{{ product.title | title | truncatewords:8 }}</a></h6>
                    <div class="card-text pt-3">
                        <h5 class="text-end">&#8377;<span id="productPrice">{{ product.price }}</span></h5>
                        <button class="btn btn-dark w-100 p-lg-2 p-sm-1 p-1 addToCart" value="{{ product.id }}">Add to
                            cart</button>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div> -->
    <!-- <script>
        $(document).ready(function () {
            $("#id_brand")[0][0].text = "Choose Brand";
            $("#id_comic_type")[0][0].text = "Choose Comic Type";
        });
    </script> -->

    <ComicGrid></ComicGrid>
</template>
