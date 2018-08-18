# from moviepy.video.VideoClip import TextClip
from moviepy.editor import *
# File saved as C:\Users\wazih\AppData\Local\imageio\ffmpeg\ffmpeg-win32-v3.2.4.exe.

files = os.listdir("C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\test_clips")
for file in files:  
  clip = VideoFileClip("C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\test_clips\\"+file)
  
  # get index of the _ and then [:_ index]
  if '_' in file:
    slice_point = file.index('_')
    txt_clip = TextClip("    twitch.tv/"+file[:slice_point], fontsize=30, color='purple').set_pos("left").set_duration(14)
  else:
    slice_point = file.index('.mp4')
    txt_clip = TextClip("    twitch.tv/"+file[:slice_point], fontsize=30, color='purple').set_pos("left").set_duration(14)

  img_clip = ImageClip("./twitch_logo_32.png").set_pos("left").set_duration(11)

  new_text_clip = (txt_clip.fx( vfx.fadein, duration=3, initial_color=0.5 ))
  final_clip = CompositeVideoClip([clip, new_text_clip, img_clip])
  final_clip.write_videofile(
    "C:\\Users\\wazih\\Desktop\\courses\\youtab_highligh_gen\\edited_clips\\"+file, 
    fps=30
  )






