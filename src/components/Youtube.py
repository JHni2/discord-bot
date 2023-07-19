import requests
import json

def get_youtube_search_results():
    url = "https://www.googleapis.com/youtube/v3/search"
    q = "윤하"
    params = {
        "part": "snippet",
        "maxResults": 25,
        "q": q,
        "type": "video",
        "key": "AIzaSyCi0Jiy9oVTXV6eoaWnPUTC-7_LMU-nEcA",
    }

    response = requests.get(url, params=params)
    response_data = response.json()

    print((json.dumps(response_data, indent=2)))
    return response_data

get_youtube_search_results()
