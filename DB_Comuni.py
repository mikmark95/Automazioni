import pandas as pd
import numpy as np
import csv
from geopy.distance import geodesic
from geopy import Nominatim
import openpyxl


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


def associa_sito(file_comuni, file_siti, file_output, path_risultato):
    '''Funzione che legge uno per uno tutti i comuni presenti in un database, e gli associa in un altro file la corrispondenza comune-sito rinex.'''
    #leggo i file di input
    df_comuni = pd.read_excel(file_comuni)
    df_siti = pd.read_excel(file_siti)
    df_output = pd.read_excel(file_output)


    #Itero su ogni comune
    for ind_comuni, riga_comuni in df_comuni.iterrows():
        res = ('', 0)

        comune = riga_comuni['comune']
        #eatraggo le coordiante di quel comune
        lat_comune = riga_comuni['latitude']
        long_comune = riga_comuni['longitude']

        #itero su ogni sito
        for ind_siti, riga_siti in df_siti.iterrows():

            #estraggo le coordinate di ogni sito
            lat_siti = riga_siti['Latitude']
            long_siti = riga_siti['Longitude']

            #calcola la distanza
            distanza = distanza_AB((lat_comune,long_comune),(lat_siti,long_siti))

            #aggiorno il risultato
            if res[1]== 0:
                sito = riga_siti['Name']
                res = (sito, distanza)

            elif distanza < res[1]:
                sito = riga_siti['Name']
                res = (sito, distanza)

        df_output.at[ind_comuni,'Comune']=comune
        df_output.at[ind_comuni,'Sito']=res[0]
        df_output.at[ind_comuni,'Distanza']=res[1]
        print(df_output['Comune']+ ' Terminato!')

    df_output.to_excel(path_risultato, index=False)





if __name__=='__main__':
    pass

    # lst =[
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_ABRUZZO.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_BASILICATA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_CALABRIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_CAMPANIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_EMILIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_FRIULI.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_LAZIO.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_LIGURIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_LOMBARDIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_MARCHE.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_MOLISE.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_PIEMONTE.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_PUGLIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_SARDEGNA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_SICILIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_TOSCANA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_TRENTINO.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_UMBRIA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_VALLE AOSTA.xlsx",
    #     "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\risultato_VENETO.xlsx"
    #     ]
    # out = "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\ELENCO SITI-COMUNI\\Risultato_ITALIA.xlsx"
    #
    # unisci_excell(lst,out)


    # #-----------------------------------------------------------------------------------------------------------------------------------------
    #
    # comune = 'VENETO'
    # file_comuni = f"C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\\Comune_Regione_Filtrato_{comune}_OUTPUT.xlsx"
    # file_siti = "C:\\Users\\mmarchetti\Desktop\\ELENCO STAZIONI RINEX\\Elenco siti-Rinex_EXCELL.xlsx"
    # file_output = "C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\ELENCO SITI-COMUNI\\output_1.xlsx"
    # path_risultato = f"C:\\Users\\mmarchetti\\Desktop\\ELENCO STAZIONI RINEX\\ELENCO COMUNI\\OUTPUT\ELENCO SITI-COMUNI\\risultato_{comune}.xlsx"
    #
    #
    # associa_sito(file_comuni,file_siti,file_output,path_risultato)
    #
    #
    # #-----------------------------------------------------------------------------------------------------------------------------------------
    #
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


