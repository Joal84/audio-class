import css from "./title.module.css";
import PropTypes from "prop-types";

function Title(props) {
  const size = props.size;
  return (
    <div className={css.main}>
      <div className={css[size]}>
        Audio Classifier
        <div className={css[size + "byName"]}>
          PROJECT BY <spam className={css[size + "name"]}>JOÃO PINHEIRO</spam>
        </div>
      </div>
    </div>
  );
}
Title.propTypes = {
  size: PropTypes.object,
};
export default Title;
