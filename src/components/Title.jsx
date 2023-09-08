import React from "react";
import css from "./title.module.css";

function Title(props) {
  return (
    <div className={css.main}>
      <div className={css[props.size]}>
        Audio Classifier
        <div className={css[props.size + "byName"]}>
          PROJECT BY{" "}
          <spam className={css[props.size + "name"]}>JOÃO PINHEIRO</spam>
        </div>
      </div>
    </div>
  );
}

export default Title;
