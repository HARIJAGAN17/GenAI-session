import { useState } from "react";
import api from "./api";

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  const fetchTodos = async () => {
    try {
      const response = await api.get('/recommendation');
      setTodos(response.data.response);
      console.log(todos);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>Todo List</h2>
      <button onClick={fetchTodos}>Generate Todos</button>
      <ul style={{ listStyleType: "none", padding: 0 }}>
        {todos.map((todo, index) => (
          <li key={index} style={{ margin: "10px 0", background: "#f4f4f4", padding: "10px", borderRadius: "5px" }}>
            {todo.trim()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
