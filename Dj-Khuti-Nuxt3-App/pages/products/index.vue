<template>
    <div>
        <div v-if="error">error - {{ error }}</div>
        <div v-else-if="pending">pending ... </div>

        <div v-else="products">
            <div>
                <div>
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4">
                                <div class="p-4 md:w-1/3 sm:mb-0 mb-6" v-for="product in products.results" :key="product.id">
                                    <div class="rounded-lg h-64 overflow-hidden">
                                        <NuxtImg v-if="product?.image" :src="product.image"
                                            class="object-cover object-cover h-full w-full" loading="lazy" />
                                    </div>
                                    <h2 class="text-xl font-medium title-font text-gray-900 mt-5">Shooting Stars</h2>
                                    <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                        <NuxtLink :to="{ name: 'products-id', params: { id: product.id } }">
                                            {{ product.name }} - {{ product.id }}
                                        </NuxtLink>
                                    </h2>
                                    <a class="text-indigo-500 inline-flex items-center mt-3">Learn More
                                        <svg fill="none" stroke="currentColor" stroke-linecap="round"
                                            stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2"
                                            viewBox="0 0 24 24">
                                            <path d="M5 12h14M12 5l7 7-7 7"></path>
                                        </svg>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
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