import css from "./second-page.module.css";
import SoundsDetected from "./sounds-detected";
import StopButton from "./stop-button.jsx";
//import Title from "./title.jsx";
import DsSelector from "./ds-selector.jsx";

export default function SecondPage() {
  return (
    <div className={css.bg}>
      <div className={css.container}>
        <div className={css.title}></div>
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
