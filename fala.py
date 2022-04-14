from gtts import gTTS # importamos o modúlo gTTS
voz = gTTS("Olá, tudo bem?", lang ="pt") # guardamos o nosso texto na variavel voz
voz.save("voz.mp3") #salvamos com o comando save em mp3