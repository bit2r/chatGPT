import speech_recognition as sr
import moviepy.editor as mp
from datetime import timedelta

# Function to convert seconds to SRT time format
def format_srt_time(seconds):
    return str(timedelta(seconds=seconds))


def transcribe_and_create_srt(input_video, output_srt):
    # Load the video
    video = mp.VideoFileClip(input_video)
    audio = video.audio

    # Save the audio as a temporary WAV file
    audio.write_audiofile("temp_audio.wav")

    # Transcribe the audio
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = recognizer.record(source)
        transcription = recognizer.recognize_google(audio_data, language="en-US", show_all=True)

    # Create the SRT file
    with open(output_srt, "w") as srt_file:
        index = 1
        if 'alternative' in transcription:
            for entry in transcription["alternative"]:
                if 'timestampedWords' in entry:
                    for word_info in entry["timestampedWords"]:
                        start_time = format_srt_time(float(word_info["startTime"][:-1]))
                        end_time = format_srt_time(float(word_info["endTime"][:-1]))
                        srt_file.write(f"{index}\n{start_time} --> {end_time}\n{word_info['word']}\n\n")
                        index += 1



input_video_file = "../../../ElephantsDream.mp4"
output_srt_file = "audio_sample.srt"
transcribe_and_create_srt(input_video_file, output_srt_file)
