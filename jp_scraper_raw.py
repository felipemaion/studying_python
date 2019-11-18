import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
from multiprocessing import Pool
import csv
import time

# try:
#     import easygui 
# except:
#     os.system("pip install easygui")
start = time.time()
dir = os.getcwd() #easygui.diropenbox()
os.chdir(dir)
if not os.path.exists("voicelines"): 
    os.mkdir("voicelines")
os.chdir(dir + "/voicelines")



def get_personagens():
    personagens = []
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }
    link1 = "https://paladins.gamepedia.com/Category:Voice_lines"
    site = requests.get(link1, headers = headers)
    soup = BeautifulSoup(site.content, "html.parser")
    for f in soup.find_all("div", class_="mw-category-group"):
        for e in f.find_all("a"):
            if e.has_attr('href'):
                personagens.append(e.attrs["href"])
    return personagens

def get_voices(personagem):
    DATA = {
    ":authority": "paladins.gamepedia.com",
    ":method": "GET",
    ":path": "/A-bomb-inable_Bomb_King_voice_lines",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "cookie":" __cfduid=d86280e5dd81689f7e485fff1f602fea91552289659; _ga=GA1.2.77390328.1552289661; _gid=GA1.2.729937787.1552289661; cdmgeo=br; __gads=ID=2ea02dc01169da8f:T=1552289662:S=ALNI_MZ_10hWmyZI7CwVr8fVgJWn_ZsRcw; i10cfd=1",
    "if-modified-since": "Sun, 10 Mar 2019 23:42:42 GMT",
    "referer": "https://paladins.gamepedia.com/Category:Voice_lines",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }

    DATA[':path']= personagem
    # print("Getting Personagem: {}".format(personagem.strip("/")))

    lista = ['10', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '11', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6','11.7', '11.8', '11.9', '11.10', '11.11', '11.12', '11.13', '11.14', '11.15', '11.16', '11.17', '11.18', '11.19', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6','12.7', '12.8', '12.9', '12.10', '12.11', '12.12', '12.13', '12.14']

    
    # for personagem in personagens:
    # doc = docx.Document()
    results = []
    voices = []
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
        
        link = "https://paladins.gamepedia.com{}".format(str(personagem))
        site = requests.get(link, headers = headers, data=DATA)
        soup = BeautifulSoup(site.content, "html.parser")
    except:
        pass

    for c in range(len(soup.find_all('li'))):
            if "Play" in soup.find_all("li")[c].get_text():
                voices.append((soup.find_all("li")[c].get_text()))

    for i in lista:
        for a in voices:
            if i in a:
                voices.remove(a)

    for voice in voices: 
        results.append([personagem.strip("/"),voice.strip("Play")])
    
    print("Coletado voice de: {}".format(personagem.strip("/")))
    return results
    

personagens = get_personagens()

records = []
with Pool(200) as p:
    records = p.map(get_voices, personagens)

with open('all.csv', mode='w') as file: 
    file_w = csv.writer(file, delimiter=',') 
    file_w.writerow(['Personagem', 'Fala']) 

    for conteudo in records: 
        for personagem, fala in conteudo: 
            file_w.writerow([personagem, fala]) 


print("Scrapping finalizado.")
end = time.time()
print("Total time: {}".format(end - start))