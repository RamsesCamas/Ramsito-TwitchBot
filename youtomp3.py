import os
from moviepy.editor import VideoFileClip


video = VideoFileClip("./Hey Hey -Hayasaka.mp4")
video.audio.write_audiofile("tranformers.mp3")