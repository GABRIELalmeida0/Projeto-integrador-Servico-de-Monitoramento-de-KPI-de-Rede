from icmplib import ping
from prometheus_client import Gauge, generate_latest
from threading import Thread, Event
from flask import Flask
from time import sleep


class Monitor():
    def __init__(self, host_ip="10.0.0.3", count=10):
        self.__host_ip = host_ip
        self.__count = count
        self.gauge = Gauge("Metrics_KPIs", "KPIs capturadas da conexão", ['name_client', 'type_metric'])

    def __capture_metrics(self):
        host = ping(self.__host_ip, self.__count, interval=0.1, timeout=1)
        self.gauge.labels(self.__host_ip, "delay").set(host.avg_rtt)
        self.gauge.labels(self.__host_ip, "jitter").set(host.jitter)
        self.gauge.labels(self.__host_ip, "packet_loss").set(host.packet_loss)

    def __loop_metric(self, event):
        while True:
            if event.is_set():
                break
            self.__capture_metrics()
            sleep(3)

    def start_app(self):
        app = Flask("__APP__")

        self.event = Event()
        self.__thread_get_metric = Thread(target=self.__loop_metric, args=(self.event,))
        self.__thread_get_metric.start()

        @app.route("/metrics", methods=["GET"])
        def metrics():
            return generate_latest()

        return app

    def __del__(self):
        self.event.set()
        self.__thread_get_metric.join()


Monitor().start_app().run(host="0.0.0.0")
