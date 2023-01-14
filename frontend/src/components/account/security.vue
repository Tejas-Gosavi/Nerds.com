<script setup lang="ts">
import { Form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import ProfileSidebar from '../common/profileSidebar.vue';

const changePasswordSchema = yup.object({
    oldPassword: yup.string().required('Old password is required').min(1),
    newPassword: yup.string().required('New password is required').min(1),
    newPassword2: yup.string().required('New password is required').oneOf([
        yup.ref('newPassword')
    ], 'Both Passwords do not match')
})

function saveChangePassword(values: any, actions: any) {
    alert(JSON.stringify(values, null, 2));
}
</script>

<template>
    <div class="row">
        <ProfileSidebar side-bar="security" />
        <div class="d-flex flex-column col-md-10 col-sm-9 col-10 offset-sm-0 offset-1 ps-md-5 ps-sm-4 ps-0 pt-sm-0 pt-4 dataGroup">
            <Form @submit="saveChangePassword" :validation-schema="changePasswordSchema" class="form-group">
                <legend>Change Password</legend>
                <div class="row">
                    <div class="col">
                        <label for="oldPassword" class="col-form-label py-1">Old Password</label>
                        <Field class="form-control" placeholder="Old Password" 
                            aria-label="Old Password" name="oldPassword" />
                        <ErrorMessage name="oldPassword" class="text-danger" as="p"/>
                    </div>
                </div>
                <div class="row pt-3">
                    <div class="col">
                        <label for="newPassword" class="col-form-label py-1">New Password</label>
                        <Field class="form-control" placeholder="New Password" 
                            aria-label="New Password" name="newPassword" />
                        <ErrorMessage name="newPassword" class="text-danger" as="p"/>
                    </div>
                    <div class="col">
                        <label for="newPassword2" class="col-form-label py-1">Retype New Password</label>
                        <Field class="form-control" placeholder="Retype New Password"
                            aria-label="Retype New Password" name="newPassword2" />
                        <ErrorMessage name="newPassword2" class="text-danger" as="p"/>
                    </div>
                </div>
                <div class="row pt-4">
                    <div class="col">
                        <button class="btn btn-dark" type="submit">Save</button>
                    </div>
                </div>
            </Form>
            <div class="form-group mt-5">
                <legend>Delete Account</legend>
                <div class="row">
                    <label>Are you sure you want to delete your account?</label>
                    <div class="col py-3">
                        <button class="btn btn-outline-danger">Delete</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>