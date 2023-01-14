export default [
    {
        path: 'profile',
        name: 'profile',
        component: () => import('@/components/account/profile.vue')
    },
    {
        path: 'address',
        name: 'address',
        component: () => import('@/components/account/address.vue')
    },
    {
        path: 'orders',
        name: 'orders',
        component: () => import('@/components/account/orders.vue')
    },
    {
        path: 'security',
        name: 'security',
        component: () => import('@/components/account/security.vue')
    },
    {
        path: 'wishlist',
        name: 'wishlist',
        component: () => import('@/components/account/wishlist.vue')
    },
    {
        path: 'auth',
        name: 'auth',
        component: () => import('@/components/account/auth.vue')
    },
]