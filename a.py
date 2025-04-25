import streamlit as st
import os
from PIL import Image, UnidentifiedImageError

# 获取当前文件夹中的所有文件
files = os.listdir('.')

# 过滤出图片和视频文件
image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
video_files = [f for f in files if f.endswith('.mp4')]

st.title('叮叮')


# 使用 Streamlit 的 columns 方法来在一行中展示多张图片
cols = st.columns(3)  # 假设一行展示三张图片
for i, image_file in enumerate(image_files):
    with cols[i % 3]:
        try:
            img = Image.open(image_file)
            # 直接使用原始图片展示
            st.image(img, use_container_width=True)
            # 提供查看原始大小图片的选项

        except UnidentifiedImageError:
            continue



# 使用 Streamlit 的 columns 方法来在一行中展示多个视频
cols = st.columns(3)  # 假设一行展示三个视频
for i, video_file in enumerate(video_files):
    with cols[i % 3]:
        st.video(video_file)
