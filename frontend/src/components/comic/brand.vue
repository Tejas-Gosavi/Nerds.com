<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import axios from 'axios';
import { useComicStore } from '@/stores/comic.store';
import { useUserStore } from '@/stores/user.store';
import type { Comic } from '@/interface/comic.interface';
import comicGrid from '@/components/common/comicGrid.vue'; 
import router from '@/router';

const comicStore = useComicStore();
const userStore = useUserStore();

let comics = ref<Comic[]>([]);

onBeforeMount(async () => {
    try {
        const response = await axios.post(`${userStore.url}${router.currentRoute.value.path}`);
        if (response.data.status === 'Success') {
            comicStore.setBrands(response.data.data.brands);
            comicStore.setComicTypes(response.data.data.comic_types);
            comicStore.setComics(response.data.data.comics);
        } else {
            alert('Fail');
        }
    } catch (error) {
        alert('Error');
        console.error(error);
    }
})

comics.value = comicStore.getComics();
</script>

<template>
    <!-- <h1 v-if="router.currentRoute.value.name?.toString() != 'comic'">
        {{ router.currentRoute.value.name?.toString() }}
    </h1> -->
    <comicGrid/>
</template>
