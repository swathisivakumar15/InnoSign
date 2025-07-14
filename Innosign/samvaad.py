import os
import speech_recognition as sr
from moviepy import VideoFileClip, concatenate_videoclips

# Path to the folder containing animation videos
ANIMATION_FOLDER = "animations"

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
    """Find the animation video for a given keyword."""
    animation_path = os.path.join(ANIMATION_FOLDER, f"{keyword}.mp4")
    if os.path.exists(animation_path):
        return animation_path
    return None

def play_animation(animation_path):
    """Play an animation video."""
    clip = VideoFileClip(animation_path)
    clip.preview()
    clip.close()

def process_speech():
    """Process speech input and play corresponding animations."""
    text = recognize_speech()
    if not text:
        return

    # Split the text into individual words
    words = text.split()

    # Find and play animations for each word
    animation_clips = []
    for word in words:
        animation_path = find_animation(word)
        if animation_path:
            print(f"Found animation for: {word}")
            animation_clips.append(VideoFileClip(animation_path))
        else:
            print(f"No animation found for: {word}")

    if animation_clips:
        # Combine all animations into one video
        final_clip = concatenate_videoclips(animation_clips)
        final_clip.preview()
        final_clip.close()
    else:
        print("No animations found for the given input.")

if __name__ == "__main__":
    # Ensure the animations folder exists
    if not os.path.exists(ANIMATION_FOLDER):
        os.makedirs(ANIMATION_FOLDER)
        print(f"Created animations folder at: {ANIMATION_FOLDER}")

    print("Speech-to-Sign Language Converter")
    process_speech()