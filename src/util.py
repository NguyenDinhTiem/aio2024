import os
import textwrap
from PIL import Image
from aio_code_editor import ui, st_connect_data
import streamlit as st


def check_authentication():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        display_login_form()


def display_login_form():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st_connect_data.login_form(
            create_username_placeholder="Tạo tên đăng nhập của bạn, ví dụ 'nguyenvana'",
            create_password_placeholder="Đặt mật khẩu của bạn",
            guest_submit_label="Khách đăng nhập"
        )


def install_packages():
    try:
        import tensorflow as tf
    except ImportError:
        os.system('pip install "tensorflow-cpu==2.14.0"')

    try:
        import torch
    except ImportError:
        os.system("pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cpu")

def generate_code_file(code, key, data_dir):
    dedented_code = textwrap.dedent(code)
    file_name = data_dir + key + ".py"
    ui.code_io(dedented_code, key=key, file_name=file_name, type_out="python", show_now=True)

def plot_img(image_url, caption, width=720, ratio=[1, 2, 1]):
    col1, col2, col3 = st.columns(ratio)
    with col2:
        st.image(image_url,caption, output_format="PNG", width=width)