import React, { useState, useEffect } from "react";
import css from "./soundsDetected.module.css";
import axios from "axios";

function SoundsDetected() {
  const [soundList, setSoundList] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/sounds");
      setSoundList(response.data);
    } catch (error) {
      console.error(error);
    } finally {
      // After each response, make the next request.
      fetchData();
    }
  };

  return (
    <ul>
      {soundList.map((sound, index) => (
        <li key={index} className={css["sound" + index]}>
          {sound}
        </li>
      ))}
    </ul>
  );
}

export default SoundsDetected;
