    import React from 'react';
    import TodoList from './components/TodoList';

    const App = () => {
        return (
            <div>
                {/* Main application container */}
                <h1>ToDo</h1> {/* Main heading for the todo application */}
                <TodoList /> {/* Component that displays and manages the list of todo items */}
            </div>
        );
    };

    export default App;
