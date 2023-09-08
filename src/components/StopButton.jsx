import { useState } from "react";
import css from "./stopButton.module.css";

function StopButton() {
  const [status, setStatus] = useState(true);

  const handleClick = async () => {
    setStatus(!status);
    try {
      if (status === false) {
        // Make a request to the Flask server's /start endpoint
        await fetch("http://127.0.0.1:8000/start", {
          method: "POST",
        });
      }
      if (status === true) {
        // Make a request to the Flask server's /start endpoint
        await fetch("http://127.0.0.1:8000/stop", {
          method: "POST",
        });
      }
    } catch (error) {
      console.error("Error starting server:", error);
      // Handle any errors that occurred during the request
    }
  };
  return (
    <div onClick={handleClick}>
      {status === true ? (
        <div className={css.outerCircle}>
          <div className={css.greenScanner}></div>
        </div>
      ) : (
        <div className={css.stoppedOuter}>
          <div className={css.stoppedinner}>
            <div className={css.label}>Start Listening</div>
          </div>
        </div>
      )}
    </div>
  );
}

export default StopButton;
