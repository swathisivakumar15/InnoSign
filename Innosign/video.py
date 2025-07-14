import os
import whisper
import requests

# Step 1: Extract Audio from Video
def extract_audio(video_file, audio_file):
    os.system(f"ffmpeg -i {video_file} -q:a 0 -map a {audio_file} -y")

# Step 2: Convert Audio to Text
def audio_to_text(audio_file):
    model = whisper.load_model("base")  # Load Whisper model
    result = model.transcribe(audio_file)  # Transcribe audio to text
    return result["text"]

# Step 3: Translate Text to Sign Language Gestures
def text_to_sign_language(text):
    # Simulated mapping of text to sign language gestures
    sign_language_dict = {
        "hello": "wave_hand",
        "world": "circle_earth",
        "learn": "open_book",
        "thank": "hand_to_chin",
        "you": "point_forward",
        # Add more mappings as needed
    }
    gestures = []
    words = text.lower().split()
    for word in words:
        if word in sign_language_dict:
            gestures.append(sign_language_dict[word])
        else:
            gestures.append("unknown_gesture")  # Placeholder for unknown words
    return gestures

# Step 4: Generate Sign Language Video (Simulated API Call)
def generate_sign_language_video(gestures):
    # Simulated API call to an AI video generator (e.g., DeepMotion)
    api_key = "your_deepmotion_api_key"  # Replace with your API key
    url = "https://api.deepmotion.com/v1/animate"  # Example API endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "gestures": gestures,
        "avatar": "default"  # Specify the avatar
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        video_url = response.json()["video_url"]
        return video_url
    else:
        return "Failed to generate video."

# Main Function
def main(video_file):
    # Step 1: Extract Audio
    audio_file = "audio.wav"
    extract_audio(video_file, audio_file)
    print("Audio extracted successfully.")

    # Step 2: Convert Audio to Text
    text = audio_to_text(audio_file)
    print("Extracted Text:", text)

    # Step 3: Translate Text to Sign Language Gestures
    gestures = text_to_sign_language(text)
    print("Sign Language Gestures:", gestures)

    # Step 4: Generate Sign Language Video
    print("Generating sign language video...")
    video_url = generate_sign_language_video(gestures)
    if video_url.startswith("http"):
        print("Sign Language Video URL:", video_url)
    else:
        print(video_url)  # Show error message

if __name__ == "__main__":
    video_file = "input_video.mp4"  # Replace with your video file path
    main(video_file)