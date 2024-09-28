<template>
    <div>
        <div v-if="error">error - {{ error }}</div>
        <div v-else-if="pending">pending ... </div>

        <div v-else="products">
            <LazyProducts :products="products" />
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import useFetchProducts from '~/composables/useFetchProducts';

// Ensure you have all the necessary imports
const { products, pending, error, fetchAllProducts } = useFetchProducts()
// console.log('index page' products);
// Fetch all products when the component is mounted
onMounted(() => {
    fetchAllProducts()
});

</script>