import React, { useState } from 'react';

const TodoItem = ({ todo, deleteTodo, updateTodo }) => {
    // State for managing edit mode
    const [isEditing, setIsEditing] = useState(false);
    // State for holding edited title
    const [editedTitle, setEditedTitle] = useState(todo.title);
    // State for holding edited description
    const [editedDescription, setEditedDescription] = useState(todo.description);
    // State for showing the completed message
    const [showCompletedMessage, setShowCompletedMessage] = useState(false);

    // Function to handle toggling the completion status
    const handleToggle = () => {
        const newCompletedStatus = !todo.completed;
        updateTodo(todo.id, { ...todo, completed: newCompletedStatus });
        setShowCompletedMessage(newCompletedStatus);
    };

    // Function to handle saving the edited todo
    const handleSave = () => {
        updateTodo(todo.id, {
            ...todo,
            title: editedTitle,
            description: editedDescription
        });
        setIsEditing(false);
    };

    // Function to handle canceling the edit
    const handleCancel = () => {
        setEditedTitle(todo.title);
        setEditedDescription(todo.description);
        setIsEditing(false);
    };

    return (
        <div className='todo-item'>
            {isEditing ? (
                <div className='edit-form'>
                    {/* Edit Form */}
                    <label>
                        Title:
                        <input
                            type="text"
                            value={editedTitle}
                            onChange={(e) => setEditedTitle(e.target.value)}
                        />
                    </label>
                    <label>
                        Description:
                        <textarea
                            value={editedDescription}
                            onChange={(e) => setEditedDescription(e.target.value)}
                        />
                    </label>
                    <div className='edit-form-buttons'>
                        <button onClick={handleSave}>Save</button>
                        <button onClick={handleCancel}>Cancel</button>
                    </div>
                </div>
            ) : (
                <div>
                    {/* Display Todo Item */}
                    <h3>{todo.title}</h3>
                    <p>{todo.description}</p>
                    <div className='todo-buttons'>
                        <button onClick={() => deleteTodo(todo.id)}>Delete</button>
                        <button onClick={handleToggle}>
                            {todo.completed ? 'Mark as Incomplete' : 'Mark as Complete'}
                        </button>
                        <button onClick={() => setIsEditing(true)}>Edit</button>
                    </div>
                    {showCompletedMessage && <p className='completed-message'>Task completed!</p>}
                </div>
            )}
        </div>
    );
};

export default TodoItem;
