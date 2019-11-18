import requests 
from bs4 import BeautifulSoup
import docx
from tqdm import tqdm
import os
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

personagens = []
link1 = "https://paladins.gamepedia.com/Category:Voice_lines"
site = requests.get(link1)
soup = BeautifulSoup(site.content, "html.parser")
for f in soup.find_all("div", class_="mw-category-group"):
    for e in f.find_all("a"):
        if e.has_attr('href'):
            personagens.append(e.attrs["href"])

lista = ['10', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '11', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6','11.7', '11.8', '11.9', '11.10', '11.11', '11.12', '11.13', '11.14', '11.15', '11.16', '11.17', '11.18', '11.19', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6','12.7', '12.8', '12.9', '12.10', '12.11', '12.12', '12.13', '12.14']
pbar = tqdm(total=100, desc="Buscando voice lines")
for personagem in personagens:
    doc = docx.Document()
    voices = []
    try:
        link = "https://paladins.gamepedia.com{}".format(str(personagem))
        site = requests.get(link)
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
        doc.add_paragraph(voice.strip("Play"))
    pbar.set_description(desc="Buscando voice lines de: {}".format(personagem.strip("/").split("_voice_lines")[0]), refresh=True)
    pbar.update(100/len(personagens))       
    doc.save("{}.docx".format(personagem.strip("/")))
pbar.close()
print("Scrapping finalizado.")
end = time.time()
print("Total time: {}".format(end - start))