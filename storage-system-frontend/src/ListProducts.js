import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "./Header";

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/products/");
        setProducts(response.data);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <Header />
      <div className="min-h-screen flex flex-col items-center gap-y-8 bg-blue-50">
        <h1 className="text-3xl font-bold my-6">Produtos</h1>
        {products.length > 0 ? (
            <div>
            {products.map((product, index) => (
                <div
                    className="w-auto max-w-4xl grid items-start bg-white p-6 rounded-lg shadow-lg mb-3 grid-cols-3 grid-rows-3"
                    key={index}>
                  <div className="italic col-span-3">
                    {product.category}
                  </div>
                  <div className="text-2xl font-bold mb-0 col-span-2 pr-30">
                    {product.name}
                  </div>
                  <div>
                    <b>Vencimento: </b>{product.expirationTime} dias
                  </div>
                  <div className="text-xl italic mb-1 col-span-2">
                    {product.brand}
                  </div>
                  <div>
                    <b>Min - Max: </b>{product.minSupply} - {product.maxSupply}
                  </div>
                </div>
            ))
            }
            </div>
        ) : (
            <p className="text-center text-gray-500">Nenhum produto encontrado.</p>
        )}
      </div>
    </div>
  );
};

export default ProductList;
