<script setup>
definePageMeta({
    layout: 'custom'
})

// Import necessary functions from Vue/Nuxt
import { ref, computed } from 'vue'

// Fetch all posts
const { data: allPosts, status: allPostsStatus, error: allPostsError } = useLazyFetch(() => 'api/posts', {
    immediate: true
})
// console.log('all posts', allPosts);
// const id = ref(1);

// Track loading states
const allPostsPending = computed(() => allPostsStatus.value === 'pending');
</script>

<template>
    <div>
        <div style="display: flex;">
            <div style="flex: 1;">
                <h2>All Posts Index Page here, ---------->>>>>>>>>>>>>>>>>>>>>>>>></h2>
                <section class="text-gray-600 body-font overflow-hidden">
                    <div class="container px-5 py-24 mx-auto">
                        <div v-if="allPostsPending">
                            Loading all posts...
                        </div>
                        <div v-else-if="allPosts && allPosts.results">
                            <div v-for="post in allPosts.results" :key="post.id"
                                class="-my-8 divide-y-2 divide-gray-100">
                                <div class="py-8 flex flex-wrap md:flex-nowrap">
                                    <a class="block relative h-48 rounded overflow-hidden px-8">
                                        <!-- <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                            :src="post.image"> -->
                                        <NuxtImg :src=post.image loading="lazy" />
                                    </a>
                                    <div class="md:flex-grow">
                                        <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                            <NuxtLink :to="{ name: 'postsall-id', params: { id: post.id } }">
                                                {{ post.title }}
                                            </NuxtLink>
                                        </h2>
                                        <p>{{ post.description.slice(0, 200) }} ...</p>
                                        <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                            <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor"
                                                stroke-width="2" fill="none" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M5 12h14"></path>
                                                <path d="M12 5l7 7-7 7"></path>
                                            </svg>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-else>
                            <p>No posts found.</p>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Single Post Section -->
            <div style="flex: 1;">
                <!-- <div v-if="singlePostStatus === 'success' && singlePost"> -->
                <h1>success is there </h1>
                <div>
                    <NuxtPage />
                    <!-- postsall-id is a routeview , iam passing this as a routeview name but not  working  -->
                </div>
            </div>
        </div>
    </div>
</template>
