import { useState } from "react";
import api from "./api";
import "./gpt_image.css";

const GptImage = () => {
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setDescription("");
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const response = await api.post("/describe-image", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setDescription(response.data.description);
    } catch (error) {
      console.error("Error uploading image:", error);
      setDescription("Failed to get description.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="gpt-image-container">
      <h2>GPT Image Description</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file || loading}>
        {loading ? "Describing..." : "Upload & Describe"}
      </button>
      {description && (
        <div className="description-box">
          <h3>Description:</h3>
          <p>{description}</p>
        </div>
      )}
    </div>
  );
};

export default GptImage;
