import streamlit as st
import os
import sys
from aio_code_editor import ui, st_connect_data

st.set_page_config(page_title="Test App", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"]=False

if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
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
    
    st.markdown("# IF-ELIF-ELSE, LOOP IN PYTHON - AIO 2024")
    
    # Câu lệnh điều kiện
    st.markdown('''## 1. Câu lệnh điều kiện if-elif-else''')
    st.markdown('''Ví dụ 1.1: Chương trình kiểm tra số nào lớn hơn''')
    
    ex_1 = '''#ai vietnam
a = 10
b = 42
if b > a:
  print("b is greater than a")
    '''
    ui.code_io(ex_1, key='ex1', file_name=data_dir+"/ex1.py",type_out="python" )
    
    ########################1.2#####################################################
    
    st.markdown(r'''Ví dụ 1.2: Chương trình kiểm tra số chẵn lẻ''')
    
    ex_2 = '''#ai vietnam
number = 5

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

    '''
    ui.code_io(ex_2, key='ex2', file_name=data_dir+"/ex2.py",type_out="python" )
    
    ############################################1.3###############################
    st.markdown(r'''Ví dụ 1.3: Kiểm tra nhiều điều kiện với if-elif-else''')
    ex_3 = '''#ai vietnam
temperature = 25

if temperature > 30:
    print("The weather is hot")
elif 20 <= temperature <= 30:
    print("The weather is warm")
else:
    print("The weather is cold")


    '''
    ui.code_io(ex_3, key='ex3', file_name=data_dir+"/ex3.py",type_out="python" )
    
    ############################################1.4###############################
    st.markdown(r'''Ví dụ 1.4: Sử dụng câu lệnh điều kiện lồng nhau để kiểm tra số đó là số 0 hay số âm, số dương.''')
    ex_4 = '''#ai vietnam
num = -5

if num >= 0:
    if num == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")

    '''
    ui.code_io(ex_4, key='ex4', file_name=data_dir+"/ex4.py",type_out="python" )
    
    ############################################Phan 2 Vong lap for###############################
    
    st.markdown(r'''## 2. Vòng lặp for''')
    st.markdown('''Ví dụ 2.1: Ví dụ vòng lặp for sau sẽ thực hiện hiển thị giá trị của biến i 5 lần, mỗi lần lặp i sẽ nhận 1 giá trị trong range(5) từ 0 đến 4.''')
    
    ex_21 = '''#ai vietnam
for i in range(5):
    print(i)
    '''
    ui.code_io(ex_21, key='ex21', file_name=data_dir+"/ex21.py",type_out="python" )
    
    
    st.markdown(r'''Ví dụ 2.2: Ví dụ sử dụng vòng lặp for qua từng phần tử trong list.''')              
    
    ex_22 = '''#ai vietnam
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    '''
    ui.code_io(ex_22, key='ex22', file_name=data_dir+"/ex22.py")
    
    
    st.markdown(r'''Ví dụ 2.3: Vòng lặp for với continue''')

    ex_23 = """#ai vietnam
for i in range(5):
    if i == 2:
        continue
    print(i)
    """
    ui.code_io(ex_23, key='ex23', file_name=data_dir+"/ex23.py")


    st.markdown(r'''Ví dụ 2.4: Vòng lặp for với break''')
                
    ex_24 = """#ai vietnam
for i in range(5):
    if i == 2:
        break
    print(i)
    """
    ui.code_io(ex_24, key='ex24', file_name=data_dir+"/ex24.py")
    
    # Phan 3: While
    
    st.markdown(r'''## 3. Vòng lặp while''')
    st.markdown('''Ví dụ 3.1: Ví dụ chương trình in ra màn hình các số từ 1 đến 5:''')
    
    ex_3_1 = '''#ai vietnam
i = 1
while i <= 5:
    print(i)
    i += 1
    '''
    ui.code_io(ex_3_1, key='ex31', file_name=data_dir+"/ex3_1.py",type_out="python" )
    
    st.markdown(r'''Ví dụ 3.2: Chương trình vòng lặp while với break''')
    
    ex_3_2 = '''#ai vietnam
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
    '''
    ui.code_io(ex_3_2, key='ex32', file_name=data_dir+"/ex3_2.py",type_out="python" )
    
    st.markdown(r'''Ví dụ 3.3: Chương trình sử dụng continue để bỏ qua lần lặp của những trường hợp i chia hết cho 2''')
    
    
    ex_3_3 = '''#ai vietnam
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    '''
    ui.code_io(ex_3_3, key='ex33', file_name=data_dir+"/ex3_3.py",type_out="python" )
    
    