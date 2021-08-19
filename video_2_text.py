"""Este programa permite convertir el audio de videos en archivos de texto"""

# Importing required modules
import wave
import math
import contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import time
from tkinter import *




def selecUbicacionDest():
    


    
    video_file_name = ubic.get()


    audioclip = AudioFileClip(video_file_name)
    audioclip.write_audiofile(transcribed_audio_file_name)


    with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
        frames = f.getnframes()# Number of frames		
        rate = f.getframerate() # Rate of frames per second
        duration = frames / float(rate) # Total number of frames divided by the rate = duration
        
        

    global total_duration
    total_duration = math.ceil(duration / 60)
    

    

    ventana.quit()

    ventana.geometry("400x150")

    mensaje = Label(ventana ,text="Ingrese la ruta donde desea guardar el archivo\n Ej: C:/User/Documents")

    boxUbicacion = Entry(ventana, textvariable=ubic, width = 50)
    ubic.set('')
    botonA = Button(ventana, text="Aceptar", command=colocarNombreArch)
    botonC = Button(ventana, text="Cancelar", command=salir)    
    
    mensaje.place(x=10, y=10)
    boxUbicacion.place(x=10, y=50)
    botonA.place(x=90, y=80)
    botonC.place(x=250, y=80)
    
    ventana.mainloop()


      
def colocarNombreArch():
    global destination_folder
    destination_folder = ubic.get()
    
    ventana.quit()
    
    ventana.geometry("400x150")

    mensaje = Label(ventana,text="Ingrese el nombre del archivo a guardar\n Ej: texto.txt")

    boxUbicacion = Entry(ventana, textvariable=ubic, width = 50)
    ubic.set('')
    botonA = Button(ventana, text="Aceptar", command=traducir)
    botonC = Button(ventana, text="Cancelar", command=salir)

    mensaje.place(x=10, y=10)
    boxUbicacion.place(x=10, y=50)
    botonA.place(x=90, y=80)
    botonC.place(x=250, y=80)
    ventana.mainloop()
      


def traducir():
    global destination_folder
    file_name = ubic.get()
    user_path = f"{destination_folder}/{file_name}"
    print(user_path)

    animation = "|/-\\|/-\\"
    idx = 0
    while idx < 11:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.3)

    language = 'es-ES'
    r = sr.Recognizer()
    global total_duration

    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i*60, duration=60)
            # Create file or append new data if already existing
            f = open(user_path, 'w')
            # Write into file what the Google API transcribes
            f.write(r.recognize_google(audio, language=language))
            f.write(' ')  # Leave spaces between two batches/ sentences
        f.close()
    print('Video convertido con exito')
        

def salir():
    global ventana
    ventana.destroy()
    sys.exit()
 
destination_folder = ''
transcribed_audio_file_name = 'videos/transcribed_speech.wav'
total_duration = 0;
ventana = Tk()
ubic = StringVar()
ventana.geometry("400x150")
mensaje = Label(ventana,text="Ingrese la ruta del video a convertir:\n Ej: C:/User/Documents/video.mp4")
boxUbicacion = Entry(ventana, textvariable=ubic, width = 63)
botonA = Button(ventana, text="Aceptar", command=selecUbicacionDest)
botonC = Button(ventana, text="Cancelar", command=salir)
mensaje.place(x=10, y=10)
boxUbicacion.place(x=10, y=50)
botonA.place(x=90, y=80)
botonC.place(x=250, y=80)
ventana.mainloop()


