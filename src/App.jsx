//import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import FirstPage from "./components/FirstPage";
import SecondPage from "./components/SecondPage";
function App() {
  //const [data, setData] = useState({});
  /*
  useEffect(() => {
    fetch("http://127.0.0.1:5000/members")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => console.log(data));
  }, []);
*/
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
