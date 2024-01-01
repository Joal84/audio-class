//import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import FirstPage from "./components/first-page";
import SecondPage from "./components/second-page";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<FirstPage />} />
        <Route path="/listening" element={<SecondPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
