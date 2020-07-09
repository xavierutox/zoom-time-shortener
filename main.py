import cv2
import numpy as np
from scipy.io import wavfile
import math
from audiotsm import phasevocoder
from shutil import copyfile, rmtree
import sys
import subprocess
from pytube import YouTube
import os
import glob
from bs4 import BeautifulSoup
import requests
 
def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    returnlist=[]
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            link = (domain + href + '\n')
            returnlist.append(link)
    return returnlist
def createPath(s):
    #assert (not os.path.exists(s)), "The filepath "+s+" already exists. Don't want to overwrite it. Aborting."

    try:  
        os.mkdir(s)
    except OSError:  
        assert False, "Creation of the directory %s failed. (The TEMP folder may already exist. Delete or rename it, and try again.)"

def deletePath(s): # Dangerous! Watch out!
    try:  
        rmtree(s,ignore_errors=False)
    except OSError:  
        adsasdads=1
def downloadFile(url):
    if YouTube(url).streams.get_by_itag(22):
        name = YouTube(url).streams.get_by_itag(22).download()
    else:
        name = YouTube(url).streams.first().download()
    name2 = name.split('/')
    name = name2[-1]
    newname = name.replace(' ','_')
    os.rename(name,newname)
    newname=newname.split("/")
    return newname[-1]

deletePath("output")
deletePath("out")

createPath("output")
createPath("out")
nombre=input("Ingrese un nombre para el archivo. Debe terminar en .mp4: ")
test = None
previo=input("Ingrese 'nuevo' si va a procesar videos nuevos o 'procesado' si va a usa un video ya procesado: ")
if previo=='nuevo':
    f= open("mylist.txt","w+")
    listvideo=[]
    while(test!="end"):
        test = input("Ingresa 'youtube', 'file' o end: ")
        if test=="youtube":
            p= input("Es un 'video' o una 'playlist'?: ")
            if p == 'video':
                listvideo.append(downloadFile(input("Ingresa el link: ")))
            else:
                playlisturl=input('Ingresa el link: ')
                plist= getPlaylistLinks(playlisturl)
                for i in plist:
                    listvideo.append(downloadFile(i))
        elif test=="file":
            listvideo.append(input("ingresa el nombre del archivo: "))
    checkfps=input("Todos los videos tienen el mismo framerate? (s/n): ")
    if checkfps=='n':
        for i in listvideo:
            subprocess.call("ffmpeg -i "+i+" -filter:v fps=fps=25 25_"+i,shell=True)
            subprocess.call("rm "+i,shell=True)
            linea="file '25_"+i+"'\n"
            f.write(linea)
    else:
        for i in listvideo:
            linea="file '"+i+"'\n"
            f.write(linea)
    f.close()
    subprocess.call("ffmpeg -f concat -safe 0 -i mylist.txt -c copy merged.mp4",shell=True)
    for i in listvideo:
        subprocess.call("rm 25_"+i,shell=True)
    videoFile = "merged.mp4"
else:
    videoFile=input("ingresa el nombre del archivo: ")
try:
    subprocess.call("python3 splitter.py -f "+videoFile+" -s 60 -v h264",shell=True)

    f = sorted(glob.glob("output/*.mp4"))
    for i in f:
        subprocess.call("python3 jump.py --input_file "+i+" --output_file out/"+i.strip("output/")+" --sounded_speed 1 --silent_speed 999999 --frame_margin 4 --frame_rate 25", shell=True)

    outfiles= sorted(glob.glob("out/*.mp4"))
    f= open("mylist.txt","w+")
    for i in outfiles:
        linea="file '"+i+"'\n"
        f.write(linea)
    f.close()
    subprocess.call("ffmpeg -f concat -safe 0 -i mylist.txt -c copy "+nombre,shell=True)
except OSError:
    subprocess.call("python3 jump.py --input_file "+videoFIle+" --output_file "+nombre+" --sounded_speed 1 --silent_speed 999999 --frame_margin 4 --frame_rate 25", shell=True)
deletePath("output")
deletePath("out")
