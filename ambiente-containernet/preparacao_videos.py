import os
import subprocess

video_out_path = ['video_out720p.m4v','video_out480p.m4v','video_out1080p.m4v']
for videos_out in video_out_path:
    videos_out
video_ready_path = ['video_ready720p.mp4','video_ready480p.mp4','video_ready1080p.mp4']
for videos_ready in video_ready_path:
    videos_ready
video_ref_path = ['video_ready_ref720p.yuv','video_ready_ref480p.yuv','video_ready_ref1080p.yuv']
for videos_ref in video_ref_path:
    videos_ref



if os.path.exists(videos_out) and os.path.exists(videos_ready) and os.path.exists(videos_ref):
    print("Os arquivos de vídeo já foram preparados anteriormente.")
    
else:
    print("Iniciando a conversão do vídeo 720p...")
    video_convert_command = ['ffmpeg', '-i', 'video_origin720p.y4m', 'video_out720p.m4v']
    video_convert = subprocess.Popen(video_convert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output1, err1 = video_convert.communicate()
    video_convert.wait()
    
    if video_convert.returncode != 0:
        print("Erro durante a conversão do vídeo 720p:")
        print(err1)
        exit(1)

    print("Conversão do vídeo 720p concluída.")
    print("Iniciando a adição de dicas ao vídeo 720p...")
    video_hint_command = ['MP4Box', '-hint', '-mtu', '1024', '-add', 'video_out720p.m4v', 'video_ready720p.mp4']
    video_hint = subprocess.Popen(video_hint_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output2, err2 = video_hint.communicate()
    video_hint.wait()

    if video_hint.returncode != 0:
        print("Erro durante a adição de dicas ao vídeo 720p:")
        print(err2)
        exit(1)

    print("Adição de dicas ao vídeo 720p concluída.")
    print("Iniciando a criação do vídeo 720p de referência...")
    video_ref_command = ['ffmpeg', '-i', 'video_ready720p.mp4', 'video_ready_ref720p.yuv']
    video_ref = subprocess.Popen(video_ref_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output3, err3 = video_ref.communicate()
    video_ref.wait()

    if video_ref.returncode != 0:
        print("Erro durante a criação do vídeo 720p de referência:")
        print(err3)
        exit(1)

    print("Criação do vídeo de referência 720p concluída.")

###########################################################################################################################################################################

    print("Iniciando a conversão do vídeo 480p...")
    video_convert_command = ['ffmpeg', '-i', 'video_origin480p.y4m', 'video_out480p.m4v']
    video_convert = subprocess.Popen(video_convert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output1, err1 = video_convert.communicate()
    video_convert.wait()
    
    if video_convert.returncode != 0:
        print("Erro durante a conversão do vídeo 480p:")
        print(err1)
        exit(1)

    print("Conversão do vídeo concluída 480p.")
    print("Iniciando a adição de dicas ao vídeo 480p...")
    video_hint_command = ['MP4Box', '-hint', '-mtu', '1024', '-add', 'video_out480p.m4v', 'video_ready480p.mp4']
    video_hint = subprocess.Popen(video_hint_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output2, err2 = video_hint.communicate()
    video_hint.wait()

    if video_hint.returncode != 0:
        print("Erro durante a adição de dicas ao vídeo 480p:")
        print(err2)
        exit(1)

    print("Adição de dicas ao vídeo concluída 480p.")
    print("Iniciando a criação do vídeo de referência 480p...")
    video_ref_command = ['ffmpeg', '-i', 'video_ready480p.mp4', 'video_ready_ref480p.yuv']
    video_ref = subprocess.Popen(video_ref_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output3, err3 = video_ref.communicate()
    video_ref.wait()

    if video_ref.returncode != 0:
        print("Erro durante a criação do vídeo 480p de referência:")
        print(err3)
        exit(1)

    print("Criação do vídeo 480p de referência concluída.")

###########################################################################################################################################################################

    print("Iniciando a conversão do vídeo 1080p...")
    video_convert_command = ['ffmpeg', '-i', 'video_origin1080p.y4m', 'video_out1080p.m4v']
    video_convert = subprocess.Popen(video_convert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output1, err1 = video_convert.communicate()
    video_convert.wait()
    
    if video_convert.returncode != 0:
        print("Erro durante a conversão do vídeo 1080p:")
        print(err1)
        exit(1)

    print("Conversão do vídeo concluída 1080p.")
    print("Iniciando a adição de dicas ao vídeo 1080p...")
    video_hint_command = ['MP4Box', '-hint', '-mtu', '1024', '-add', 'video_out1080p.m4v', 'video_ready1080p.mp4']
    video_hint = subprocess.Popen(video_hint_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output2, err2 = video_hint.communicate()
    video_hint.wait()

    if video_hint.returncode != 0:
        print("Erro durante a adição de dicas ao vídeo 1080p:")
        print(err2)
        exit(1)

    print("Adição de dicas ao vídeo concluída 1080p.")
    print("Iniciando a criação do vídeo de referência 1080p...")
    video_ref_command = ['ffmpeg', '-i', 'video_ready1080p.mp4', 'video_ready_ref1080p.yuv']
    video_ref = subprocess.Popen(video_ref_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output3, err3 = video_ref.communicate()
    video_ref.wait()

    if video_ref.returncode != 0:
        print("Erro durante a criação do vídeo de referência 1080p:")
        print(err3)
        exit(1)

    print("Criação do vídeo de referência concluída 1080p.")