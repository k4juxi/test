import time
import os


saat = int(input("Saat giriniz: "))
dakika = int(input("Dakika giriniz: "))

while True:
    tut = time.localtime(time.time())
    if saat == tut.tm_hour and dakika == tut.tm_min:
#         import webbrowser
        # strURL = "https://www.youtube.com/watch?v=p4yxn8ZahPI"
        # webbrowser.open(strURL, new=2)
        #
        # SendKeys.SendKeys("{SPACE}")
        print("alarm çaldı")
        break
    else:
        pass
print("başarılı")

# os.system(google)
# importing webbrowser python module
# import webbrowser
# #Assigning URL to be opened
# strURL = "https://www.youtube.com/watch?v=p4yxn8ZahPI"
# #Open url in default browser
# webbrowser.open(strURL, new=2)
#

# import pafy
# import vlc
#
# url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url
