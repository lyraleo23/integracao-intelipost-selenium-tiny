from tiny_web import start_tiny, integrar_intelipost
from bot_web import open_page
import os
from dotenv import load_dotenv

load_dotenv()

user_miligrama = os.getenv('USER_MILIGRAMA')
user_mili_nordeste = os.getenv('USER_MILI_NORDESTE')
password_tiny = os.getenv('PASSWORD')

def main():
    contas_tiny = ['miligrama_nordeste', 'miligrama']
    transportadoras_miligrama = [
        '6', #Total Express
        '7', #Correios
        '8', #Envie Agora
        '25', #Jadlog
        '35', #Quality
        '36', #Entrega Full - Norte e Nordeste
        '37', #Total Express - Norte e Nordeste
        '39', #Total Express - Manual
    ]

    transportadoras_mili_nordeste = [
        '5', #Total Express
        '6', #Correios
    ]

    for conta in contas_tiny:
        print(conta)
        if conta == 'miligrama':
            user = user_miligrama
            transportadoras = transportadoras_miligrama
        elif conta == 'miligrama_nordeste':
            user = user_mili_nordeste
            transportadoras = transportadoras_mili_nordeste
        password = password_tiny

        driver = start_tiny(user, password)

        for transportadora in transportadoras:
            try:
                # Ir para Expedição
                url = 'https://erp.tiny.com.br/expedicao'
                open_page(driver, url)
                integrar_intelipost(driver, transportadora)
            except:
                driver = start_tiny(user, password)
                continue









    

main()