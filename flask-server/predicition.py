import pyaudio
import numpy as np
from keras.models import load_model
from cfg import Config
import cfg
import pickle
import audioop
import time

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = RATE * 0.

# Threshold parameters
THRESHOLD = 0.07  # Adjust this threshold to your desired value
recording = False
audio = pyaudio.PyAudio()
audio_data = []
stream = None

# Loading df"s
config = Config()

with open(config.p_path, "rb") as handle:
    tmp = pickle.load(handle)

df_esc50 = tmp.df_esc50
df_us8k = tmp.df_us8k


# Loading models
model_us8k = load_model("best_us8k_model.ckpt")
model_esc50 = load_model("best_esc50_model.ckpt")


# Signal formating function

def read_signal(writeFile):

    data_sample_average = 220500
    data = writeFile

    # padding data to keep the same size
    if data.shape[0] <= data_sample_average:
        newdata = np.zeros((data_sample_average,), dtype=np.float32)
        newdata[: data.shape[0]] = data
        newdata.astype(np.float32)
    else:
        newdata = data[:data_sample_average].astype(np.float32)

    newdata.astype(np.float32)

    dataN = np.shape(newdata)[0]

    newdata = np.reshape(np.transpose(newdata), (1, dataN))

    return newdata

# Signal processing function to spectograms


def NRDT(filename, w, flag, channels):

    signal = filename
    signal = signal.astype("float32")
    Nsamples = np.size(signal, 1)
    # delay should be no more than w/4 (w usually is a power of 2)
    delmax = w / 4
    res = np.where(channels <= delmax)
    # print(res)
    channels = channels[res]  # remove chanells not satisfyiong this condition.
    m = np.shape(channels)[0]

    spectrograms = Nsamples // w  # The number of spectrograms computed

    # The number of samples used to compute the spectrograms.The other samples are discarded
    Samples = spectrograms * w

    # each line is one to be submited for computation of spectrogram
    matrix = np.reshape(signal[0, 0: Samples], (spectrograms, w))

    spectrum = np.zeros((m, spectrograms))
    for i in range(0, spectrograms):
        values = matrix[i, :]  # the whole line
        for k in range(0, m):
            delay = channels[k]  # delays
            t = np.array(range(delay, w-delay-1))
            difus = np.abs(values[t - delay] +
                           values[t + delay] - 2 * values[t])
            if flag == 0:
                spectrum[k, i] = np.mean(difus) / 4
            elif flag == 1:
                spectrum[k, i] = np.mean(difus / (np.abs(values[t - delay]) + np.abs(
                    values[t + delay]) + 2 * np.abs(values[t]) + 1e-12)) / 4
    return spectrum


def prediction(audio_data):

    audio_data_combined = np.concatenate(audio_data)
    signal = read_signal(audio_data_combined)

    channels = np.array(
        [2, 4, 8, 16, 20, 32, 50, 64, 100, 128, 200, 300])
    w = 1000
    flag = 0
    predict = NRDT(filename=signal, w=w,
                   flag=flag, channels=channels)

    s = np.shape(predict)
    if cfg.model_type == "us8k":
        z = model_us8k.predict(np.reshape(predict, (1, s[0], s[1], 1)))
        filtered_row = df_us8k[df_us8k['classID']
                               == np.argmax(z)].iloc[0]
        category_value = filtered_row['class']
    else:
        z = model_esc50.predict(np.reshape(predict, (1, s[0], s[1], 1)))
        filtered_row = df_esc50[df_esc50["target"] == np.argmax(z)].iloc[0]
        category_value = filtered_row["category"]

    return category_value


def audio_callback(in_data, frame_count, time_info, status):

    # Convert audio data to numpy array
    audio_np = np.frombuffer(in_data, dtype=np.int16)
    rms = audioop.rms(audio_np, 2)  # 2 is the width (in bytes) of each sample

    cfg.rms_normalized = rms / 32768.0

    if cfg.glob_start == True:
        if not cfg.recording and cfg.rms_normalized > THRESHOLD:
            print("Recording started.")
            cfg.recording = True
            cfg.audio_data.clear()

        # Append the audio data to the list if recording is enabled and above the threshold
        if cfg.recording and cfg.rms_normalized > THRESHOLD:
            cfg.audio_data.append(audio_np)

        # Check if the volume dropped below the threshold to stop recording and send for prediction
        elif cfg.recording and cfg.rms_normalized <= THRESHOLD:
            time.sleep(0.8)
            print("Recording stopped.")
            cfg.recording = False

            if len(cfg.audio_data) > 0:
                pred = prediction(cfg.audio_data)
                cfg.sound_list.append(pred)
                if len(cfg.sound_list) >= 11:
                    cfg.sound_list = []
        # Continue streaming audio
    return in_data, pyaudio.paContinue


# Initialize PyAudio
def init_audio_stream():
    stream = audio.open(format=FORMAT,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024,
                        input_device_index=1,
                        stream_callback=audio_callback)

    return stream


# List available audio devices (microphones)
print("Available audio devices:")
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    print(f"{i}: {device_info['name']}")


def start_audio_stream():
    cfg.stream.start_stream()


def stop_audio_stream():
    cfg.stream.stop_stream()
    if len(cfg.audio_data) > 0:
        pred = prediction(cfg.audio_data)
    return pred


def stop_audio_button():
    cfg.stream.stop_stream()
    if len(cfg.audio_data) > 0:
        pred = prediction(cfg.audio_data)

    return pred


def is_audio_stream_active():
    return cfg.stream.is_active()
