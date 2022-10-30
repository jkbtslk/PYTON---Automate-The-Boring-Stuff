#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):

	# Download the page.
	print(f"Downloading {url}...")
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")

	# Find the URL of the comic image.
	elem = soup.select("#comic img")
	if elem == []:
		print("Couldn't download the image.")
	else:
		comicUrl = "https:" + elem[0].get("src")

		# Download the image.
		print(f"Downloading image {comicUrl}.")
		res = requests.get(comicUrl)
		res.raise_for_status()

		# Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	# Get the Prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')