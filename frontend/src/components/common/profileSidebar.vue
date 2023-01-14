<script setup lang="ts">
defineProps({
    sideBar: String
})
const sideBarValues: string[] = ['profile', 'address', 'orders', 'wishlist', 'security'];
</script>

<template>
     <div class="col-md-2 col-sm-3 col-10 offset-sm-0 offset-1 d-flex flex-column p-0 bg-secondary text-center dataBtnGroup">
        <RouterLink v-for="sideBarValue in sideBarValues"
            :to="{ name: sideBarValue }" 
            class="btn dataBtn" 
            v-bind:class="{ 'btn-dark': sideBar === sideBarValue }" 
            role="button"
        >{{ sideBarValue }}</RouterLink>
    </div>
</template>