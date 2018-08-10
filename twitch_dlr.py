import credentials
import requests, urllib.request,pprint, pyperclip

headers = {
  'Accept': 'application/vnd.twitchtv.v5+json',
  'Client-ID': credentials.twitch_cid
}

# getting the game id - league: 21779, fortnite: 33214
#clip_req = requests.get("https://api.twitch.tv/kraken/games/top", headers=headers).json()

# https://github.com/amiechen/twitch-batch-loader/blob/master/batchloader.py
# https://dev.twitch.tv/docs/v5/reference/clips/#get-clip
# loop through channel names: loltyler1, LCK1, TFBlade, imaqtpie, Trick2g, LLStylez, Yassuo, Shiphtur, C9Sneaky, hashinshin, Gosu, Doublelift, Nightblue3, Voyboy, nalcs, midbeast
# loop in the order above and get 1 clip from each channel from that day
# end loop when the added duration of all vids is above 15mins


clip_req = requests.get(
          "https://api.twitch.tv/kraken/clips/top?channel=loltyler1", 
           headers=headers
          ).json()

# clips = clip_req['data']

# for clip in clips:
#   thumb = clip['thumbnail_url']
#   slice_index = thumb.index('-preview-')
#   twitch_dl_url = thumb[:slice_index] + ".mp4"
#   print(twitch_dl_url)

pprint.pprint(clip_req['clips'])
