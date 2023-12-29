from flask import Flask, request
from os import listdir, mkdir
from time import sleep

class App():
    def __init__(self, net, default_url):
        self.net = net
        self.default_url = default_url

    def start_app(self):
        app = Flask("__APP__")

        @app.route("/capture_streaming", methods=["GET"])
        def capture_streaming():
            node = request.args.get("node_name")
            d = "0ms" if request.args.get("delay") is None else request.args.get("delay")
            j = "0ms" if request.args.get("jitter") is None else request.args.get("jitter")
            l = "0%" if request.args.get("loss") is None else request.args.get("loss")
            if node:
                if node in [node.name for node in self.net.hosts]:
                    # Relacionado as mudanças dos parametros da rede
                    print(f"alterando parametros da rede para {d} {j} {l} ...")
                    switch = self.net.getNodeByName("s1")
                    switch.cmd(f"python3 alteracao_rede.py {switch.name}-eth2 {d} {j} {l}")

                    node = self.net.getNodeByName(node)
                    # Relacionado com a captura streaming
                    video_name = f'{self.default_url.split("/")[-1]}.mp4'
                    experiment_num = len([dir for dir in listdir("videos") if dir.startswith("experiment")])+1
                    print(f"Criando Experimento-{experiment_num} ...")
                    mkdir(f"videos/experiment-{experiment_num}")
                    print("iniciando a captura do video ...")
                    cmd = f"ffmpeg -i {self.default_url} -c copy -preset ultrafast -r 60 -b 900k /save-videos/experiment-{experiment_num}/{video_name}"
                    capture_video_process = node.popen(cmd)
                    capture_video_process.wait()

                    # Retirada das Métricas de SSIM do video capturado e do recebido
                    print("iniciando a comparação dos videos ...")
                    node.cmd(f'echo "delay-{d}, jitter-{j}, loss-{l}" > /save-videos/experiment-{experiment_num}/metrics.txt')
                    cmd = f"ffmpeg-quality-metrics /save-videos/experiment-{experiment_num}/{video_name} /videos/suttle_{video_name} --metrics ssim >> /save-videos/experiment-{experiment_num}/metrics.txt"
                    node.cmd(cmd)
                    sleep(10)
                    print("finalizado!")
                    return f"metrica capturada com sucesso, verifique videos/experiment-{experiment_num}/metrics.txt\n", 200
                else:
                    return "node not found!\n", 404
            else:
                return "error node name not found\n", 404
        return app