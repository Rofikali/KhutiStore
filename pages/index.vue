<!-- Error Handling -->
<!-- Displaying Posts -->
<!-- <div v-if="posts">
    <LazyMaincontent :posts="posts.results" />
</div> -->

<template>
    <div>
        <div v-if="error">error - {{ error }}</div>
        <div v-else-if="pending">pending ... </div>

        <div v-if="posts">
            <LazyMaincontent :posts="posts.results" :pending="pending" />
        </div>
        <!-- dta {{ posts }} -->
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import useFetchPosts from '~/composables/useFetchPosts';

// Ensure you have all the necessary imports
const { posts, pending, error, fetchAllPosts } = useFetchPosts()
// console.log('index page' posts);
// Fetch all posts when the component is mounted
onMounted(() => {
    fetchAllPosts()
});

</script>