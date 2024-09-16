// // server/api/hello.ts

// import { defineEventHandler } from 'h3'
// import axios from 'axios'

// export default defineEventHandler(async (event) => {
//     try {
//         // Fetch data from the Django backend
//         const response = await axios.get('http://127.0.0.1:8000/posts?limit=100')
//         // const response = await axios.get('http://127.0.0.1:8000/posts')

//         // Return the data to the frontend
//         // console.log('response from server', response.data);
//         // console.log('only reslults', response.data.results[0]);
//         return response.data
//     } catch (error) {
//         // Handle errors
//         return { error: 'Failed to fetch posts' }
//     }
// })

// server/api/hello.ts
import { defineEventHandler } from 'h3';
import axios from 'axios';

export default defineEventHandler(async (event) => {
    try {
        // Fetch data from the Django backend
        const response = await axios.get('http://127.0.0.1:8000/posts?limit=100');

        // Check if response status is OK
        if (response.status === 200) {
            // Return the data to the frontend
            return response.data;
        } else {
            // Handle non-200 responses
            return { error: `Error fetching posts. Status code: ${response.status}` };
        }
    } catch (error) {
        // Handle network or server errors
        console.error('Error fetching posts from Django backend:', error);
        return { error: 'Failed to fetch posts. Please check your server.' };
    }
});
