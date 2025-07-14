# Innosign – Bridging Communication for the Speech and Hearing Impaired

**Innosign** is an AI-powered real-time sign language translation system designed to enable seamless communication between the speech- and hearing-impaired and the rest of the world. Using deep learning and computer vision techniques, it recognizes hand gestures from Indian Sign Language (ISL) and converts them into text or speech. The project aims to promote accessibility, inclusion, and independence through affordable assistive technology.

---

## Achievements

- Selected in the **Smart India Hackathon (SIH)**, a prestigious national innovation competition.
- Winner of multiple **National-Level Project Expos** for innovation, utility, and social impact.
- Successfully demonstrated a **real-time, end-to-end prototype** for gesture recognition and voice synthesis.
- Recognized for addressing a key accessibility challenge through deep tech.

---

## Problem Statement

Individuals with speech and hearing impairments face significant barriers in daily communication due to limited public awareness of sign language. This affects their access to education, healthcare, employment, and essential services.

**Innosign** bridges this communication gap by:

- Recognizing Indian Sign Language (ISL) gestures in real-time using a webcam.
- Translating these gestures into text and converting them to speech.
- Enabling reverse communication using speech-to-text for assisted dialogue.
- Making human-computer and human-human interaction accessible and inclusive.

---

## Technologies Used

- **Programming Language:** Python
- **Frameworks:** TensorFlow / PyTorch
- **Computer Vision:** OpenCV, MediaPipe (for hand and pose tracking)
- **Speech Processing:** gTTS (Google Text-to-Speech), SpeechRecognition
- **Model Architecture:** CNN + LSTM (for sequence gesture recognition)
- **Frontend (optional):** Streamlit or Flask
- **Deployment Target:** Desktop/Web (mobile support under consideration)

---

## Repository Structure

innosign/
├── code/
│ ├── gesture_model.py # CNN/LSTM model definition
│ ├── predict.py # Real-time prediction and webcam feed
│ ├── tts.py # Text-to-Speech module
│ └── app.py # Main application entry point
├── data/
│ ├── gestures/ # Preprocessed or sample ISL gesture dataset
│ └── labels.csv # Gesture label mappings
├── utils/
│ ├── preprocessing.py # Image processing and data augmentation
│ └── helper.py # Miscellaneous utility functions
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/innosign.git
cd innosign

### 2. Install Dependencies
Make sure you have Python 3.8+ and pip installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt

### 3. Run the Application
bash
Copy
Edit
python code/app.py
This will launch the webcam-based interface, which will recognize gestures and convert them to text and speech in real-time.

## Screenshots and Demo

Demo Video: 
Interface Screenshot:
<img width="1366" height="768" alt="2025-07-14" src="https://github.com/user-attachments/assets/9b80f69a-2217-41de-960e-438f4ce9a8f0" />




## Future Enhancements
Expand ISL dataset to support more complex, sentence-level gestures.

Optimize for mobile devices using TensorFlow Lite or MediaPipe mobile SDK.

Integrate avatar-based gesture playback for reverse communication (speech-to-sign).

Add multilingual speech support (Hindi, Telugu, Tamil, etc.).

Deploy on cloud with a user-friendly web interface for accessibility.

## Contact
For queries, demo requests, or collaboration opportunities:

Email: swathi2004sivakumar@gmail.com

LinkedIn: http://linkedin.com/in/swathisivakumar

