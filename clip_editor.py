# from moviepy.video.VideoClip import TextClip
from moviepy.editor import *
from random import randint
# File saved as C:\Users\wazih\AppData\Local\imageio\ffmpeg\ffmpeg-win32-v3.2.4.exe.

files = os.listdir("C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\test_clips")
counter = 0

# # halfing the number of files because goign to iterate 2 files at a time
# while (counter < len(files)/2):
#   # iterating two files at a time
for file in files:
  try:
    clip = VideoFileClip("C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\test_clips\\"+file)
  except OSError:
    print("Another bullshit os error")

  # get index of the _ and then [:_ index]
  if '_' in file:
    slice_point = file.index('_')
    txt_clip = TextClip("    twitch.tv/"+file[:slice_point],
                        fontsize=30, color='purple').set_pos("left").set_duration(12)
  else:
    slice_point = file.index('.mp4')
    txt_clip = TextClip("    twitch.tv/"+file[:slice_point],
                        fontsize=30, color='purple').set_pos("left").set_duration(14)

  img_clip = ImageClip("./twitch_logo_32.png").set_pos("left").set_duration(11)

  new_text_clip = (txt_clip.fx(vfx.fadein, duration=3, initial_color=0.5))
  final_clip = CompositeVideoClip([clip, new_text_clip, img_clip])
  try:
    final_clip.write_videofile("C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\new_edited_clips\\"+file)
  except OSError:
    print("Bullshit Os Error")  
  
  # counter = counter + 2
  # print('counter is now', str(counter))



