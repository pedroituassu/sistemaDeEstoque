import React, { useState } from "react";
import axios from "axios";
import Header from "./Header";

const CreateProduct = () => {
  const [product, setProduct] = useState({
    name: "",
    expirationTime: "",
    minSupply: "",
    maxSupply: "",
    category: "",
    brand: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProduct((prevProduct) => ({
      ...prevProduct,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/products/", product);
      alert("Product created: " + response.data.product.name);
    } catch (error) {
      alert("Error creating product: " + error.message);
    }
  };

  return (
    <div>
      <Header/>
      <div className="min-h-screen flex items-center justify-center bg-blue-50">
        <div className="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
          <h1 className="text-2xl font-bold mb-6">Criar novo produto</h1>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium">Nome:</label>
              <input
                type="text"
                name="name"
                value={product.name}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border rounded-lg"
              />
            </div>

            <div>
              <label className="block text-sm font-medium">Tempo de vencimento:</label>
              <input
                type="number"
                name="expirationTime"
                value={product.expirationTime}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border rounded-lg"
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium">Quantidade mínima:</label>
                <input
                  type="number"
                  name="minSupply"
                  value={product.minSupply}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-2 border rounded-lg"
                />
              </div>
              <div>
                <label className="block text-sm font-medium">Quantidade máxima:</label>
                <input
                  type="number"
                  name="maxSupply"
                  value={product.maxSupply}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-2 border rounded-lg"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium">Categoria:</label>
              <input
                type="text"
                name="category"
                value={product.category}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border rounded-lg"
              />
            </div>

            <div>
              <label className="block text-sm font-medium">Marca:</label>
              <input
                type="text"
                name="brand"
                value={product.brand}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border rounded-lg"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
            >
              Create Product
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default CreateProduct;
