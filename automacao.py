import pyautogui as pa
import time
from interacao_xl import dados

def pausa(tempo):
    time.sleep(tempo)

pa.press('win')
pa.write("Anydesk")
pausa(2)
pa.press('enter')
pausa(2)
pa.click(x=-406, y=37)
pausa(2)
pa.click(x=-527, y=121)
pausa(2)
pa.click(x=-1617, y=40)
pausa(2)
pa.click(x=-1110, y=450)
pausa(2)
dados()