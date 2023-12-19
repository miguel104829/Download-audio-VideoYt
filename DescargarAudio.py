from tkinter import *
from tkinter.ttk import Style
from ttkthemes import ThemedTk
import os
import pytube
from moviepy.editor import *

def download_audio():
    try:
        video_url = url_entry.get()
        video = pytube.YouTube(video_url)
        video_title = video.title
        filename = f"{video_title}.mp3"

        video_stream = video.streams.get_highest_resolution()
        video_stream.download()

        video_clip = VideoFileClip(video_stream.default_filename)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(filename)

        os.remove(video_stream.default_filename)
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        output_path = os.path.join(desktop_path, filename)
        os.replace(filename, output_path)

        success_label.config(text=f"File saved at: {output_path}")
    except Exception as e:
        error_label.config(text=f"Error: {e}")

root = ThemedTk(theme="radiance")  # Cambia "radiance" por el nombre del tema que quieras usar
root.title("Galactic Audio Downloader")

style = Style()
style.configure("TLabel", foreground="black", background="white", padding=10, font=('Helvetica', 16))
style.configure("TEntry", foreground="black", background="white", padding=10, font=('Helvetica', 16))
style.configure("TButton", foreground="black", background="white", padding=10, font=('Helvetica', 16))

url_label = Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = Entry(root)
url_entry.pack()

download_button = Button(root, text="Download Audio", command=download_audio)
download_button.pack()

success_label = Label(root, text="")
success_label.pack()

error_label = Label(root, text="", fg="red")
error_label.pack()

root.mainloop()