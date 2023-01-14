export default [
	{
		path: 'checkout',
		name: 'checkout',
		component: () => import('@/components/cart/checkout.vue')
	},
	{
		path: 'pay',
		name: 'pay',
		component: () => import('@/components/cart/pay.vue')
	},
]