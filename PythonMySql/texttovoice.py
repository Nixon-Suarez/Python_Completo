import pyttsx3

decir = input("ingrese el texto que quiere que diga: ")
engine = pyttsx3.init()

voices = engine.getProperty('voices') # cambiar la voz
engine.setProperty("voice", voices[1].id)

# engine.setProperty("rate", 125) # velocidad de la voz 
# engine.setProperty("volume", 100.0) # volumen de la voz 
engine.say(decir)
engine.runAndWait() # reprodce la voz
