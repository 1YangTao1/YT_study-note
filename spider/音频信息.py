import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

mus = res.content

music = open('music.mp3','wb')
music.write(mus)
music.close()
