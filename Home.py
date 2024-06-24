import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide"   
)


st.markdown('''# Danh sách các bài viết Numpy-Pytorch-Tensorflow: ''')
st.page_link('pages/1_Numpy_Pytorch_Tensorflow_part1.py', label="NUMPY ARRAY VÀ PYTORCH/TENSORFLOW TENSOR - PHẦN 1", icon="📚")
st.page_link('pages/2_Numpy_Pytorch_Tensorflow_part2.py', label="NUMPY ARRAY VÀ PYTORCH/TENSORFLOW TENSOR - PHẦN 2", icon="📚")
st.page_link('pages/3_Numpy_Pytorch_Tensorflow_part3.py', label="NUMPY ARRAY VÀ PYTORCH/TENSORFLOW TENSOR - PHẦN 3", icon="📚")