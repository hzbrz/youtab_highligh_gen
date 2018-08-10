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
# loop through channel names from credentials.py 
# loop in the order above and get 1 clip from each channel from that day
# end loop when the added duration of all vids is above 15mins


vid_dur_in_sec = 0
counter = 0
video_duration = 0

while video_duration < 15.0:
  counter = counter + 1
  for streamer in credentials.league_names:
    clip_req = requests.get(
            "https://api.twitch.tv/kraken/clips/top?channel="+streamer+"&period=day", 
            headers=headers
            ).json()
    if len(clip_req['clips'][counter-1:counter]) != 0:
      clip = clip_req['clips'][counter-1:counter][0]
      thumb = clip['thumbnails']['medium']
      title = clip['title']
      clip_duration = clip['duration']
      slice_index = thumb.index('-preview-')
      twitch_dl_url = thumb[:slice_index] + ".mp4"
      # pprint.pprint(clip)
      
      vid_dur_in_sec = vid_dur_in_sec + clip_duration
      video_duration = vid_dur_in_sec / 60
      print(clip_duration, video_duration)
      print(title)
      print(twitch_dl_url)
      # print(counter)



             
# clips = clip_req['data']

# for clip in clips:
#   thumb = clip['thumbnail_url']
#   slice_index = thumb.index('-preview-')
#   twitch_dl_url = thumb[:slice_index] + ".mp4"
#   print(twitch_dl_url)

