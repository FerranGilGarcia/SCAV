#Exercise 1
# Importar el módulo subprocess para ejecutar comandos de ffmpeg
import subprocess
from moviepy.editor import VideoFileClip
import json

def convert_to_mpeg(video_path, output_path):
    clip = VideoFileClip(video_path)
    clip.write_videofile(output_path, codec='mpeg2video')#use this functiion to convert to mpeg

#Exercise 2
def change_resolution(input_file, output_file, width, height): #width and height will be the resolution that we want
    command = f"ffmpeg -i {input_file} -vf scale={width}:{height} {output_file}" #use of ffmpeg to change the width and height
    subprocess.run(command, shell=True)

#Exercise 3
def change_chroma_subsampling(input_file, output_file, subsampling):
    command = f"ffmpeg -i {input_file} -vf format=yuv{subsampling} {output_file}"#use the ffmpeg to change the chroma subsampling
    subprocess.run(command, shell=True)


#Exercise 4
def print_video_info(input_file):
    command = f"ffprobe -v quiet -print_format json -show_format -show_streams {input_file}"
    result = subprocess.run(command, shell=True, capture_output=True)
    video_info = json.loads(result.stdout)
# 5 relevant data of the BBB vídeo
    print("File Name: ", input_file)
    print("Duration: ", video_info['format']['duration'])
    print("Bit Rate: ", video_info['format']['bit_rate'])
    print("Format Name: ", video_info['format']['format_name'])
    print("Format Long Name: ", video_info['format']['format_long_name'])