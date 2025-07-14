from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def animation_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen', '').lower()  # Get input text and convert to lowercase
        words = word_tokenize(text)  # Tokenize the text into words
        tagged = nltk.pos_tag(words)  # Tag words with their part of speech

        # Initialize lemmatizer
        lemmatizer = WordNetLemmatizer()

        # Filter and lemmatize words
        filtered_text = []
        for word, pos in tagged:
            if pos.startswith('VB'):  # Verbs
                filtered_text.append(lemmatizer.lemmatize(word, pos='v'))
            elif pos.startswith('JJ'):  # Adjectives
                filtered_text.append(lemmatizer.lemmatize(word, pos='a'))
            elif pos.startswith('RB'):  # Adverbs
                filtered_text.append(lemmatizer.lemmatize(word, pos='r'))
            else:
                filtered_text.append(lemmatizer.lemmatize(word))  # Default lemmatization

        # Replace specific words with ISL equivalents
        isl_words = []
        for word in filtered_text:
            if word == 'i':
                isl_words.append('me')
            else:
                isl_words.append(word)

        # Map words to ISL animations
        isl_animations = []
        for word in isl_words:
            # Look for ISL animation file (e.g., word.mp4 or word.png)
            animation_path = finders.find(f'isl_animations/{word}.mp4') or finders.find(f'isl_animations/{word}.png')
            if animation_path:
                isl_animations.append(word)
            else:
                # If no animation found, split the word into characters and map each character
                for char in word:
                    char_animation_path = finders.find(f'isl_animations/{char}.mp4') or finders.find(f'isl_animations/{char}.png')
                    if char_animation_path:
                        isl_animations.append(char)

        # Render the result
        return render(request, 'animation.html', {'words': isl_animations, 'text': text})
    else:
        return render(request, 'animation.html')







# import os
# import speech_recognition as sr
# from moviepy import VideoFileClip, concatenate_videoclips
#
# # Path to the folder containing animation videos
# ANIMATION_FOLDER = "C:/Users/Admin/Documents/SWATHI/animations"
#
# def recognize_speech():
#     """Convert speech to text using the microphone."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#
#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#         return text.lower()  # Convert to lowercase for easier matching
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#         return None
#     except sr.RequestError:
#         print("Sorry, there was an issue with the speech recognition service.")
#         return None
#
# def find_animation(keyword):
#     """Find the animation video for a given keyword."""
#     animation_path = os.path.join(ANIMATION_FOLDER, f"{keyword}.mp4")
#     if os.path.exists(animation_path):
#         return animation_path
#     return None
#
# def play_animation(animation_path):
#     """Play an animation video."""
#     clip = VideoFileClip(animation_path)
#     clip.preview()
#     clip.close()
#
# def process_speech():
#     """Process speech input and play corresponding animations."""
#     text = recognize_speech()
#     if not text:
#         return
#
#     # Split the text into individual words
#     words = text.split()
#
#     # Find and play animations for each word
#     animation_clips = []
#     for word in words:
#         animation_path = find_animation(word)
#         if animation_path:
#             print(f"Found animation for: {word}")
#             animation_clips.append(VideoFileClip(animation_path))
#         else:
#             print(f"No animation found for: {word}")
#
#     if animation_clips:
#         # Combine all animations into one video
#         final_clip = concatenate_videoclips(animation_clips)
#         final_clip.preview()
#         final_clip.close()
#     else:
#         print("No animations found for the given input.")
#
# if __name__ == "__main__":
#     # Ensure the animations folder exists
#     if not os.path.exists(ANIMATION_FOLDER):
#         os.makedirs(ANIMATION_FOLDER)
#         print(f"Created animations folder at: {ANIMATION_FOLDER}")
#
#     print("Speech-to-Sign Language Converter")
#     process_speech()



# import os
# import speech_recognition as sr
# from moviepy.editor import VideoFileClip, concatenate_videoclips
#
# # Path to the folder containing animation videos
# ANIMATION_FOLDER = r"C:\Users\Admin\Documents\FSDproject\myProject\animations"
#
# def recognize_speech():
#     """Convert speech to text using the microphone."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#
#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#         return text.lower()  # Convert to lowercase for easier matching
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#         return None
#     except sr.RequestError:
#         print("Sorry, there was an issue with the speech recognition service.")
#         return None
#
# def find_animation(keyword):
#     """Find the animation video for a given keyword."""
#     animation_path = os.path.join(ANIMATION_FOLDER, f"{keyword}.mp4")
#     if os.path.exists(animation_path):
#         return animation_path
#     return None
#
# def play_animation(animation_path):
#     """Play an animation video."""
#     clip = VideoFileClip(animation_path)
#     clip.preview()
#     clip.close()
#
# def process_speech():
#     """Process speech input and play corresponding animations."""
#     text = recognize_speech()
#     if not text:
#         return
#
#     # Split the text into individual words
#     words = text.split()
#
#     # Find and play animations for each word
#     animation_clips = []
#     for word in words:
#         animation_path = find_animation(word)
#         print(f"Searching for animation: {word} -> {animation_path}")
#         if animation_path:
#             print(f"Found animation for: {word}")
#             animation_clips.append(VideoFileClip(animation_path))
#         else:
#             print(f"No animation found for: {word}")
#
#     if animation_clips:
#         # Combine all animations into one video
#         final_clip = concatenate_videoclips(animation_clips)
#         final_clip.preview()
#         final_clip.close()
#     else:
#         print("No animations found for the given input.")
#
# if __name__ == "__main__":
#     # Ensure the animations folder exists
#     if not os.path.exists(ANIMATION_FOLDER):
#         os.makedirs(ANIMATION_FOLDER)
#         print(f"Created animations folder at: {ANIMATION_FOLDER}")
#
#     print("Speech-to-Sign Language Converter")
#     process_speech()






























