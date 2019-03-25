# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 08:20:58 2019

@author: mh70
"""

from moviepy.editor import *
clip = VideoFileClip('../../CZ_TFS_SPO_orig.mp4', audio=False)


#%%
clip.save_frame(r"../../out1.png", t=8.1)
clip.save_frame(r"../../out2.png", t=22)
clip.save_frame(r"../../out3.png", t=30)
clip.save_frame(r"../../out5.png", t=34)

clip.save_frame(r"../../out6.png", t=95)

#%%
clip.save_frame(r"../../out7.png", t=43)


#%%

clip1 = clip.subclip(0,2)
clip1a = clip.subclip(4,18)
clip2 = clip.subclip(21,23)
clip3 = clip.subclip(23,30)
clip4 = clip.subclip(30,33)
clip5 = clip.subclip(33,38)



clip6 = clip.subclip(43,95)
clip7 = clip.subclip(95,)

#%%



#%%
clip_ins_intro_1 = ImageClip("../../img_ins_intro_1.png", duration=2)
clip_ins_1 = ImageClip("../../img_ins_1.png", duration=2)
clip_ins_new = ImageClip("../../img_ins_new.png", duration=2)
clip_ins_1st_screen = ImageClip("../../img_ins_1st_screen.png", duration=4)

clip_ins_2 = ImageClip("../../img_ins_2.png", duration=2)
clip_ins_3 = ImageClip("../../img_ins_3.png", duration=3)
clip_ins_4 = ImageClip("../../img_ins_4.png", duration=2)

clip_ins_5 = ImageClip("../../img_ins_5.png", duration=2)

clip_ins_3rd_screen = ImageClip("../../img_ins_3rd_screen.png", duration=3)

clip_ins_under_con = ImageClip("../../img_ins_under_con.png", duration=4)
clip_ins_wait = ImageClip("../../img_ins_wait.png", duration=1)

clip_ins_att_0 = ImageClip("../../img_ins_att_0.png", duration=2)
clip_ins_att_1 = ImageClip("../../img_ins_att_1.png", duration=1)
clip_ins_att_2 = ImageClip("../../img_ins_att_2.png", duration=1)
clip_ins_att_3 = ImageClip("../../img_ins_att_3.png", duration=1)
clip_ins_att_4 = ImageClip("../../img_ins_att_4.png", duration=1)
clip_ins_att_5 = ImageClip("../../img_ins_att_5.png", duration=1)

clip_ins_conn_1 = ImageClip("../../img_ins_conn_1.png", duration=1)
clip_ins_conn_2 = ImageClip("../../img_ins_conn_2.png", duration=1)
clip_ins_conn_3 = ImageClip("../../img_ins_conn_3.png", duration=1)
clip_ins_conn_4 = ImageClip("../../img_ins_conn_4.png", duration=1)
clip_ins_conn_5 = ImageClip("../../img_ins_conn_5.png", duration=1)
clip_ins_conn_6 = ImageClip("../../img_ins_conn_6.png", duration=1)
clip_ins_conn_7 = ImageClip("../../img_ins_conn_7.png", duration=1)
clip_ins_conn_8 = ImageClip("../../img_ins_conn_8.png", duration=1)
clip_ins_conn_9 = ImageClip("../../img_ins_conn_9.png", duration=1)

img_ins_conn_bee_bonita = ImageClip("../../img_ins_conn_bee_bonita.png", duration=5)

#%%
wrk_out = concatenate_videoclips([
                                clip_ins_intro_1,
                                clip1,
                                clip_ins_1, 
                                clip_ins_new,
                                clip_ins_1st_screen,
                                clip1a,                                
                                clip2, 
                                clip_ins_2, 
                                clip3,                                
                                clip4,
                                clip_ins_3,
                                clip_ins_4,
                                clip5,
                                
                                clip_ins_3rd_screen,
                                ])

#%%
wrk_out.write_videofile(r"../../out.mp4")








#%%
final = concatenate_videoclips([
                                clip_ins_intro_1,
                                clip1,
                                clip_ins_1, 
                                clip_ins_new,
                                clip_ins_1st_screen,
                                clip1a,                                
                                clip2, 
                                clip_ins_2, 
                                clip3,                                
                                clip4,
                                clip_ins_3,
                                clip_ins_4,
                                clip5,
                                
                                clip_ins_3rd_screen,
                                
                                clip6,
                                
                                clip_ins_under_con,
                                clip_ins_wait,
                                
                                clip_ins_att_0,
                                clip_ins_att_1,
                                clip_ins_att_2,
                                clip_ins_att_3,
                                clip_ins_att_4,
                                clip_ins_att_5,
                                
                                clip_ins_wait,
                                                                                                
                                clip_ins_conn_1,
                                clip_ins_conn_2,
                                clip_ins_conn_3,
                                clip_ins_conn_4,
                                clip_ins_conn_5,
                                clip_ins_conn_6,
                                clip_ins_conn_7,
                                clip_ins_conn_8,
                                clip_ins_conn_9,
                                
                                img_ins_conn_bee_bonita,
                                
                                clip7,
                                clip_ins_intro_1,
                                ])

#%%

final.write_videofile(r"../../out.mp4")
