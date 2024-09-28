<template>
    <Editor api-key="your-api-key" :init="{
        height: 500,
        menubar: false,
        plugins: 'code image link media table',
        toolbar: false,
        content_css: 'default'
    }" :value="description" disabled="true" />
</template>

<script setup>
import { Editor } from '@tinymce/tinymce-vue';
defineProps({
    description: {
        type: String,
        required: true
    }
});
</script>

<style scoped></style>