import webbrowser

idol = ["아이유"," BTS","레드벨벳","태연"]
base_url = "https://www.google.com/search?q="
for i in idol:
    #webbrowser.open(base_url+i)
    #webbrowser.open(f"https://www.google.com/search?q={i}")
    webbrowser.open("https://www.google.com/search?q={}".format(i))