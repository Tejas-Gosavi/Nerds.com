import { createRouter, createWebHistory } from 'vue-router'
import comicRouter  from '@/router/comic';
import accountRouter  from '@/router/account';
import cartRouter  from '@/router/cart';


const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [{
			path: '',
			name: 'comic',
			component: () => import('@/views/ComicView.vue'),
			children: [...comicRouter],
		},
		{
			path: '/account',
			name: 'account',
			component: () => import('@/views/AccountView.vue'),
			children: [...accountRouter],
		},
		{
			path: '/cart',
			name: 'cart',
			component: () => import('@/views/CartView.vue'),
			children: [...cartRouter],
		},
		// ...comicRouter,
		// ...accountRouter,
		// ...cartRouter,
		{ path: '/:pathMatch(.*)*', name: 'NotFound', redirect: 'home' },
	]
})

export default router
