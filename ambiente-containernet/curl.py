from requests import *
import numpy as np

list_of_number = []
for d in range(0, 201, 10):
    for j in range(0, 201, 10):
        for l in np.arange(0.0, 3.1, 0.5):
            network = {"node_name":"d2", "delay":f"{d}ms", "jitter":f"{j}ms", "loss":f"{l}%"}
            list_of_number.append(network)
list_of_number = np.array(list_of_number)

for request_params in list_of_number:
    print(f"Iniciando requisição: delay={request_params['delay']}, jitter={request_params['jitter']}, loss={request_params['loss']} .")
    #experiment = get("http://localhost:5000/capture_streaming", params=request_params)
    #print("Experimento Finalizado!.")












