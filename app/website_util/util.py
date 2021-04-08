import requests, json

base_url = 'https://www2.kickassanime.rs'

def query_anime(name):
    
    res = requests.get(f'{base_url}/search?q={name}').text
    
    res = res[res.index('[{'):res.index('}]')+2]
    
    data = json.loads(res)
    
    return data

def get_episode(anime, ep):
    res = requests.get(f'{base_url}{anime}').text
    res = res[res.index(':[{')+1:res.index('}]')+2]

    ep_data = json.loads(res)

    for episode in ep_data:
        
        if f'Episode {ep}' == episode['epnum']:
            return episode['slug']
