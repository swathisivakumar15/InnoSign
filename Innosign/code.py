import os
import speech_recognition as sr
import cv2

# Path to the folder containing animation videos
ANIMATION_FOLDER = r"C:\Users\Admin\Documents\FSDproject\myProject\animations"


def recognize_speech():
    """Convert speech to text using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()  # Convert to lowercase for easier matching
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return None


def find_animation(keyword):
    """Find the animation video for a given keyword (case-insensitive)."""
    for file in os.listdir(ANIMATION_FOLDER):
        if file.lower() == f"{keyword}.mp4":
            return os.path.join(ANIMATION_FOLDER, file)
    return None


def play_animation(animation_path):
    """Play an animation video using OpenCV."""
    cap = cv2.VideoCapture(animation_path)

    if not cap.isOpened():
        print(f"Error opening video: {animation_path}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Sign Language Animation', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def process_speech():
    """Process speech input and play corresponding animations."""
    text = recognize_speech()
    if not text:
        return

    words = text.split()
    animation_paths = [find_animation(word) for word in words if find_animation(word)]

    if not animation_paths:
        print("No animations found for the given input.")
        return

    for animation_path in animation_paths:
        print(f"Playing animation for: {os.path.basename(animation_path)}")
        play_animation(animation_path)


if __name__ == "__main__":
    if not os.path.exists(ANIMATION_FOLDER):
        os.makedirs(ANIMATION_FOLDER)
        print(f"Created animations folder at: {ANIMATION_FOLDER}")

    print("Speech-to-Sign Language Converter")
    process_speech()
