<script setup lang="ts">
// import { defineProps } from 'vue';
// const props = defineProps(['comics']);
// const comics = props.comics;
import { ref } from '@vue/reactivity';
import axios from 'axios';
import { onBeforeMount } from 'vue';
import { useNerdsStore } from '@/stores/index';

const store = useNerdsStore();

let comics = ref([]);

onBeforeMount(async () => {
    try {
        const response = await axios.post(`${store.url}`);
        if (response.data.status === 'Success') {
            comics.value = response.data.data.comics;
        } else {
            alert('Fail');
        }
    } catch (error) {
        alert('Error');
        console.error(error);
    }
})

</script>
<template>
    <div class="row row-cols-lg-5 row-cols-md-4 row-cols-sm-3 row-cols-2 g-3">
        <div v-for="comic in comics" class="col d-flex align-items-stretch">
            <!-- {{ comic.title }} -->
            <div class="card border-0 shadow-sm">
                <img class="card-img-top rounded-0 comicImg"
                    :alt="`Image for ${comic.title}`">
                <div class="card-body rounded-0 bg-light">
                    <h6 class="card-subtitle text-muted pt-0 pb-2">{{ comic.brand_id }}</h6>
                    <h6 class="card-subtitle" style="height: 30px;">
                        <a style="text-decoration: none;">
                            {{ comic.title }}
                        </a>
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