import Title from "./title";
import StartRec from "./start-rec";
import css from "./first-page.module.css";
import DsSelector from "./ds-selector";

function FirstPage() {
  return (
    <div className={css.bg}>
      <div className={css.container}>
        <Title size="big" />
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
