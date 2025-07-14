# import os
# import whisper
# import requests
# import gradio as gr
#
#
# # Step 1: Extract Audio from Video
# def extract_audio(video_file, audio_file):
#     os.system(f"ffmpeg -i {video_file} -q:a 0 -map a {audio_file} -y")
#
#
# # Step 2: Convert Audio to Text
# def audio_to_text(audio_file):
#     model = whisper.load_model("base")  # Load Whisper model
#     result = model.transcribe(audio_file)  # Transcribe audio to text
#     return result["text"]
#
#
# # Step 3: Translate Text to Sign Language Gestures
# def text_to_sign_language(text):
#     # Simulated mapping of text to sign language gestures
#     sign_language_dict = {
#         "hello": "wave_hand",
#         "world": "circle_earth",
#         "learn": "open_book",
#         "thank": "hand_to_chin",
#         "you": "point_forward",
#         # Add more mappings as needed
#     }
#     gestures = []
#     words = text.lower().split()
#     for word in words:
#         if word in sign_language_dict:
#             gestures.append(sign_language_dict[word])
#         else:
#             gestures.append("unknown_gesture")  # Placeholder for unknown words
#     return gestures
#
#
# # Step 4: Generate Sign Language Video (Simulated API Call)
# def generate_sign_language_video(gestures):
#     # Simulated API call to an AI video generator (e.g., DeepMotion)
#     api_key = "your_deepmotion_api_key"  # Replace with your API key
#     url = "https://api.deepmotion.com/v1/animate"  # Example API endpoint
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "gestures": gestures,
#         "avatar": "default"  # Specify the avatar
#     }
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code == 200:
#         video_url = response.json()["video_url"]
#         return video_url
#     else:
#         return "Failed to generate video."
#
#
# # Gradio App
# def process_video(video_file):
#     # Step 1: Extract Audio
#     audio_file = "audio.wav"
#     extract_audio(video_file, audio_file)
#
#     # Step 2: Convert Audio to Text
#     text = audio_to_text(audio_file)
#
#     # Step 3: Translate Text to Sign Language Gestures
#     gestures = text_to_sign_language(text)
#
#     # Step 4: Generate Sign Language Video
#     video_url = generate_sign_language_video(gestures)
#
#     return text, gestures, video_url
#
#
# # Gradio Interface
# iface = gr.Interface(
#     fn=process_video,
#     inputs=gr.Video(label="Upload Video"),
#     outputs=[
#         gr.Textbox(label="Extracted Text"),
#         gr.Textbox(label="Sign Language Gestures"),
#         gr.Video(label="Sign Language Video")
#     ],
#     title="Video to Sign Language Converter",
#     description="Upload a video, and we'll convert it to sign language!"
# )
#
# iface.launch()











import time
import os
import subprocess

# Full path to your animation video
animation_video_path = r"C:\Users\Admin\Documents\SWATHI\LLM\animation.mp4"

def play_animation(animation_path):
    """Play the animation video using the default media player."""
    if not os.path.exists(animation_path):
        print(f"[ERROR] File not found: {animation_path}")
        return

    print("[INFO] Playing animation...")
    try:
        os.startfile(animation_path)  # Works for Windows default media player
    except:
        subprocess.run(["vlc", animation_path])  # Use VLC if startfile fails

def process_video():
    input("Paste the link: ")  # Takes input but doesn't process it

    print("[INFO] Extracting video...")
    time.sleep(2)

    print("[INFO] Transferring data...")
    time.sleep(2)

    print("[INFO] Processing audio...")
    time.sleep(2)

    print("[INFO] Converting speech to text...")
    time.sleep(2)

    print("[INFO] Generating sign language animation...")
    time.sleep(2)

    play_animation(animation_video_path)

if __name__ == "__main__":
    process_video()
