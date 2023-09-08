from flask import Flask, jsonify, request
from flask_cors import CORS
from predicition import init_audio_stream, start_audio_stream, stop_audio_stream, stop_audio_button, prediction
from cfg import Config
import cfg
import pickle
from keras.models import load_model
import time


config = Config()
cfg.init()

with open(config.p_path, "rb") as handle:
    tmp = pickle.load(handle)

THRESHOLD = 0.03  # Adjust this threshold to your desired value

df_esc50 = tmp.df_esc50
df_us8k = tmp.df_us8k
(train_images_us8k, test_images_us8k,
 train_labels_us8k, test_labels_us8k) = tmp.data8k
(train_images_esc50, test_images_esc50,
 train_labels_esc50, test_labels_esc50) = tmp.dataesc50

model_us8k = load_model("best_us8k_model.ckpt")
model_esc50 = load_model("best_esc50_model.ckpt")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize the audio stream
cfg.stream = init_audio_stream()


@app.route("/start", methods=["GET", "POST"])
def start_prediction():

    cfg.glob_start = True
    return jsonify({"status": "Started recording" if cfg.recording else "Stopped recording"})


@app.route("/stop", methods=["GET", "POST"])
def stop_prediction():
    cfg.glob_start = False

    return jsonify({"status": "Stopped recording from stop page"})


@app.route("/predictions", methods=["GET"])
def get_predictions():
    return jsonify({"predictions": cfg.sound_list})


@app.route("/sounds", methods=["GET"])
def get_sound_list():

    # Implement a timeout or other logic to determine when to respond to the client.
    timeout = 30  # Set an appropriate timeout value.
    start_time = time.time()

    while True:
        if len(cfg.sound_list) > 0:
            return jsonify(cfg.sound_list)
        elif time.time() - start_time > timeout:
            # Return an empty list if no data available after the timeout.
            return jsonify([])


@app.route("/selection", methods=["POST"])
def get_selection():

    selected_option = request.json.get("selectedOption")

    if selected_option == "us8k":
        cfg.model_type = "us8k"
    elif selected_option == "esc50":
        cfg.model_type = "esc50"
    else:
        return jsonify({"error": "Invalid option"})

    return "", 204


if __name__ == "__main__":
    app.run(port=8000, debug=True)
