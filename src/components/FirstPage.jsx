import Title from "./Title";
import StartRec from "./StartRec";
import css from "./firstPage.module.css";
import DsSelector from "./dsSelector";

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
