import time
import os
import webbrowser

saat = int(input("Saat giriniz: "))
dakika = int(input("Dakika giriniz: "))

while True:
    tut = time.localtime(time.time())


    if saat == tut.tm_hour and dakika == tut.tm_min:
        strURL = "https://www.youtube.com/watch?v=p4yxn8ZahPI"
        webbrowser.open(strURL, new=2)
        time.sleep(10)
        break
    else:
        pass
print("başarılı")
