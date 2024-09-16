<template>

    <div v-if="error">
        <h1>error ... {{ error }}</h1>
    </div>
    <div v-else-if="pending">
        <h1>Loading...</h1>
    </div>
    <div v-else="post">
        <LazyPostdetail :post="post" />
        <!-- single post here - {{ post }} -->
    </div>
    <!-- <h2>child -- {{ props.child }}</h2> -->
</template>

<script setup>


// const child = useAttrs().child
// console.log('child from parents', useAttrs.child);

// const props = defineProps(['child'])



definePageMeta({
    layout: 'custom'
})
// import { ref } from 'vue'
const route = useRoute();
// Fetching the data using useLazyAsyncData
const { data: post, pending, error } = await useLazyAsyncData(() => $fetch(`/api/posts/${route.params.id}`))

</script>

<style scoped></style>