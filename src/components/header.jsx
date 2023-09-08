import css from "./header.module.css";
import PropTypes from "prop-types";

export default function Header(props) {
  const size = props.size;
  Header.propTypes = {
    size: PropTypes.string,
  };
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
