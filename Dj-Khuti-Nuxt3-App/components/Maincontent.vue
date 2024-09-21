<template>
    <div>
        <section class="text-gray-600 body-font overflow-hidden">
            <div class="container px-5 py-24 mx-auto">
                <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                    <div class="py-8 flex flex-wrap md:flex-nowrap">
                        <div class="block relative h-48 rounded overflow-hidden px-8">
                            <NuxtImg :src="post.image" alt="Image-Not-Found" loading="lazy" class="h-full w-full" />
                        </div>
                        <div class="md:flex-grow">
                            <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                <NuxtLink :to="{ name: 'posts-id', params: { id: post.id } }">
                                    {{ post.title }} - {{ post.id }}
                                </NuxtLink>
                            </h2>
                            <p>{{ post.description.slice(0, 200) }} ...</p>
                            <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
                                    fill="none" stroke-linecap="round" stroke-linejoin="round">
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
</template>

<script setup>
defineProps(['posts'])
</script>

<style scoped></style>
