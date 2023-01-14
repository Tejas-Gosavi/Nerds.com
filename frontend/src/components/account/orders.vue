<script setup lang="ts">
import ProfileSidebar from '../common/profileSidebar.vue';

const orders: any[] = [];
</script>

<template>
    <div class="row">
        <ProfileSidebar side-bar="orders" />
        <div class="col-md-10 col-sm-9 col-10 offset-sm-0 offset-1 d-flex flex-column ps-md-5 ps-sm-4 ps-0 pt-sm-0 pt-4 dataGroup">
            <legend>Orders</legend>
            <template v-if="orders.length == 0">
                <p class="text-center">Nothing here <i class="bi bi-emoji-frown"></i></p>
            </template>
            <template v-else>
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Order ID</th>
                                <th scope="col">Payment ID</th>
                                <th scope="col">Total</th>
                                <th scope="col">Delivery Charges</th>
                                <th scope="col">Payment Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- {% for order in orders %}
                            <tr>
                                <td>{{ forloop.counter }}</td>
                                <td> <a href="{{ order.get_absolute_url }}"
                                        style="text-decoration: none; color: #0275d8;">{{ order.order_id }}</a></td>
                                <td>{{ order.payment_id }}</td>
                                <td>{{ order.total }}</td>
                                <td>{{ order.delivery_charges }}</td>
                                {% if order.payment_status == 1 %}
                                <td> <i class="bi bi-circle-fill text-warning"></i></td>
                                {% elif order.payment_status == 2 %}
                                <td><i class="bi bi-circle-fill text-success"></i></td>
                                {% else %}
                                <td><i class="bi bi-circle-fill text-danger"></i></td>
                                {% endif %}
                            </tr>
                            {% endfor %} -->
                        </tbody>
                    </table>
                </div>
            </template>
        </div>
    </div>
</template>