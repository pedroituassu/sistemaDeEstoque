import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "./Header";
import {useNavigate} from "react-router-dom";

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/products/");
        setProducts(response.data);
      } catch (error) {
        console.error("Erro ao buscar produtos:", error);
      }
    };
    fetchProducts();
  }, []);


  const navigate = useNavigate();

  const editProduct = (product_hash) => {
    navigate(`/edit-product/${product_hash}`); // Navigate to the edit page with hash
  };

  const deleteProduct = async (product_hash) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/products/${product_hash}`);
      alert(`Produto deletado com sucesso!`);
      setProducts(products.filter((product) => product.hash !== product_hash));
    } catch (error) {
      console.error("Erro ao deletar produto:", error);
      alert("Falha ao deletar produto. Tente novamente.");
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen flex flex-col items-center gap-y-8 bg-blue-50">
        <h1 className="text-3xl font-bold my-6">Produtos</h1>
        {products.length > 0 ? (
            <div className="min-w-635px">
              {products.map((product, index) => (
                  <div
                      className="grid items-start bg-gray-50 p-6 rounded-lg shadow-lg mb-3 grid-cols-3 grid-rows-4 hover:bg-white hover:scale-105 transition duration-300 ease-in-out"
                      key={index}>
                    <div className="italic col-span-1">
                      {product.category}
                    </div>
                    <div className="col-start-4 flex flex-row justify-end">
                      <div
                          className="bg-blue-500 text-white text-center px-3 py-1 rounded-lg hover:bg-blue-600 transition col-start-3 mx-1"
                          onClick={() => editProduct(product.hash)}
                      >
                        Editar
                      </div>
                      <div
                          className="bg-red-500 text-white text-center px-3 py-1 rounded-lg hover:bg-red-600 transition mx-1"
                          onClick={() => deleteProduct(product.hash)}
                      >
                        Excluir
                      </div>
                    </div>

                    <div className="text-2xl font-bold mb-0 col-span-2 pr-30">
                      {product.name}
                    </div>
                    <div className="col-start-4 mt-2">
                      <b>Peso unitário: </b>{product.unitWeight} g
                    </div>
                    <div className="text-xl italic mb-1 col-span-2">
                      {product.brand}
                    </div>
                    <div className="col-start-4 mt-1">
                      <b>Vencimento: </b>{product.expirationTime} dias
                    </div>
                    <div className="text-[12px] text- italic col-span-3">
                      {product.hash}
                    </div>
                    <div>
                      <b>Min - Max: </b>{product.minSupply} - {product.maxSupply}
                    </div>
                  </div>
              ))
              }
              <div
                  className="justify-center w-fit bg-red-500 text-white text-center px-3 py-1 rounded-lg hover:bg-red-600 transition mx-1">
                Criar novo produto
              </div>
            </div>

        ) : (
            <div className="flex flex-col items-center">
              <p className="text-center text-gray-500">Nenhum produto encontrado.</p>
              <p><a href="/create-product" className="text-center text-sky-500">Criar um produto</a></p>
            </div>
        )}
      </div>
    </div>
  );
};

export default ProductList;
