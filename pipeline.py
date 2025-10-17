import subprocess

# Function to get video duration in seconds
def get_duration(filename):
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return float(result.stdout.strip())


commands = [
    '''ffmpeg -i "output.mp4" -i "real_audio.mp3" -vf "ass=words_karaoke.ass" -c:a aac "final.mp4" -y''',
    '''ffmpeg -i final.mp4 -i real_audio.mp3 -filter_complex "[1:a]adelay=2000|2000[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -shortest upload.mp4 -y''']
    
    


# Run commands in order
for cmd in commands:
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)
    print("Done! #1")

duration = get_duration("upload.mp4")
print("Duration:", duration)

commands2 = [  
     f'''ffmpeg -i upload.mp4 -loop 1 -i title.png -filter_complex "[0:v]split[main][blur];[blur]boxblur=luma_radius=10:luma_power=1:chroma_radius=10:chroma_power=1,fade=t=in:st=2:d=0.25:alpha=1,fade=t=out:st=4:d=0.25:alpha=1[blurred];[main][blurred]overlay[bg];[1:v]format=rgba,scale=iw*0.4:ih*0.4,fade=t=in:st=2:d=0.25:alpha=1,fade=t=out:st=4:d=0.25:alpha=1[img];[bg][img]overlay=(W-w)/2:(H-h)/2:enable=\'between(t,2,4)\'[v]" -map "[v]" -map 0:a? -c:v libx264 -c:a copy -pix_fmt yuv420p -to {duration} upload_new.mp4 -y''',
    ###'''ffmpeg -i upload_new.mp4 -i bgm.mp3 -filter_complex "[1:a]adelay=2000|2000,volume=0.075[a1];[0:a][a1]amix=inputs=2:duration=first[a]" -map 0:v -map "[a]" -c:v copy -c:a aac final_with_bgm.mp4 -y''',###
    '''ffmpeg -ss 2 -i upload_new.mp4 -c copy output_trimmed.mp4 -y'''

]

for cmd in commands2:
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)
    print("Done! #2")