<script setup lang="ts">
import { onBeforeMount } from 'vue';
import router from '@/router';
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import axios from 'axios';
import { useNerdsStore } from '@/stores/index';

const store = useNerdsStore();

onBeforeMount(() => {
    if (store.isUserLoggedIn()) {
        router.push('profile');
    }
});

const logInSchema = yup.object({
	email: yup.string().required('Email is required').email(),
	password: yup.string().required('Password is required').min(1).default('a'),
});

const onLogin = async (values: any, actions: any) => {
    try {
        const response = await axios.post(`${store.url}/account/userLogin`, {
            email: values.email, password: values.password
        });

        if (response.data.status === 'Success') {
            // const e = document.getElementById('alert');
            // if(e) {
            //     e.hidden = false;
            // }
            store.setUser(true, { ...response.data.data });
        } else {
            if (response.data.code == 1) {
                actions.setFieldError('email', 'Wrong Email');
            } else if(response.data.code == 2) {
                actions.setFieldError('password', 'Wrong Password');
            } else {
                actions.setFieldError('email', 'Account is deleted or not activated');
            }
        }
    } catch (error) {
        console.error(error);
    }
}

const signUpSchema = yup.object({
	email: yup.string().required('Email is required').email(),
	password: yup.string().required('Password is required').min(1),
	password2: yup.string().required('Password is required').oneOf([
        yup.ref('password')
    ], 'Both Passwords do not match')
});

function onSignup(values: any, actions: any) {
	actions.setFieldError('email', 'this email is already taken 2');
  	// alert(JSON.stringify(values, null, 2));
}
</script>

<template>
    <div class="container pt-3">
        <div class="row">
            <div class="col-lg-3 col-md-2 col-2"></div>
            <div class="col-lg-6 col-md-8">
                <div class="accordion" id="accordionExample">
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                Log in
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <Form @submit="onLogin" :validation-schema="logInSchema" class="form-group">
                                    <div class="form-floating mb-3">
                                        <Field type="email" class="form-control" name="email"
                                            placeholder="tom@hardy.com" />
                                        <label for="floatingInput">Email address</label>
										<ErrorMessage name="email" class="text-danger" as="p"/>
                                    </div>
                                    <div class="form-floating">
                                        <Field type="password" class="form-control" name="password"
                                            placeholder="Password" />
                                        <label for="floatingPassword">Password</label>
										<ErrorMessage name="password" class="text-danger" as="p"/>
                                    </div>
                                    <button class="btn btn-primary w-100 mt-3" type="submit">Log
                                        in</button>
								</Form>
                            </div>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingTwo">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                Create account
                            </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                            data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <Form @submit="onSignup" :validation-schema="signUpSchema" class="form-group">
                                    <div class="form-floating mb-3">
                                        <Field type="email" class="form-control" name="email"
                                            placeholder="tom@hardy.com" />
                                        <label for="floatingInput">Email address</label>
										<ErrorMessage name="email" class="text-danger" as="p"/>
                                    </div>
                                    <div class="form-floating mb-3">
                                        <Field type="password" class="form-control" name="password"
                                            placeholder="Password" />
                                        <label for="floatingPassword">Password</label>
										<ErrorMessage name="password" class="text-danger" as="p"/>
                                    </div>
                                    <div class="form-floating">
                                        <Field type="password" class="form-control" name="password2"
                                            placeholder="Repeat Password" />
                                        <label for="floatingPassword">Repeat Password</label>
										<ErrorMessage name="password2" class="text-danger" as="p"/>
                                    </div>
                                    <button class="btn btn-primary w-100 mt-3" type="submit">Create
                                        account</button>
								</Form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-2 col-2"></div>
        </div>
    </div>
</template>
