<script setup lang="ts">
import comicGrid from '@/components/common/comicGrid.vue'; 
import axios from 'axios';
import { onBeforeMount, ref } from 'vue';
import { RouterView } from 'vue-router';
import { useNerdsStore } from '@/stores/index';

const store = useNerdsStore();

</script>

<template>
    <RouterView></RouterView>
    <comicGrid />
</template>
