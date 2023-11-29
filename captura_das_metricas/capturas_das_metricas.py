from icmplib import ping
from flask import Flask, jsonify

class Monitor():
    def __init__(self, host_ip="8.8.8.8", count=10):
        self.__host_ip = host_ip
        self.__count = count

    def __capture_metrics(self):
        host = ping(self.__host_ip, self.__count, interval=0.5, timeout=1)
        delay_avg = host.avg_rtt
        jittter = host.jitter
        packet_loss = host.packet_loss
        return {self.__host_ip: {"delay_avg":delay_avg, "jitter": jittter, "packet_loss": packet_loss}} 

    def start_app(self):
        app = Flask("__APP__")

        @app.route("/metrics", methods=["GET"])
        def metrics():
            return jsonify(self.__capture_metrics())
                
        return app
    
Monitor().start_app().run(host="0.0.0.0")