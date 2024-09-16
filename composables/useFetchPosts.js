

// composables/useFetchPosts.ts
export default function useFetchPosts() {
    // Fetch all posts using useLazyAsyncData
    const { pending, data: posts, error, refresh } = useLazyAsyncData('posts-data', () =>
        $fetch('/api/posts') // Make sure the path is absolute by starting with a "/"
    );

    // Method to manually refresh posts data (fetch all posts)
    const fetchAllPosts = async () => {
        try {
            console.log('Refreshing posts data...');
            await refresh(); // Trigger a re-fetch of the data
            console.log('Posts:', posts.value);
        } catch (err) {
            console.log('Error fetching posts:', err);
        }
    };

    // Method to fetch a single post by ID
    const fetchSinglePost = async (id) => {
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
        posts,
        pending,
        error,
        fetchAllPosts, // Fetch all posts
        fetchSinglePost, // Fetch a single post by ID
    };
}
