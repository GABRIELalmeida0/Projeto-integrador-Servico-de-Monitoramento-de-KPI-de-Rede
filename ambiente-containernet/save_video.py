from subprocess import Popen, PIPE
import signal
import time

container_name = "d2"
cmd_ffmpeg = "ffmpeg -i rtsp://10.0.0.1:8554/launch480p -vcodec copy -an -loglevel quiet MyOutput.mp4 &"
ffmpeg_process = Popen(cmd_ffmpeg, stdout=PIPE, text=True, shell=True)

cmd = f"tcpdump -i {container_name}-eth0"
tcpdump_process = Popen(cmd, stdout=PIPE, text=True, shell=True)

for line in tcpdump_process.stdout:
    print(line, end="")

print("sem dados...")

time.sleep(2)
ffmpeg_process.send_signal(signal.SIGTERM)
