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

system("docker stop $(docker ps -aq)")
system("docker rm $(docker ps -aq)")


setLogLevel('info')
net = Containernet(controller=Controller)

info('*** Adding controller\n')
c0 = net.addController('c0')

info('*** add ffmpeg server \n')
d1 = net.addDocker('d1', dimage="server")
d2 = net.addDocker('d2', dimage="server",environment={"DISPLAY":getenv("DISPLAY"), "XDG_RUNTIME_DIR":"/run/user/1000"},volumes=[f"{getenv('HOME')}/.Xauthority:/root/.Xauthority", "/tmp/.X11-unix:/tmp/.X11-unix"])
d3 = net.addDocker('d3', dimage="server",environment={"DISPLAY":getenv("DISPLAY"), "XDG_RUNTIME_DIR":"/run/user/1000"},volumes=[f"{getenv('HOME')}/.Xauthority:/root/.Xauthority", "/tmp/.X11-unix:/tmp/.X11-unix"])


info('*** Adding switches\n')
s1 = net.addSwitch('s1')
ap_arg = {"client_isolation": True}
ap1 = net.addAccessPoint('ap1', ssid="simpletopo", mode="g", channel="5", **ap_arg)

info('*** Creating links\n')
net.configureNodes()
net.addLink(d1, s1)
net.addLink(d2, s1)
net.addLink(s1, ap1)

info('*** Starting network\n')
net.build()
c0.start()
s1.start( [c0] )
ap1.start( [c0] )

d1.popen("./mediamtx")

info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
