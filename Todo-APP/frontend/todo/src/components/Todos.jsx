import { useState } from "react";
import api from "./api";
import './Todo_generate.css';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchTodos = async () => {
    setLoading(true);
    try {
      const response = await api.get('/recommendation');
      setTodos(response.data.response);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="center-wrapper">
      <div className="todo-container">
        <h1 className="todo-title">✨ Daily Todo Recommendations</h1>
        <button className="generate-button" onClick={fetchTodos}>Generate Todos</button>

        {loading ? (
          <div className="loader"></div>
        ) : (
          <div className="todo-grid">
            {todos.map((todo, index) => (
              <div key={index} className="todo-card">
                <strong>Task {index + 1}</strong>
                <p>{todo.trim()}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TodoList;
