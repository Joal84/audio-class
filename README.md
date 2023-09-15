# Environmental Audio Classification Application
This application is designed for environmental audio classification and aims to assist individuals who are deaf or have severe hearing loss by focusing on environmental and urban sounds. To get started with this project, follow the steps below.
Please note that this application is meant to run locally, as all audio capturing and analysis processes are performed on the server.

[![Final video of fixing issues in your code in VS Code](https://img.youtube.com/vi/srpw3UPxvaw/maxresdefault.jpg)](https://www.youtube.com/watch?v=srpw3UPxvaw)
## Getting Started
### Clone this repository to your local machine:
```
git clone https://github.com/Joal84/audio-class.git
```
### Navigate to the project directory:
```
cd audio-class
```
### Install the required dependencies:
```
npm install
```
### Go to /flask-server folder and install the required libraries and packages:
```
pip install -r requirements.txt
```
### Start the application:
```
npm run dev
```
## Project Overview
Purpose: This application is designed for environmental audio classification, with a focus on assisting individuals who are deaf or have severe hearing loss, particularly in recognizing environmental and urban sounds.

Data Sources: The classification model was trained using two datasets:
- ESC50: 50 classes, 40 recordings per class, each lasting 5 seconds.
- us8K: 10 classes, 8732 total recordings, each with a duration of less than 4 seconds.
- ![Screenshot of class distribution of both datasets.](https://private-user-images.githubusercontent.com/97687297/267327243-5daeec6d-9132-4360-bbaf-56a2ea922291.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ1MjE5NDUsIm5iZiI6MTY5NDUyMTY0NSwicGF0aCI6Ii85NzY4NzI5Ny8yNjczMjcyNDMtNWRhZWVjNmQtOTEzMi00MzYwLWJiYWYtNTZhMmVhOTIyMjkxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzA5MTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMwOTEyVDEyMjcyNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU5OTYyMjFlNDAxMTgyYjdmYTIwZWE3ZmMzN2Q4ZWYwMjI1OWFiYmQ0ZmYxOTAyYTRjZDQ4MzAxOTdhZTJkZmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.6Bxns4FKcKA9WCy6QRZ-kgK-JxbuZh0-SiyIcgAEwTk)

## Feature Extraction
- The application uses the "Librosa" library to load all audio files.
- All audio files have a sample rate of 44.1 kHz.
- Audio signals are captured in 1-second chunks. If a sound has a smaller duration, it's padded with 0's. Longer sounds are truncated.
- The audio data is reshaped into a 2D array.
- Spectrogram extraction uses the Normalized Radial Diffusivity Transform (NRDT) algorithm to calculate diffusivity at different time delays.
- Various parameters like flag, window (w), and channels are set for different spectrogram extraction approaches.

## Convolutional Neural Network (CNN) Model
- The CNN model uses the "Selu" activation function to mitigate vanishing and exploding gradient problems.
- It monitors validation accuracy and saves the best model checkpoint per epoch.
- Model evaluation involves training both datasets on the same model, achieving high accuracy levels of 94% (esc50) and 97% (us8k) on test data.

## Live Audio Input
- The application utilizes the "pyaudio" library for managing live audio input into Python.
- You can choose which microphone to be used by changing `input_device_index` value, in `prediction.py`, to curresponding number of the device you would like to use.

## Audio Gate
Issues with live audio input are often related to the "chunks" of audio sent to the model for prediction.
A gate system has been implemented to automate the start and end of the recording process, helping to address these issues. A gate **threshold** in `prediction.py` can be ajusted for fine tuning. 
