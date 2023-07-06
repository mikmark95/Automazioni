import pandas as pd
import numpy as np
import csv
from geopy.distance import geodesic
from geopy import Nominatim

"""
Questo insieme di funzioni di utilità servono per leggere un elenco di comuni da un foglio excell
per poi aggiungere an ogni riga la colonna relativa alle coordinate geografiche.
Si presentano funzioni che estraggono coordinate dal nome del comune, fondono una lista di file excell\csv 
in un unico file file excell\csv
"""

def ottieni_coordinate(comune):
    geolocator = Nominatim(user_agent="nome_utente")
    location = geolocator.geocode(comune + ", Italy")
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

def unisci_csv(lista_file: list[str], path_out: str) -> 'file CSV':
    '''Funzione che legge una lista di percorsi file csv e li unisce in un unico file'''
    result = pd.concat([pd.read_csv(f) for f in lista_file], ignore_index=True)
    file = result.to_csv(path_out)
    return file, path_out

def unisci_excell(file_list, output):
    # Leggi il primo file Excel per inizializzare il DataFrame di output
    df_merged = pd.read_excel(file_list[0])

    # Itera sugli altri file Excel e uniscili al DataFrame di output
    for file in file_list[1:]:
        df = pd.read_excel(file)
        df_merged = pd.concat([df_merged, df], ignore_index=True)

    # Salva il DataFrame fuso in un unico file Excel
    df_merged.to_excel(output, index=False)


def inserisci_colonne_excell(path_input, colonna):
    df = pd.read_excel(path_input)
    df[colonna] = ""
    for index, row in df.iterrows():
        df.at[index, colonna] = ""
    df.to_excel(path_input, index=False)


def inserici_coordinate_DB(path_input,path_output):
    df = pd.read_excel(path_input)
    df['coordinate'] = ""
    df['latitude'] = "" #prova
    df['longitude'] = "" #prova


    for index, row in df.iterrows():
        comune = str(row['comune'])

        print(index,comune, type(comune))
        coordinate = ottieni_coordinate(comune)
        if coordinate is not None:
            df.at[index, 'coordinate'] = coordinate
            df.at[index, 'latitude'] = coordinate[0] #prova
            df.at[index, 'longitude'] = coordinate[1] #prova

    df.to_excel(path_output, index=False)


def distanza_AB(a:tuple[float,float], b:tuple[float,float]):
    return geodesic(a,b).km

if __name__=='__main__':


    pass

    '''
    EXCELL_REGIONE                          EXCELL_SITI
    lat_comune, long_comune                 lat_sito, long_sito

    for comune in range(n.comuni):
        res = ('', 0)
        for sito in range(n.siti):
            distanza = calcola_dst(lat_comune, long_comune, lat_sito_long_sito)
            if distanza < res[1]:
                res = (sito, distanza)
        modifica_sito(comune,res)
    print('TERMINATO')

    '''

    #--------------------------------------------------------------------------------------

    #
    # regione='VENETO'
    #
    # path_input =f"C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\Comune_Regione_Filtrato_{regione}.xlsx"
    # path_output =f"C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\Comune_Regione_Filtrato_{regione}_OUTPUT.xlsx"
    #
    # df = pd.read_excel(path_input)
    # df['coordinate'] = ""
    # df['latitude'] = "" #prova
    # df['longitude'] = "" #prova
    #
    #
    # for index, row in df.iterrows():
    #     comune = str(row['comune'])
    #
    #     print(index,comune, type(comune))
    #     coordinate = ottieni_coordinate(comune)
    #     if coordinate is not None:
    #         df.at[index, 'coordinate'] = coordinate
    #         df.at[index, 'latitude'] = coordinate[0] #prova
    #         df.at[index, 'longitude'] = coordinate[1] #prova
    #
    # df.to_excel(path_output, index=False)

    #---------------------------------------------------------------------------------------


