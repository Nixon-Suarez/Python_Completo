# este es un prograna para descargar videos o audios de youtube
# el archivo - link2dovn10ad.txt- tiere las direcciones url a descargar'
# siempre inicia indicando que quieres descargar "audio" o "video"
# y seguidamente se ponen los links a descargar, para este ejemlo tenemos 2 links


import tkinter as tk
from pytube import YouTube
import os

def download_video():
    url = "https://youtu.be/Oyhpwyrq1N0?si=whQUF8nFh3GRXjB6"
    current_folder = os.getcwd()
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path=current_folder)
    status_label.config(text="Audio downloaded successfully!")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL label
url_label = tk.Label(root, text="YouTube Video:")
url_label.pack()

# Button to download
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Run the application
root.mainloop()

