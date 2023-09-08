import React from "react";
import css from "./secondPage.module.css";
import SoundsDetected from "./SoundsDetected";
import StopButton from "./StopButton";
import Title from "./Title";
import DsSelector from "./DsSelector";

export default function SecondPage() {
  return (
    <div className={css.bg}>
      <div className={css.container}>
        <div className={css.title}>
          <Title size="small" />
        </div>
        <SoundsDetected />
        <div className={css.radar}>
          <StopButton />
        </div>
        <div className={css.selector}>
          <DsSelector info="no" />
        </div>
      </div>
    </div>
  );
}
