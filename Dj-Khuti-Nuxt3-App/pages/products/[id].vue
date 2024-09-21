<template>
    <div>
        <h1>Product id page here.</h1>
        <div v-if="pending">Loading post...</div>
        <div v-else-if="error">Error: {{ error.message }}</div>
        <div v-else="Product">
            <LazyProductdetail :product="product" />
        </div>
    </div>
</template>

<script setup>
definePageMeta({
    layout: 'custom'
})

import { ref, onMounted } from 'vue'
import useFetchProducts from '~/composables/useFetchProducts';

const { fetchSingleProduct, pending, error } = useFetchProducts()
const route = useRoute()
const product = ref(null)

onMounted(async () => {
    const productId = route.params.id // Get the post ID from the route
    product.value = await fetchSingleProduct(productId) // Fetch the single post
})
</script>

<style scoped></style>