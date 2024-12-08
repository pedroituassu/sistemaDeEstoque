import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
      <header className="header">
          <div className="flex justify-left bg-blue-50">
              <div className="flex justify-center">
                  <Link
                      to="/"
                      className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                  >
                      Início
                  </Link>
              </div>
              <div className="flex justify-center">
                  <Link
                      to="/list-products"
                      className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                  >
                      Produtos
                  </Link>
              </div>
              <div className="flex justify-center">
                  <Link
                      to="/create-product"
                      className="bg-blue-50 text-black px-6 py-3 hover:bg-blue-600 hover:text-white transition"
                  >
                      Criar Produto
                  </Link>
              </div>
          </div>
      </header>
  );
};

export default Header;
