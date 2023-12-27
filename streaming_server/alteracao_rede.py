import subprocess
import sys


def alterar_parametros_rede(interface=None, delay=None, jitter=None, loss=None):
    # try add interface if get a error, then they don't show the error and redirect the error output to stderr
    subprocess.Popen(f"tc qdisc add dev {interface} root netem delay 0ms".split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
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
