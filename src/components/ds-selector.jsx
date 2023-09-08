import { useState } from "react";
import css from "./ds-selector.module.css";
import axios from "axios";
import PropTypes from "prop-types";

function DsSelector(props) {
  const info = props.info;
  const [selectedOption, setSelectedOption] = useState("us8k");

  const handleOptionClick = async (option) => {
    setSelectedOption(option);

    try {
      await axios.post("http://127.0.0.1:8000/selection", {
        selectedOption: option,
      });
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className={css.container}>
      <div className={css.textContainer}>
        <div className={css.title}>Choose a DataSet: </div>
        <div
          className={selectedOption === "us8k" ? css.acitve : css.option}
          onClick={() => handleOptionClick("us8k")}
        >
          us8K
        </div>
        <span className={css.divider}>|</span>
        <div
          className={selectedOption === "esc50" ? css.acitve : css.option}
          onClick={() => handleOptionClick("esc50")}
        >
          ESC50
        </div>
      </div>
      {info === "no" ? (
        ""
      ) : (
        <div className={css.descriptionContainer}>
          {selectedOption === "us8k" ? (
            <div className={css.description}>
              This dataset contains 8732 labeled sound excerpts of urban sounds
              from 10 classes: air_conditioner, car_horn, children_playing,
              dog_bark, drilling, enginge_idling, gun_shot, jackhammer, siren,
              and street_music. The classes are drawn from the urban sound
              taxonomy.
            </div>
          ) : (
            <div className={css.description}>
              The ESC-50 dataset is a labeled collection of 2000 environmental
              audio recordings suitable for benchmarking methods of
              environmental sound classification. The dataset consists of
              5-second- long recordings organized into 50 semantical classes
            </div>
          )}
        </div>
      )}
    </div>
  );
}

DsSelector.propTypes = {
  info: PropTypes.object,
};
export default DsSelector;
