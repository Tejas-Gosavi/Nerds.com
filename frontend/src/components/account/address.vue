<script setup lang="ts">
import { onBeforeMount } from 'vue';
import router from '@/router';
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import { useNerdsStore } from '@/stores/index';
import ProfileSidebar from '../common/profileSidebar.vue';
import statesDistricts from './statesDistricts.json';
import axios from 'axios';

const store = useNerdsStore();

const states: string[] = statesDistricts.states;
const unionStates: string[] = statesDistricts.unionStates;
const stateAndDistricts: any = statesDistricts.stateAndDistricts;
let districts: string[] = [];

const addressSchema = yup.object({
    building_name: yup.string().required('Building name is required'),
    street_name: yup.string().required('Street name is required'),
    landmark: yup.string().required('Landmark is required'),
    town_city: yup.string().required('Town/City is required'),
    state: yup.string().required('State is required'),
    district: yup.string().required('District is required')
})

const addressSchemaInitialValues = store.getAddress();

onBeforeMount(() => {
    if (!store.isUserLoggedIn()) {
        router.push('auth');
    }

    districts = addressSchemaInitialValues?.state ? 
                stateAndDistricts[addressSchemaInitialValues?.state] : []
})

const onStateChange = (event: any) => {
    districts = stateAndDistricts[event.target.value];
}

const saveAddressSchema = async (values: any, actions: any) => {
    try {
        const response = await axios.post(`${store.url}/account/saveUserAddress`, {
            email: store.getUser(),
            ...values
        });

        if (response.data.status === 'Success') {
            store.setAddress(response.data.data);
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
        <ProfileSidebar side-bar="address" />
        <div class="d-flex flex-column col-md-10 col-sm-9 col-10 offset-sm-0 offset-1 ps-md-5 ps-sm-4 ps-0 pt-sm-0 pt-4 dataGroup">
            <Form @submit="saveAddressSchema" :validation-schema="addressSchema"
                    :initial-values="addressSchemaInitialValues" class="form-group">
                <legend>Shipping Address</legend>
                <div class="row">
                    <div class="col">
                        <label for="building_name" class="col-form-label py-1">Building Address</label>
                        <Field class="form-control" placeholder="Building Address"
                            aria-label="Building Address" name="building_name" />
                        <ErrorMessage name="building_name" class="text-danger" as="p" />
                    </div>
                    <div class="col">
                        <label for="street_name" class="col-form-label py-1">Street Name</label>
                        <Field class="form-control" placeholder="Street Name" 
                            aria-label="Street Name" name="street_name" />
                        <ErrorMessage name="street_name" class="text-danger" as="p" />
                    </div>
                </div>
                <div class="row pt-3">
                    <div class="col">
                        <label for="landmark" class="col-form-label py-1">Landmark</label>
                        <Field class="form-control" placeholder="Landmark" 
                            aria-label="Landmark" name="landmark" />
                        <ErrorMessage name="landmark" class="text-danger" as="p"/>
                    </div>
                    <div class="col">
                        <label for="town_city" class="col-form-label py-1">Town/City</label>
                        <Field class="form-control" placeholder="Town/City" 
                            aria-label="Town/City" name="town_city" />
                        <ErrorMessage name="town_city" class="text-danger" as="p"/>
                    </div>
                </div>
                <div class="row pt-3">
                    <div class="col">
                        <label for="state" class="col-form-label py-1">State</label>
                        <Field as="select" name="state" class="form-control" :onchange="onStateChange">
                            <option value="" selected>Select State</option>
                            <option v-for="state in states" :key="state" 
                                :value="state">{{ state }}</option>
                            <option disabled class="bg-dark text-light">
                                UNION Territories</option>
                            <option v-for="unionState in unionStates" :key="unionState" 
                                :value="unionState">{{ unionState }}</option>
                        </Field>
                        <ErrorMessage name="state" class="text-danger" as="p" />
                    </div>
                    <div class="col">
                        <label for="district" class="col-form-label py-1">District</label>
                        <Field as="select" name="district" class="form-control">
                            <option value="" selected>Select District</option>
                            <option v-for="district in districts" :key="district" 
                                :value="district">{{ district }}</option>
                        </Field>
                        <ErrorMessage name="district" class="text-danger" as="p" />
                    </div>
                </div>
                <div class="row pt-4">
                    <div class="col">
                        <button class="btn btn-dark">Save</button>
                    </div>
                </div>
            </Form>
        </div>
    </div>
</template>