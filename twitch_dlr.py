import credentials
import requests, urllib.request,pprint

headers = {
  'Accept': 'application/vnd.twitchtv.v5+json',
  'Client-ID': credentials.twitch_cid
}

# getting the game id - league: 497467, fortnite: 33214
clip_req = requests.get("https://api.twitch.tv/kraken/games/top", headers=headers).json()

pprint.pprint(clip_req)