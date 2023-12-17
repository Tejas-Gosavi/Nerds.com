export default [
    {
        path: '',
        name: 'comic',
        component: () => import('@/components/comic/comic.vue')
    },
    {
        path: 'brand/:brand',
        name: 'brand',
        component: () => import('@/components/comic/brand.vue')
    },
    {
        path: 'type/:type',
        name: 'type',
        component: () => import('@/components/comic/comic.vue')
    },
    {
        path: ':brand/:type/:comic',
        name: 'detail',
        component: () => import('@/components/comic/comicDetail.vue')
    },
    {
        path: 'volumes',
        name: 'volumes',
        component: () => import('@/components/comic/volume.vue')
    },
    {
        path: 'search',
        name: 'searchComics',
        component: () => import('@/components/comic/search.vue')
    },
]