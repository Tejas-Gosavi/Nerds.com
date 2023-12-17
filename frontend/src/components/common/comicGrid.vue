<script setup lang="ts">
import { useComicStore } from '@/stores/comic.store';

const comicStore = useComicStore();
// const props = defineProps(['comics']);
const comics = comicStore.getComics();

</script>
<template>
    <div class="row row-cols-lg-5 row-cols-md-4 row-cols-sm-3 row-cols-2 g-3">
        <div v-for="comic in comics" class="col d-flex align-items-stretch">
            <div class="card border-0 shadow-sm">
                <img class="card-img-top rounded-0 comicImg"
                    :src="`${comicStore.s3Bucket}/${comic.main_image}`"
                    :alt="`Image for ${comic.title}`" loading="lazy">
                <div class="card-body rounded-0 bg-light">
                    <h6 class="card-subtitle text-muted pt-0 pb-2">{{ comic.brand?.brand_title }}</h6>
                    <h6 class="card-subtitle" style="height: 30px;">
                        <RouterLink :to="{ name: 'detail', 
                                params: {
                                    brand: comic.brand?.brand_slug,
                                    type: comic.comic_type?.comic_type_slug,
                                    comic: comic.slug,
                                }}" style="text-decoration: none;">
                            {{ comic.title }}
                        </RouterLink>
                    </h6>
                    <div class="card-text pt-3">
                        <h5 class="text-end">&#8377;<span>{{ comic.price }}</span></h5>
                        <button class="btn btn-dark w-100 p-lg-2 p-sm-1 p-1">Add to cart</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>