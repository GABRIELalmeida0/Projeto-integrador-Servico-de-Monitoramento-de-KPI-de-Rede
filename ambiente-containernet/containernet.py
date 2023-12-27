#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from os import *
from subprocess import Popen
from containernet.net import Containernet
from mininet.node import Controller
from containernet.cli import CLI
from containernet.link import TCLink
from mininet.log import info, setLogLevel
from app import App

system("docker stop $(docker ps -aq)")
system("docker rm $(docker ps -aq)")


setLogLevel('info')
net = Containernet(controller=Controller)

info('*** Adding controller\n')
c0 = net.addController('c0')

info('*** add ffmpeg server \n')
d1 = net.addDocker('d1', dimage="streaming-server")
envs = {"DISPLAY":getenv("DISPLAY"), "XDG_RUNTIME_DIR":"/run/user/1000"}
volumes = [f"{getenv('HOME')}/.Xauthority:/root/.Xauthority",
           "/tmp/.X11-unix:/tmp/.X11-unix",
           f"{getcwd()}/videos/:/save-videos/"]
d2 = net.addDocker('d2', dimage="streaming-server",environment=envs,volumes=volumes)

info('*** Adding switches\n')
s1 = net.addSwitch('s1')

info('*** Creating links\n')
net.configureNodes()
net.addLink(d1, s1)
net.addLink(d2, s1)
#net.addLink(s1, ap1)

info('*** Starting network\n')  
net.build()
c0.start()
s1.start( [c0] )

d1.popen("./mediamtx")

info('*** Running CLI\n')
app = App(net, default_url="rtsp://10.0.0.1:8554/launch480p15s")
app.start_app().run()
CLI(net)
info('*** Stopping network')
net.stop()
