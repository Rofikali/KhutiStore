// import { ref } from 'vue'
// import { useFetch } from '#app'

// export function useFetchProducts() {
//     const products = ref([])
//     const product = ref(null)

//     const fetchAllProducts = async () => {
//         try {
//             const { data } = await useFetch('/api/products')
//             products.value = data.value
//         } catch (error) {
//             console.error('Error fetching products:', error)
//         }
//     }

//     const fetchProductById = async (id: string) => {
//         try {
//             const { data } = await useFetch(`/api/products/${id}`)
//             product.value = data.value
//         } catch (error) {
//             console.error('Error fetching product:', error)
//         }
//     }

//     return {
//         products,
//         product,
//         fetchAllProducts,
//         fetchProductById,
//     }
// }



// composables/useFetchPosts.ts
export default function useFetchPosts() {
    // Fetch all posts using useLazyAsyncData
    const { pending, data: products, error, refresh } = useLazyAsyncData('posts-data', () =>
        $fetch('/api/products') // Make sure the path is absolute by starting with a "/"
    );

    // Method to manually refresh posts data (fetch all posts)
    const fetchAllProducts = async () => {
        try {
            console.log('Refreshing posts data...');
            await refresh(); // Trigger a re-fetch of the data
            console.log('products:', products.value);
        } catch (err) {
            console.log('Error fetching posts:', err);
        }
    };

    // Method to fetch a single post by ID
    const fetchSingleProduct = async (id) => {
        try {
            console.log(`Fetching single post with ID: ${id}`);
            const singlePost = await $fetch(`/api/posts/${id}`); // Ensure this path is also absolute
            console.log('Single Post:', singlePost);
            return singlePost; // Return the fetched single post
        } catch (err) {
            console.log('Error fetching single post:', err);
            throw err; // Handle the error appropriately
        }
    };

    return {
        products,
        pending,
        error,
        fetchAllProducts, // Fetch all posts
        fetchSingleProduct, // Fetch a single post by ID
    };
}
