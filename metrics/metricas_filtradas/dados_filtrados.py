import pandas as pd

class Dados_filtrados():
    def __init__(self,csv_packt_loss=None, csv_dellay=None, csv_jitter=None):
        self.df_packet_loss = pd.read_csv(csv_packt_loss)
        self.df_delay = pd.read_csv(csv_dellay)
        self.df_jitter = pd.read_csv(csv_jitter)

    def media_geral_estado_rede(self):
        # Delay
        df = self.df_delay

        df['values'] = df['values'].replace('ms', '', regex=True).astype(float)

        media = df['values'].mean()

        print(f'A média de Delay é: {media} ms')

        ##################################################################################################################

        #Jitter

        df = self.df_jitter

        df['values'] = df['values'].replace('ms', '', regex=True).astype(float)

        media = df['values'].mean()

        print(f'A média de Jitter é: {media} ms')

        ##################################################################################################################

        #Loss

        df = self.df_packet_loss

        def percent_to_float(percent_str):
            return float(percent_str.strip('%'))

        if '%' in df['values'].iloc[0]:
            df['values'] = df['values'].apply(percent_to_float)

        media = df['values'].mean()

        print(f'A média do Loss é: {media}%')
        





    def media_por_tempo(self,inicio_intervalo=None,fim_intervalo=None):

        #Delay
        df = df = self.df_delay

        df['Time'] = pd.to_datetime(df['Time'])
        df['values'] = df['values'].replace(' ms', '', regex=True).astype(float)

        df_intervalo = df[(df['Time'] >= inicio_intervalo) & (df['Time'] <= fim_intervalo)] # Filtrar o DataFrame para incluir apenas as linhas dentro do intervalo de tempo

        media_intervalo = df_intervalo['values'].mean()

        print(f'A média do Delay no intervalo de tempo é: {media_intervalo} ms')

        ##################################################################################################################

        #Jitter
        df = self.df_jitter

        df['Time'] = pd.to_datetime(df['Time'])
        df['values'] = df['values'].replace(' ms', '', regex=True).astype(float)

        df_intervalo = df[(df['Time'] >= inicio_intervalo) & (df['Time'] <= fim_intervalo)] # Filtrar o DataFrame para incluir apenas as linhas dentro do intervalo de tempo

        media_intervalo = df_intervalo['values'].mean()

        print(f'A média do Jitter no intervalo de tempo é: {media_intervalo} ms')

        ##################################################################################################################

        #Loss
        df = self.df_packet_loss

        df['Time'] = pd.to_datetime(df['Time'])

        def percent_to_float(percent_str):
            return float(percent_str)

        df['values'] = df['values'].apply(percent_to_float)


        df_intervalo = df[(df['Time'] >= inicio_intervalo) & (df['Time'] <= fim_intervalo)]# Filtrar o DataFrame para incluir apenas as linhas dentro do intervalo de tempo

        media_intervalo = df_intervalo['values'].mean()

        print(f'A média do Loss no intervalo de tempo é: {media_intervalo}%')
