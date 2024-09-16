<template>
    <div>
        <div v-if="error">error - {{ error }}</div>
        <div v-else-if="pending">pending ... </div>

        <div v-else="products">
            <!-- <LazyMaincontent :posts="posts.results" :pending="pending" /> -->
            <!-- products {{ products.results }} -->
            <!-- <br><br><br> -->
            <!-- products {{ products }} -->
            <div>
                <section class="text-gray-600 body-font overflow-hidden">
                    <div class="container px-5 py-24 mx-auto">
                        <div v-for="post in products.results" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                            <div class="py-8 flex flex-wrap md:flex-nowrap">
                                <a class="block relative h-48 rounded overflow-hidden px-8">
                                    <!-- <NuxtImg :src="post.image" alt="Image-Not-Found" /> -->
                                    <!-- <NuxtImg :src="post.image" alt="Image-Not-Found" loading="lazy" /> -->

                                </a>
                                <div class="md:flex-grow">
                                    <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                        <NuxtLink :to="{ name: 'posts-id', params: { id: post.id } }">
                                            {{ post.name }} - {{ post.id }}
                                        </NuxtLink>
                                    </h2>
                                    <p>{{ post.description }} ...</p>
                                    <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                        <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor"
                                            stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M5 12h14"></path>
                                            <path d="M12 5l7 7-7 7"></path>
                                        </svg>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
        <!-- dta {{ posts }} -->
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import useFetchProducts from '~/composables/useFetchProducts';

// Ensure you have all the necessary imports
const { products, pending, error, fetchAllProducts } = useFetchProducts()
// console.log('index page' posts);
// Fetch all posts when the component is mounted
onMounted(() => {
    fetchAllProducts()
});

</script>