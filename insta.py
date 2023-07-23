import requests
import json

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
	    "X-RapidAPI-Key": "42827f4771mshc9142bfba648c81p11f080jsn874801fab7f8",
	    "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
    if rest['Type'] == 'Post-Image':
        dict['type'] = 'image'
        dict['media'] = rest['media']
        return dict
    elif rest['Type'] == 'Post-Video':
        dict['type'] = 'video'
        dict['media'] = rest['media']
        return dict
    elif rest['Type'] == 'Carousel':
        dict['type'] = 'carousel'
        dict['media'] = rest['media']
        return dict
    else:
        return 'Bad'