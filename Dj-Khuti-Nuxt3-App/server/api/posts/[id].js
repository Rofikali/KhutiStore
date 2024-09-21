// server/routes/posts/[id].ts

import { defineEventHandler } from 'h3'
import axios from 'axios'

export default defineEventHandler(async (event) => {
    const { id } = event.context.params
    console.log('what is inside id', id)

    if (!id) {
        return { error: 'Post ID is required' }
    }

    try {
        // Fetch a single post by ID from Django backend
        const response = await axios.get(`http://127.0.0.1:8000/posts/${id}`)

        // Return the post data
        return response.data
    } catch (error) {
        // Handle errors
        return { error: 'Failed to fetch post details' }
    }
})
