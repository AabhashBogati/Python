from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download (url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video Downloaded Successfully")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Downloading...")
        download(video_url, save_dir)
    else:
        print("Please select a folder... ")
