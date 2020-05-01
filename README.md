# zoom-time-shortener
Un sencillo script de python usado para unir varias clases y luego eliminar el tiempo muerto de estas clases (silencios al inicio, durante la clase y al final de esta). Consiguiendo asi, reducir gran parte de tiempo dedicado a ver las clases y permitiendo varias de estas en una unica sesion de estudio
# Requisitos previos
- sudo apt-get install ffmpeg o https://windowsloop.com/install-ffmpeg-windows-10/ (en caso de usar windows)
- sudo pip3 install -f requirements.txt o su equivalente en windows
- un video.mp4 o el link a un video mayor a 16minutos

# ¿Como utilizar?
- python3 main.py
- Seguir las instrucciones indicadas en la consola
# ¿Nuevo o procesado?
Lo recomendable es utilizar siempre "nuevo" ya que de esta forma podrás seleccionar varios archivos, ademas de descargar directamente las clases publicadas en youtube desde la consola de comandos.
En caso de utilizar una unica clase y que ya cuentes con el .mp4 descargado desde antes, entonces elige procesado
# ¿Como funciona 'nuevo'?

 - Busca y descarga los videos en caso de seleccionar la opción
   "youtube", de lo contrario te pedirá los videos que ya se encuentren
   en la carpeta y desees procesar
  - Una vez realizado esto te preguntara si los videos tienen el mismo framerate, en caso de no serlo o de no saberlo escribe "N" y el programa convertirá todos los videos a 25fps (la velocidad de fps de un video grabado desde zoom)
  - Una vez realizado lo anterior unirá los videos en un unico video ya procesado.
  # ¿ Como funciona 'procesado'?
- Procesado asume que el proceso anterior ya se realizo o que estas trabajando con un video grabado desde zoom (25fps)
# ¿Y ahora qué?
- El programa procederá a separar el video en fragmentos de 1,000 segundos y los guardará en la carpeta temporal "OUTPUT"
- Luego, por cada uno de los videos en OUTPUT, ejecutara el script jump.py y guardará el video en "OUT"
- Posteriormente, se uniran cada uno de los fragmentos del video en OUT y se guardará en el directorio principal (donde estan los .py)
- Finalmente, se borraran todos los ficheros temporales (solo en ubuntu)
# ¿Cuanto tarda esto?
- Depende bastante del cpu y dependiendo del uso que le des (si unes varios videos, si tienes un único video procesado o si es necesario convertir todos los videos a una misma tasa de fotogramas).
- Es recomendable ejecutarlo mientras ves otra clase ya procesada o durante la noche mientras no estas ocupando tu computador.
- En caso de querer procesar varios videos, utiliza distintas intancias del programa guardas en carpetas distintas (el numero de programas que puedes correr dependerá de tu RAM)
# Creditos
- Jumpcutter: https://github.com/carykh/jumpcutter
- VideoSplitter: https://github.com/akaraspt/video-splitter
