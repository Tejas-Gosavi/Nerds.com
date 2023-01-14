import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

import "bootstrap/dist/js/bootstrap.bundle.min";
// import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootswatch/dist/lux/bootstrap.min.css';
import './assets/main.css';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.mount('#app');
