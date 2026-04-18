#1
from datetime import datetime

def qancha_vaqt_otdi(sana_str):
    sana = datetime.strptime(sana_str, "%Y-%m-%d")
    hozir = datetime.now()
    farq = hozir - sana
    return farq.days

#2
def orta(a, b):
    return (a + b) / 2

#3
def bosh_harf_katta(soz):
    return soz.capitalize()
  
#4
def teskari_son(son):
    return int(str(son)[::-1])

#5
def juftlar(royxat):
    return [x for x in royxat if x % 2 == 0]



