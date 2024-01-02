from flask import Flask, jsonify, request
from flask_cors import CORS
from predicition import init_audio_stream
from cfg import Config
import cfg
from keras.models import load_model
import time


config = Config()
cfg.init()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize the audio stream
cfg.stream = init_audio_stream()


@app.route("/start", methods=["POST"])
def start_prediction():

    cfg.glob_start = True
    return jsonify({"status": "Started recording" if cfg.recording else "Stopped recording"})


@app.route("/stop", methods=["POST"])
def stop_prediction():
    cfg.glob_start = False

    return jsonify({"status": "Stopped recording from stop page"})


@app.route("/sounds", methods=["GET"])
def get_sound_list():

    timeout = 5  # Set an appropriate timeout value.
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
    app.run(port=8000)
