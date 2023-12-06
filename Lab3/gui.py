import subprocess
#faig servir el script del lab anterior que canviava la resolució d'un video
def change_resolution(input_file, output_file, resolution):
    # FFmpeg command to change video resolution
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'scale={resolution}',
        '-c:a', 'copy',
        output_file
    ]

def main():
    input_file = input("Enter the path of the input video: ").strip() #interaccio grafica amb lusuari
    output_file = input("Enter the path for the output video: ").strip()
    target_resolution = input("Enter the target resolution (e.g., 1280:720): ").strip()

    if not input_file or not output_file or not target_resolution:
        print("Invalid input. Please provide all required information.")
        return

    change_resolution(input_file, output_file, target_resolution)

if __name__ == "__main__":
    main()
