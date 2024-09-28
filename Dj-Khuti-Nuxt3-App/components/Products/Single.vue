<template>
    <h1>Product Singel page here.</h1>
    <div>
        <section class="text-gray-600 body-font">
            <div class="container px-5 py-24 mx-auto flex flex-col">
                <div class="lg:w-4/6 mx-auto">
                    <div class="rounded-lg h-64 overflow-hidden">
                        <!-- Check if the product object and image property exist -->
                        <div>
                            <div v-if="pending">Image is coming ...</div>
                            <div v-else>
                                <NuxtImg v-if="product?.image" :src="product.image"
                                    class="object-cover object-cover h-full w-full" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col sm:flex-row mt-10">
                        <div class="sm:w-1/3 text-center sm:pr-8 sm:py-8">
                            <div
                                class="w-20 h-20 m-2 rounded-lg inline-flex items-center justify-center bg-gray-200 text-gray-400">
                                <NuxtImg v-if="product?.image" :src="product.image"
                                    class="object-cover object-cover h-full w-full" loading="lazy" />
                            </div>
                            <div
                                class="w-20 h-20 m-2 rounded-lg inline-flex items-center justify-center bg-gray-200 text-gray-400">
                                <NuxtImg v-if="product?.image" :src="product.image"
                                    class="object-cover object-cover h-full w-full" loading="lazy" />
                            </div>
                            <div
                                class="w-20 h-20 m-2 rounded-lg inline-flex items-center justify-center bg-gray-200 text-gray-400">
                                <NuxtImg v-if="product?.image" :src="product.image"
                                    class="object-cover object-cover h-full w-full" loading="lazy" />
                            </div>
                            <div class="flex flex-col items-center text-center justify-center">
                                <h2 class="font-medium title-font mt-4 text-gray-900 text-lg">
                                    Author - {{ product?.author?.name || 'Unknown Author' }}
                                </h2>
                                <div class="w-12 h-1 bg-indigo-500 rounded mt-2 mb-4"></div>
                                <p class="text-base">Author Email - {{ product?.author?.email || 'No Email Available' }}
                                </p>
                            </div>
                        </div>
                        <div
                            class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
                            <p class="leading-relaxed text-lg mb-4">
                                {{ product?.description ||
                                    'No description available'
                                }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
defineProps(['product', 'pending'])

</script>

<style scoped></style>