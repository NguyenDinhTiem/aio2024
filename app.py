import streamlit as st
import os
import sys
from aio_code_editor import ui, st_connect_data

st.set_page_config(page_title="Test App", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"]=False

if not st.session_state["authenticated"]:
    st_connect_data.login_form(
        create_username_placeholder="Tạo tên đăng nhập của bạn, ví dụ 'nguyenvana'",
        create_password_placeholder="Đặt mật khẩu của bạn",
        guest_submit_label="Khách đăng nhập")


if st.session_state["authenticated"]:    
    username = st.session_state["username"]
    st.success(f"Xin chào {username}!")
    
    # current_directory = os.getcwd()
    data_dir = "data/"+username
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    st.button("Đăng xuất", on_click=st.session_state.clear)
    
    st.markdown("# LOOP PYTHON - AIO 2024")

    #Phan 1 Vong lap for
    
    st.markdown(r'''## 1. Vòng lặp for
                
                Ví dụ 1.1: Ví dụ vòng lặp for sau sẽ thực hiện hiển thị giá trị của biến i 5 lần, mỗi lần lặp i sẽ nhận 1 giá trị trong range(5) từ 0 đến 4.
                
                ''')
    
    
    ex_1 = '''#ai vietnam
for i in range(5):
    print(i)
    '''
    ui.code_io(ex_1, key='ex1', file_name=data_dir+"/ex1.py",type_out="python" )
    
    
    st.markdown(r'''Ví dụ 1.2: Ví dụ sử dụng vòng lặp for qua từng phần tử trong list.
                
                ''')
    
    ex_2 = '''# Vòng lặp for với danh sách
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    '''
    ui.code_io(ex_2, key='ex2', file_name=data_dir+"/ex2.py")
    
    
    st.markdown(r'''Ví dụ 1.3: Vòng lặp for với continue
                
                ''')
    ex_3 = """for i in range(5):
    if i == 2:
        continue
    print(i)
    """
    ui.code_io(ex_3, key='ex3', file_name=data_dir+"/ex3.py")


    st.markdown(r'''Ví dụ 1.4: Vòng lặp for với break
                
                ''')
    ex_4 = """for i in range(5):
    if i == 2:
        break
    print(i)
    """
    ui.code_io(ex_4, key='ex4', file_name=data_dir+"/ex4.py")
    
    # Phan 2: While
    
    st.markdown(r'''## 2. Vòng lặp while
                
                Ví dụ 2.1: Ví dụ chương trình in ra màn hình các số từ 1 đến 5:

                ''')
    
    
    ex_2_1 = '''i = 1
while i <= 5:
    print(i)
    i += 1
    '''
    ui.code_io(ex_2_1, key='ex21', file_name=data_dir+"/ex2_1.py",type_out="python" )
    
    st.markdown(r'''Ví dụ 2.2: Chương trình vòng lặp while với break''')
    
    
    ex_2_2 = '''#ai vietnam
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
    '''
    ui.code_io(ex_2_2, key='ex22', file_name=data_dir+"/ex2_2.py",type_out="python" )
    
    st.markdown(r'''Ví dụ 2.2: Chương trình sử dụng continue để bỏ qua lần lặp của những trường hợp i chia hết cho 2''')
    
    
    ex_2_3 = '''#ai vietnam
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    '''
    ui.code_io(ex_2_3, key='ex23', file_name=data_dir+"/ex2_3.py",type_out="python" )
    
    