<template>
    <div v-if="pending">Loading post...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <div v-else="post">
        <LazyPostsSingle :post="post" />
    </div>
</template>

<script setup>
definePageMeta({
    layout: 'custom'
})

import { ref, onMounted } from 'vue'
import useFetchPosts from '~/composables/useFetchPosts'

const { fetchSinglePost, pending, error } = useFetchPosts()
const route = useRoute()
const post = ref(null)

onMounted(async () => {
    const postId = route.params.id // Get the post ID from the route
    post.value = await fetchSinglePost(postId) // Fetch the single post
})
</script>