import credentials
import requests
import urllib.request
import pprint
import pyperclip


headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': credentials.twitch_cid
}

# getting the game id - league: 21779, fortnite: 33214
#clip_req = requests.get("https://api.twitch.tv/kraken/games/top", headers=headers).json()


# loops through streamer names and spits out twitch download links for thier clips from the twitch top 24h
counter = 0
video_duration = 0
# array for channel corresponding with vid
corr_channel = []
dl_links = []

while video_duration < 900:
  counter = counter + 1
  for streamer in credentials.league_names:
    clip_req = requests.get(
        "https://api.twitch.tv/kraken/clips/top?channel="+streamer+"&period=day", headers=headers).json()
    # checking for empty arrays with no clips    
    if len(clip_req['clips'][counter-1:counter]) != 0:
        clip = clip_req['clips'][counter-1:counter][0]
        thumb = clip['thumbnails']['medium']
        channel_name = clip['broadcaster']['name']
        title = clip['title']
        clip_duration = clip['duration']
        slice_index = thumb.index('-preview-')
        twitch_dl_url = thumb[:slice_index] + ".mp4"
        # pprint.pprint(clip)

        video_duration = video_duration + clip_duration
        # checking for duplicate channel names for title of download video
        if channel_name in corr_channel:
          corr_channel = corr_channel + [channel_name+"_1"]
        else:
          corr_channel = corr_channel + [channel_name]  
        # array for download links  
        dl_links.append(twitch_dl_url)

        # print("clip duration: ", clip_duration, "\tvideo duration: ", video_duration, "minutes: ",video_duration/60)
        # print(channel_name, twitch_dl_url)
        # print(counter)


for i in range(len(dl_links)):
  output_dl_path = credentials.dl_test_folder + corr_channel[i] + ".mp4" 
  print("downloading...", corr_channel[i])
  urllib.request.urlretrieve(dl_links[i], output_dl_path)
  
print('Finished downloading all', len(dl_links), 'videos')  
