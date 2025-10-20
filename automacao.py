import pyautogui as pa
import time
from interacao_xl import dados

def pausa(tempo):
    time.sleep(tempo)

pa.click(x=-1110, y=450)
pausa(2)
dados()