from moviepy import VideoFileClip

video_path = input("Enter the path : ")
edited_video_path = video_path.removeprefix('"').removesuffix('"')
video_source = VideoFileClip(edited_video_path)
extracted_audio = video_source.audio
output_file_name = input("Enter the file name : ")

user_input = int(input("""Select the audio format:\n
    Press 1 for MP3 (.mp3)\n
    Press 2 for WAV (.wav)\n
    Press 3 for OGG (.ogg)\n
    ------>  """))


def select_format(value):
    if value == 1:
        return "mp3"
    elif value == 2:
        return "wav"
    elif value == 3:
        return "ogg"


print(f"file name : {output_file_name}")
print(f"audio format selected : {edited_video_path}")
audio_format = select_format(user_input)
extracted_audio.write_audiofile(
    f"C:\\Users\\Abhiraj Shilkar\\OneDrive\\Desktop\\python projects\\results\\{output_file_name}.{audio_format}")
