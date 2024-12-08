import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home";
import CreateProduct from "./CreateProduct";
import ListProducts from "./ListProducts";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create-product" element={<CreateProduct />} />
        <Route path="/list-products" element={<ListProducts />} />
      </Routes>
    </Router>
  );
}

export default App;
