import os
import streamlit as st
import os
from src.util import check_authentication, install_packages, plot_img, generate_code_file
st.set_page_config(page_title="Test App", layout="wide")

# check_authentication()
install_packages()
st.session_state.authenticated=True
st.session_state.username = "Học viên"

if st.session_state["authenticated"]:    
    username = st.session_state["username"]
    st.success(f"Xin chào {username}! 📢📢📢📢📢📢 Tin nóng: Tích hợp tính năng hỏi đáp, debug code với AI 🥰😍😘")

    # Cửa sổ hướng dẫn người dùng
    with st.expander("Hướng dẫn sử dụng ứng dụng 📗"):
        st.write("""
        ### Hướng dẫn sử dụng
        1. Nhấn nút run để chạy code
        2. Khi chương trình chạy thành công, nhấn "Hỏi AI🤖" để giải thích code nếu bạn chưa hiểu. Đối với lần đầu sử dụng, một thông báo "Pop up blocked" xuất hiện trên
        thanh tìm kiếm của trình duyệt, bạn phải tích vào "allow for...https://aio2024-string-python.streamlit.app/" hoặc refresh lại trang và đăng nhập lại để sử dụng tính năng này.
        3. Nút "Debug AI🤖" xuất hiện khi chương trình bạn chạy có lỗi.
        4. Kết quả và ví dụ mã sẽ hiển thị bên dưới.

        #### Lưu ý
        - Lần đầu tiên sử dụng cần cho phép trình duyệt mở cửa sổ mới như đã hướng dẫn ở bước 2
        - 1 ví dụ chỉ được sử dụng hỏi AI một lần, nếu muốn sử dụng nhiều lần thì cần nhấn nút run trên ô chứa code rồi thực hiện nhấn nút hỏi AI.
        """)

    # current_directory = os.getcwd()
    data_dir = "data/"+username+"/npt/part2/"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    st.markdown("# CÁC HÀM KHỞI TẠO NUMPY ARRAY VÀ PYTORCH/TENSORFLOW TENSOR - PHẦN 2 - AIO 2024")
    st.markdown('''## **1. Mô tả**

Khi lập trình với các thư viện Numpy, Pytorch, Tensorflow có một số cách
để nhanh chóng tạo ra các array với giá trị, kích thước khác nhau. Trong
bài tập này, chúng ta sẽ tìm hiểu các sử dụng 3 hàm **zeros**, **ones**,
**full**.

a\) ***zeros***

**zeros** là hàm thực hiện chức năng tạo array, tensor toàn giá trị 0
với đầu vào là kích thước và kiểu dữ liệu ta muốn. Cả 3 thư viện đều sử
dụng hàm trên, với cú pháp tương tự nhau.''')
    
    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/d8-zeros.png", "Minh họa và cú pháp sử dụng hàm zeros")

    st.markdown('''Nhìn chung, hàm **zeros** chủ yếu dùng để khởi tạo mảng hoặc tensor với
các giá trị 0, thường được dùng trong quá trình xây dựng các mô hình máy
học và thực hiện các phép toán số học.

b\) ***ones***

Tương tự với **zeros**, hàm **ones** tạo mảng chứa toàn số 1 với đầu vào
là kích thước do người dùng chỉ định.''')
    
    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/d8-ones.png", "Minh họa và cú pháp sử dụng hàm ones")


    st.markdown('''c\) ***full, fill***

Hàm **full** giúp chúng ta tạo array, tensor(Pytorch) với phần tử là giá
trị chỉ định, đầu vào của hàm **full** gồm kích thước array và giá trị
hằng số muốn tạo. Khác với hai thư viện trên, Tensorflow sử dụng hàm
**fill**.''')

    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/d8-full-fill.png", "Minh họa và cú pháp sử dụng hàm full/fill")

    st.markdown('''Hàm **full** với Numpy, Pytorch hay **fill** với Tensorflow giúp tạo
array hoặc tensor với kích thước và giá trị được chỉ định, có ích khi ta
cần khởi tạo các cấu trúc dữ liệu với giá trị đồng nhất.''')

    st.markdown('''## **2. Bài tập**

**Câu 1:** Hãy viết chương trình sử dụng hàm zeros tạo Numpy array,
Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là số 0 với kích
thước (3, 4)?

**Câu 2:** Hãy viết chương trình sử dụng hàm ones tạo Numpy array,
Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là số 1 với kích
thước (3, 4)?

**Câu 3:** Hãy viết chương trình tạo Numpy array, Tensorflow tensor,
Pytorch tensor chỉ chứa giá trị là số 5 với kích thước (3, 4)?''')

    st.markdown('''## **3. Đáp án**

**Câu 1:** ***zeros***

Chương trình sau tạo array với kích thước (3, 4), đối với thư viện Numpy
sử dụng cú pháp **np.zeros**, bên trong hàm này chúng ta truyền vào kích
thước array chúng ta mong muốn là (3, 4).''')

    ex_1 = '''\
# Numpy code
import numpy as np

# Tạo array toàn số 0
arr_zeros = np.zeros((3, 4))
print(arr_zeros)
'''
    generate_code_file(ex_1, 'ex_1', data_dir)
    st.markdown('''Tương tự như thư viện Numpy, Pytorch sử dụng cú pháp ***torch.zeros***''')
    ex_2 = '''\
#Pytorch code
import torch

# Tạo tensor toàn số 0
tensor_zeros = torch.zeros((3, 4))
print(tensor_zeros)
'''
    generate_code_file(ex_2, 'ex_2', data_dir)

    st.markdown('''Tương tự, Tensorflow sử dụng cú pháp **tf.zeros**''')
    ex_3 = '''\
# Tensorflow code
import tensorflow as tf

# Tạo tensor toàn số 0
tensor_zeros = tf.zeros((3, 4))
print(tensor_zeros)'''

    st.markdown('''**Câu 2:** ***ones***

Chương trình sau tạo array với kích thước (3, 4), đối với thư viện Numpy
sử dụng cú pháp ***np.ones***''')

    generate_code_file(ex_3, 'ex_3', data_dir)
    ex_4 = '''\
# Numpy code
import numpy as np

# Tạo array toàn số 1
arr_ones = np.ones((3, 4))
print(arr_ones)'''

    st.markdown('''Với Pytorch và Tensorflow cú pháp thực hiện tương tự với cú pháp torch.ones, tf.ones''')

    generate_code_file(ex_4, 'ex_4', data_dir)
    ex_5 = '''\
#PyTorch code
import torch

# Tạo tensor toàn số 1
tensor_ones = torch.ones((3, 4))
print(tensor_ones)
'''
    generate_code_file(ex_5, 'ex_5', data_dir)

    ex_6 = '''\
#TensorFlow code    
import tensorflow as tf

# Tạo tensor toàn số 1
tensor_ones = tf.ones((3, 4))
print(tensor_ones)'''
    generate_code_file(ex_6, 'ex_6', data_dir)
    
    st.markdown('''**Câu 3:** ***full, fill***

Chương trình sau tạo array với kích thước (3, 4), giá trị hằng số là 5.
Đối với thư viện Numpy sử dụng cú pháp ***np.full***''')
    ex_7 = '''\
# Numpy code
import numpy as np

# Tạo array toàn số 5
arr_full = np.full((3, 4), 5)
print(arr_full)'''
    
    generate_code_file(ex_7, 'ex_7', data_dir)
    
    st.markdown('''Tương tự như thư viện Numpy, Pytorch sử dụng cú pháp ***torch.full***''')


    ex_8 = '''\
#Pytorch code
import torch

# Tạo tensor toàn số 5
tensor_full = torch.full((3, 4), 5)
print(tensor_full)'''

    st.markdown('''Khác với hai thư viện trên, Tensorflow sử dụng hàm **fill** để tạo một
tensor với giá trị được chỉ định.''')

    generate_code_file(ex_8, 'ex_8', data_dir)
    ex_9 = '''\
# Tensorflow code
import tensorflow as tf

# Tạo tensor toàn số 5
tensor_full = tf.fill((3, 4), 5)
print(tensor_full)'''