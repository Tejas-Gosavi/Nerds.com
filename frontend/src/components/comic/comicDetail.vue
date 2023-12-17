<script setup lang="ts">
import router from '@/router';
</script>
<template>
    {{ router.currentRoute.value.fullPath }}
</template>