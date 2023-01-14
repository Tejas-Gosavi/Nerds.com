<script setup lang="ts">
import { RouterView } from 'vue-router';
import Navbar from '@/components/common/navbar.vue';
import Paginator from '@/components/common/paginator.vue';
import CartModel from '@/components/common/cartModel.vue';

</script>

<template>
  	<Navbar />
	<CartModel />
	<main class="container pt-4">
		<div class="pt-5" id="content">
			<RouterView />
			<Paginator />
		</div>
	</main>
</template>

<style>
</style>
