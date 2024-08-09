import React, { useState } from 'react';

const TodoForm = ({ addTodo }) => {
    // State to manage the title of the todo
    const [title, setTitle] = useState('');
    // State to manage the description of the todo
    const [description, setDescription] = useState('');
    // State to manage error messages
    const [error, setError] = useState('');

    // Function to handle form submission
    const handleSubmit = (e) => {
        e.preventDefault(); // Prevent default form submission behavior
        // Check if title or description is empty
        if (!title.trim() || !description.trim()) {
            setError('Title and description cannot be empty.');
            return;
        }
        // Call addTodo with the new todo
        addTodo({ title, description });
        // Reset form fields and error message
        setTitle('');
        setDescription('');
        setError('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="title">Title</label>
                {/* Input for the title */}
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                />
            </div>
            <div>
                <label htmlFor="description">Description</label>
                {/* Input for the description */}
                <input
                    type="text"
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Description"
                />
            </div>
            <button type="submit">Add Todo</button>
            {/* Display error message if there's an error */}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
    );
};

export default TodoForm;
