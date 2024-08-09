import axios from 'axios';

// Create an Axios instance with a default configuration
const api = axios.create({
    baseURL: 'http://localhost:8000', // Base URL for the FastAPI server
});

// Function to fetch all todos
export const getTodos = () => api.get('/todos/');

// Function to create a new todo
export const createTodo = (todo) => api.post('/todos/', todo);

// Function to delete a todo by its ID
export const deleteTodo = (id) => api.delete(`/todos/${id}`);

// Function to update a todo by its ID
export const updateTodo = (id, todo) => api.put(`/todos/${id}`, todo);
