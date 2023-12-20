from dados_filtrados import Dados_filtrados

data = Dados_filtrados(csv_packt_loss= 'Packet Loss-data-2023-12-20 12 31 45.csv', csv_dellay='Delay-data-2023-12-20 12 31 20.csv', csv_jitter='Jitter-data-2023-12-20 12 31 34.csv')
data.media_geral_estado_rede()
data.media_por_tempo(inicio_intervalo="2023-12-20 06:31:00", fim_intervalo="2023-12-20 06:44:30")