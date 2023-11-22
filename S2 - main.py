import cv2
import numpy as np
import subprocess
import os
from moviepy.editor import VideoFileClip

#exercise 1
class VideoAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def generate_motion_vector_video(self):
        # FFmpeg command to generate video with motioon vectors
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-vf', 'mpdecimate,setpts=N/FRAME_RATE/TB,drawgrid=width=8:height=8:color=red',
            '-c:a', 'copy',
            self.output_file
        ]

        # Run FFmpeg command
        subprocess.run(ffmpeg_cmd)

    # exercise 2
    def create_bbb_container(self):
        # Output file paths
        output_video_file = 'bbb_50s.mp4'
        output_mono_audio_file = 'bbb_mono.mp3'
        output_stereo_low_bitrate_audio_file = 'bbb_stereo_low_bitrate.mp3'
        output_aac_audio_file = 'bbb_aac.aac'

        # FFmpeg command to cut video to 50 seconds
        cut_video_cmd = [
            'ffmpeg',
            '-i', self.input_file,
            '-t', '50',
            '-c', 'copy',
            output_video_file
        ]

        # FFmpeg command to export audio as MP3 mono track
        export_mono_audio_cmd = [
            'ffmpeg',
            '-i', output_video_file,
            '-vn',
            '-ac', '1',
            '-q:a', '2',
            output_mono_audio_file
        ]

        # FFmpeg command to export audio in MP3 stereo with lower bitrate
        export_stereo_low_bitrate_audio_cmd = [
            'ffmpeg',
            '-i', output_video_file,
            '-vn',
            '-q:a', '5',
            '-ac', '2',
            output_stereo_low_bitrate_audio_file
        ]

        # FFmpeg command to export audio in AAC codec
        export_aac_audio_cmd = [
            'ffmpeg',
            '-i', output_video_file,
            '-vn',
            '-c:a', 'aac',
            output_aac_audio_file
        ]

        # FFmpeg command to package everything in a .mp4
        package_cmd = [
            'ffmpeg',
            '-i', output_video_file,
            '-i', output_mono_audio_file,
            '-i', output_stereo_low_bitrate_audio_file,
            '-i', output_aac_audio_file,
            '-map', '0:v',
            '-map', '1:a',
            '-map', '2:a',
            '-map', '3:a',
            '-c', 'copy',
            self.output_file
        ]

        # Run FFmpeg commands
        subprocess.run(cut_video_cmd)
        subprocess.run(export_mono_audio_cmd)
        subprocess.run(export_stereo_low_bitrate_audio_cmd)
        subprocess.run(export_aac_audio_cmd)
        subprocess.run(package_cmd)

#Exercise 3
    def get_track_count(self):
        # FFprobe command to get information about input file
        ffprobe_cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'a:video',
            '-count_frames', '-show_entries',
            'stream=nb_read_frames',
            '-of', 'default=nokey=1:noprint_wrappers=1',
            self.input_file
        ]

        # Run FFprobe command and capture the output
        result = subprocess.run(ffprobe_cmd, capture_output=True, text=True)
        track_count = len(result.stdout.strip().split('\n'))
        return track_count

#Exercise 4

class SubtitleProcessor:
    def __init__(self, video_url, output_file):
        self.video_url = video_url
        self.output_file = output_file

    def download_subtitles(self):
        # FFmpeg command to download subtitlees
        download_cmd = [
            'ffmpeg',
            '-i', self.video_url,
            '-c:s', 'mov_text',
            '-c:v', 'copy',
            '-c:a', 'copy',
            'output_subtitles.en.vtt'
        ]

        # Run FFmpeg command
        subprocess.run(download_cmd)

    def integrate_subtitles(self):
        # Get the downloaded subtitle file
        subtitle_file = 'output_subtitles.en.vtt'

        # FFmpeg command to integrate subtitles into the video
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', self.output_file,
            '-vf', f'subtitles={subtitle_file}',
            '-c:a', 'copy',
            'output_video_with_subtitles.mp4'
        ]

        # Run FFmpeg command
        subprocess.run(ffmpeg_cmd)

#Exercise 5

class VideoProcessor(VideoAnalyzer, SubtitleProcessor): # Inherit methods from both VideoAnalyzer and SubtitleProcessor
    def __init__(self, video_url, output_file): #it calls the constructors of both parent classes
        VideoAnalyzer.__init__(self, video_url, output_file)
        SubtitleProcessor.__init__(self, video_url, output_file)
# inherits from both VideoAnalyzer and SubtitleProcessor
    def process_video_with_subtitles(self):

        self.generate_motion_vector_video()
        self.create_bbb_container()
        self.download_subtitles()
        self.integrate_subtitles()
