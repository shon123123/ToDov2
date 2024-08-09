import React, { useEffect, useState } from 'react';
import { createTodo, deleteTodo, getTodos, updateTodo } from '../api';
import TodoForm from './TodoForm';
import TodoItem from './TodoItems';

const TodoList = () => {
    // State to hold the list of todos
    const [todos, setTodos] = useState([]);

    // useEffect to fetch todos when the component mounts
    useEffect(() => {
        fetchTodos();
    }, []);

    // Function to fetch todos from the API
    const fetchTodos = async () => {
        const response = await getTodos();
        setTodos(response.data);
    };

    // Function to add a new todo
    const addTodo = async (todo) => {
        const response = await createTodo(todo);
        setTodos([...todos, response.data]);
    };

    // Function to delete a todo by id
    const removeTodo = async (id) => {
        await deleteTodo(id);
        setTodos(todos.filter((todo) => todo.id !== id));
    };

    // Function to update a todo by id
    const editTodo = async (id, todo) => {
        const response = await updateTodo(id, todo);
        setTodos(todos.map((t) => (t.id === id ? response.data : t)));
    };

    return (
        <div>
            {/* Form component to add new todos */}
            <TodoForm addTodo={addTodo} />
            {/* Map over todos and render each TodoItem component */}
            {todos.map((todo) => (
                <TodoItem
                    key={todo.id}
                    todo={todo}
                    deleteTodo={removeTodo}
                    updateTodo={editTodo}
                />
            ))}
        </div>
    );
};

export default TodoList;
