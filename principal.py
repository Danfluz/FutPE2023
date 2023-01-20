from bs4 import BeautifulSoup
import requests

def f_elenco(grupo):
    lista = []
    for jogadores in grupo:
        jogadores = jogadores.find_all('div', class_='staff')
        for jogador in jogadores:
            diciotemp = {}
            nome = jogador.text[1:-7]
            idade = jogador.text[-7:]
            link = jogador.find('div', class_='text').findNext('a')['href']
            foto = jogador.find('div', class_='photo')['style']
            foto = foto.split("'")[1]
            diciotemp['Nome'] = nome
            diciotemp['Idade'] = idade
            diciotemp['Link'] = link
            diciotemp['Foto'] = foto
            lista.append(diciotemp)

    return lista

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}
# content = requests.get('https://www.ogol.com.br/equipa.php?id=240756&search=1',headers=headers)
content = requests.get('https://www.ogol.com.br/player.php?id=264743&epoca_id=152',headers=headers)
print(content)
content = content.content

site = BeautifulSoup(content, 'html.parser')
print(site.prettify())
"""Isso abaixo é o código funcionando normalmente para pegar todo o elenco, se o link do content for o link do time"""
# squad = site.find('div', id='team_squad')
# grupos = squad.find_all('div', class_='innerbox')
#
# gole = list(grupos[0])[1:]
# defe = list(grupos[1])[1:]
# meia = list(grupos[2])[1:]
# atac = list(grupos[3])[1:]
#
# elenco = {
#     'Goleiros' : f_elenco(gole),
#     'Defensores' : f_elenco(defe),
#     'Meias' : f_elenco(meia),
#     'Atacantes' : f_elenco(atac),
# }
#
# print(elenco)