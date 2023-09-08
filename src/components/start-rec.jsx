import css from "./start-rec.module.css";
import { useNavigate } from "react-router-dom";

function StartRec() {
  const navigate = useNavigate();

  const handleClick = async () => {
    try {
      // Make a request to the Flask server's /start endpoint
      await fetch("http://127.0.0.1:8000/start", {
        method: "POST",
      });

      // Redirect the user to the /listening page
      navigate("/listening");
    } catch (error) {
      console.error("Error starting server:", error);
      // Handle any errors that occurred during the request
    }
  };
  return (
    <button className={css.button} onClick={handleClick}>
      Start Listening
    </button>
  );
}
export default StartRec;
