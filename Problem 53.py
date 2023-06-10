import gtts

x = gtts.gTTS(lang="en", text="Hello world", slow=False)
x.save("Text to audio.mp3")
print(x)