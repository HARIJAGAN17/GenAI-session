import { useState } from "react";
import api from "./api";
import './Todo_generate.css'

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  const fetchTodos = async () => {
    try {
      const response = await api.get('/recommendation');
      setTodos(response.data.response);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="todo-container">
      <h1 className="todo-title">✨ Daily Todo Recommendations</h1>
      <button className="generate-button" onClick={fetchTodos}>Generate Todos</button>

      <div className="todo-grid">
        {todos.map((todo, index) => (
          <div key={index} className="todo-card">
            <strong>Task {index + 1}</strong>
            <p>{todo.trim()}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TodoList;
