<script setup lang="ts">
import { onBeforeMount } from 'vue';
import router from '@/router';
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import { useUserStore } from '@/stores/user.store';
import ProfileSidebar from '../common/profileSidebar.vue';
import axios from 'axios';

const store = useUserStore();

const personalDataSchema = yup.object({
    first_name: yup.string().required('First name is required'),
    last_name: yup.string().required('Last name is required'),
    phone_number: yup.string().required('Phone number is required').length(10, 'Phone number must be of 10 digits')
})

onBeforeMount(() => {
    if (!store.isUserLoggedIn()) {
        router.push('auth');
    }
});

let personalDataSchemaInitialValues = store.getPersonalData();

const savePersonalData = async (values: any, actions: any) => {
    try {
        const response = await axios.post(`${store.url}/account/saveUserPersonalData`, {
            email: store.getUser(),
            ...values
        });

        if (response.data.status === 'Success') {
            store.setPersonalData(response.data.data);
        } else {
            alert('Fail');
        }
    } catch (error) {
        alert('Error');
        console.error(error);
    }
}
</script>

<template>
    <div class="row">
        <ProfileSidebar side-bar="profile" />
        <div class="d-flex flex-column col-md-10 col-sm-9 col-10 offset-sm-0 offset-1 ps-md-5 ps-sm-4 ps-0 pt-sm-0 pt-4 dataGroup">
            <Form @submit="savePersonalData" :validation-schema="personalDataSchema" 
                    :initial-values="personalDataSchemaInitialValues" class="form-group mb-5">
                <legend>Personal Data</legend>
                <div class="row">
                    <div class="col">
                        <label for="first_name" class="col-form-label py-1">First Name</label>
                        <Field class="form-control" placeholder="eg. Tom" 
                            aria-label="First name" name="first_name" />
                        <ErrorMessage name="first_name" class="text-danger" as="p"/>
                    </div>
                    <div class="col">
                        <label for="last_name" class="col-form-label py-1">Last Name</label>
                        <Field class="form-control" placeholder="eg. Hardy" 
                            aria-label="Last name" name="last_name" />
                        <ErrorMessage name="last_name" class="text-danger" as="p"/>
                    </div>
                </div>
                <div class="row pt-3">
                    <div class="col-6">
                        <label for="phone_number" class="col-form-label py-1">Phone Number</label>
                        <Field class="form-control" placeholder="eg. 9876543210" 
                            aria-label="Phone Number" name="phone_number" />
                        <ErrorMessage name="phone_number" class="text-danger" as="p"/>
                    </div>
                </div>
                <div class="row pt-4">
                    <div class="col">
                        <button class="btn btn-dark" type="submit">Save</button>
                    </div>
                </div>
            </Form>
        </div>
    </div>
</template>
