import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home";
import CreateProduct from "./CreateProduct";
import ListProducts from "./ListProducts";
import EditProduct from "./EditProduct";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create-product" element={<CreateProduct />} />
        <Route path="/list-products" element={<ListProducts />} />
        <Route path="/edit-product/:product_hash" element={<EditProduct />} />
      </Routes>
    </Router>
  );
}

export default App;
