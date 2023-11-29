import subprocess
import sys

def __init__(self):
    subprocess.run(["python3", "show_interfaces.py"])

def alterar_parametros_rede(interface=None, delay=None, jitter=None, loss=None):
    
    comando = ['tc', 'qdisc', 'change', 'dev', interface]

    if delay:
        comando.extend(['root', 'netem', 'delay', delay])

    if jitter:
        comando.extend([jitter])

    if loss:
        comando.extend(['loss', loss])

    subprocess.run(comando)

if __name__ == '__main__':
    interface = sys.argv[1] if len(sys.argv) > 1 else None
    delay = sys.argv[2] if len(sys.argv) > 2 else None
    jitter = sys.argv[3] if len(sys.argv) > 3 else None
    loss = sys.argv[4] if len(sys.argv) > 4 else None

    alterar_parametros_rede(interface, delay, jitter, loss)
