import Header from "./header.jsx";
import StartRec from "./start-rec.jsx";
import css from "./first-page.module.css";
import DsSelector from "./ds-selector.jsx";

function FirstPage() {
  return (
    <div className={css.bg}>
      <div className={css.container}>
        <Header size="big" />
        <div className={css.selector}>
          <DsSelector />
        </div>
        <div className={css.button}>
          <StartRec />
        </div>
      </div>
    </div>
  );
}

export default FirstPage;
