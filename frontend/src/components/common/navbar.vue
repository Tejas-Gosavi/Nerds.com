<script setup lang="ts">
import { useNerdsStore } from '@/stores/index';

const store = useNerdsStore();

const isUserLoggedIn = store.isUserLoggedIn();
const logout = () => {
    store.setUser(false, {});
}
</script>

<template>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container">
            <RouterLink class="navbar-brand" to="/">Nerds</RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav me-auto mb-2 mb-md-0">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle ps-sm-0 ps-3" href="#" data-bs-toggle="dropdown">Comics</a>
                        <div class="dropdown-menu dropdown-large">
                            <div class="row w-md-75">
                                <div class="col">
                                    <h6 class="title">By Brand</h6>
                                    <ul class="list-unstyled" aria-labelledby="navbarDropdown">
                                        <li><a class="dropdown-item"
                                                href="#">brand 1</a>
                                        </li>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="#">Any many more...</a>
                                    </ul>
                                </div>
                                <div class="col pt-sm-0 pt-3">
                                    <h6 class="title">By Type</h6>
                                    <ul class="list-unstyled">
                                        <li><a class="dropdown-item"
                                                href="#">type 1</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link ps-sm-0 ps-3" href="#">Volumes</a>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link ps-sm-0 ps-3" :to="{ name: 'searchComics'}">Search <i
                                class="bi bi-search"></i></RouterLink>
                    </li>
                </ul>
                <div class="d-flex gap-2 justify-content-md-end">
                    <RouterLink v-if="isUserLoggedIn" :to="{ name: 'profile' }" class="text-light me-md-3 me-3">
                        <i class="bi bi-person-circle" style="font-size: 1.6rem;"></i>
                    </RouterLink>
                    <RouterLink v-else :to="{ name: 'auth' }" class="text-light me-md-3 me-3">
                        <i class="bi bi-person-circle" style="font-size: 1.6rem;"></i>
                    </RouterLink>
                    <a class="text-light" role="button" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        <i class="bi bi-cart" style="font-size: 1.6rem;"></i>
                    </a>
                    <div class="navbar-icon-link-badge text-light cart-icon me-md-3 me-3"></div>
                    <a v-if="isUserLoggedIn" @click="logout" class="text-light" role="button">
                        <i class="bi bi-box-arrow-right" style="font-size: 1.6rem;"></i>
                    </a>
                </div>
            </div>
        </div>
    </nav>
</template>