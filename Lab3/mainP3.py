import subprocess
from moviepy.editor import VideoFileClip
import json
def convert_to_720p(input_file, output_file):
    # FFmpeg command to scale the video to 720p
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=1280:720',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)
def convert_to_480p(input_file, output_file):
    # FFmpeg command to scale the video to 480p
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=854:480',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_to_240p(input_file, output_file):
    # FFmpeg command to scale the video to 240p
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=360:240',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)


def convert_to_120p(input_file, output_file):
    # FFmpeg command to scale the video to 120p
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=160:120',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_to_vp8(input_file, output_file, video_bitrate='1M'):
    # FFmpeg command to convert video to VP8
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libvpx',
        '-b:v', video_bitrate,
        '-c:a', 'libvorbis',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_to_vp9(input_file, output_file, video_bitrate='1M'):
    # FFmpeg command to convert video to VP9
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libvpx-vp9',
        '-b:v',  video_bitrate,
        '-c:a', 'libvorbis',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_to_H265(input_file, output_file, video_bitrate='1M'):
    # FFmpeg command to convert video to H265
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx265',
        '-b:v',  video_bitrate,
        '-c:a', 'aac',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_to_AV1(input_file, output_file, video_bitrate='1M'):
    # FFmpeg command to convert video to AV1
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libaom-av1',
        '-crf 30',
        '-b:v 0',
        '-strict experimental'
        '-c:a', 'libopus',
        output_file
    ]
    subprocess.run(command, check=True)


#Exercise 2. I will compare vp8 and vp9:

def create_comparison(input_file_vp8, input_file_vp9, output_file):
    # FFmpeg command to create a side-by-side comparison of VP8 and VP9 videos
    command = [
        'ffmpeg',
        '-i', input_file_vp8,#els videos anteriors que farem servir
        '-i', input_file_vp9,
        '-filter_complex', '[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]', #aquesta opcio es per tenir els dos videos alhora un al costat de laltre
        '-map', '[vid]',
        '-c:v', 'libx264',
        '-crf', '23',
        '-preset', 'medium',
        '-c:a', 'aac',
        '-b:a', '192k',
        output_file
    ]

    # Run the FFmpeg command
    try:
        subprocess.run(command, check=True)
        print(f"Comparison video created successfully. Output video saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during comparison video creation: {e}")
