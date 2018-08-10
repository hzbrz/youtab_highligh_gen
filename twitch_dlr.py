import credentials
import requests, urllib.request,pprint

headers = {
  'Client-ID': credentials.twitch_cid
}

# getting the game id - league: 21779, fortnite: 33214
#clip_req = requests.get("https://api.twitch.tv/kraken/games/top", headers=headers).json()

clip_req = requests.get("https://api.twitch.tv/helix/clips?game_id=21779&first=5", headers=headers).json()

pprint.pprint(clip_req)