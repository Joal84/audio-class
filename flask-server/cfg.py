import os


class Config:
    def __init__(self, mode="conv", nfilt=26, nfeat=13, nfft=512, rate=16000):
        self.mode = mode
        self.nfilt = nfilt
        self.nfeat = nfeat
        self.nfft = nfft
        self.rate = rate
        self.step = int(rate*1)
        self.model_path = os.path.join("pickles", mode + ".model")
        self.p_path = os.path.join("pickles", mode + ".p")
        self.p_path2 = os.path.join("pickles2", mode + ".p")


def init():
    global recording
    recording = False

    global audio_data
    audio_data = []

    global stream
    stream = None

    global rms_normalized
    rms_normalized = 0

    global sound_list
    sound_list = []

    global glob_start
    glob_start = False

    global model_type
    model_type = "us8k"
