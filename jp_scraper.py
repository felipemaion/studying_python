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
    # print(personagem)
    # print("Personagem: {}".format(personagem.strip("/")))

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
        site = requests.get(link, headers = headers)
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
    
    # print("Ending {}".format(personagem))
    # pbar.update()
    # pbar.update(len(personagens)/len(records)) 
    return results
    

personagens = get_personagens()


# pbar = tqdm(total=len(personagens), desc="Buscando voice lines")

records = []
# with Pool(200) as p:
#     records = p.map(get_voices, personagens)
#     pbar.update(len(personagens)/len(records)) 
# pbar.close()  
    # get_voices(personagens)

def imap_unordered_bar(func, args, n_processes = 200):
    p = Pool(n_processes)
    res_list = []
    with tqdm(total = len(args), desc="Buscando voices line") as pbar:
        for i, res in tqdm(enumerate(p.imap_unordered(func, args))):
            pbar.update()
            res_list.append(res)
    pbar.close()
    p.close()
    p.join()
    return res_list

records = imap_unordered_bar(get_voices, personagens)

with open('all.csv', mode='w') as file: 
    file_w = csv.writer(file, delimiter=',') 
    file_w.writerow(['Personagem', 'Fala']) 

    for conteudo in records: 
        for personagem, fala in conteudo: 
            file_w.writerow([personagem, fala]) 


print("Scrapping finalizado.")
end = time.time()
print("Total time: {}".format(end - start))