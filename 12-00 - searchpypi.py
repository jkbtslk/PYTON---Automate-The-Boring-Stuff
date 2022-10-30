#! python3
# searchpypi.py  - Opens several search results.

import requests, bs4, sys, webbrowser

if len(sys.argv) < 2:
    print("Manual - <script> <phrase to search>")
else:
    phrase = sys.argv[1]

    res = requests.get("https://pypi.org/search/?q=" + "".join(phrase))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(".package-snippet")
    numOpen = min(5, len(elems))
    for i in range(numOpen):
        urlToOpen = "https://pypi.org" + elems[i].get('href')
        print("Opening ", urlToOpen)
        webbrowser.open(urlToOpen)


