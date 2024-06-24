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
    st.markdown("# CÁC HÀM KHỞI TẠO NUMPY ARRAY VÀ PYTORCH/TENSORFLOW TENSOR - PHẦN 3 - AIO 2024")

    st.markdown('''## **1. Mô tả**

Trong bài tập này, chúng ta tiếp tục tìm hiểu các hàm có chức năng tạo
array, tensor đặc biệt. Chúng ta sẽ tìm hiểu và sử dụng các hàm
**arange**, **range**, **eye**, và **random**.

a\) ***arange, range***

Trong Numpy, Pytorch, hàm **arange** được sử dụng để tạo một mảng chứa
dãy số có giá trị tăng dần với khoảng cách cố định. Trong Tensorflow
chúng ta sẽ sử dụng hàm **range**. Cú pháp như sau:''')
    
    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/range.png", "Minh họa và cú pháp sử dụng hàm arange")
    
    st.markdown('''Hàm **arange** (hoặc **range** trong Tensorflow) rất hữu ích khi ta muốn
tạo ra một dãy số tăng dần với các giá trị cách đều nhau.

b\) ***eye***

Hàm **eye** được sử dụng để tạo ma trận đơn vị, tức là một ma trận vuông
có tất cả các phần tử trên đường chéo chính có giá trị 1, các phần tử
còn lại là 0. Cú pháp sử dụng như sau:''')
    
    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/eye.png", "Minh họa và cú pháp sử dụng hàm eye")

    st.markdown('''
Hàm **eye** giúp tạo array hoặc tensor đơn vị, đặc biệt hữu ích trong
nhiều ứng dụng toán học và xử lý dữ liệu.

c\) ***random***

Trong thư viện Numpy, Pytorch cung cấp hàm **rand** để tạo mảng với các
giá trị ngẫu nhiên trong khoảng \[0.0, 1.0) với kích cỡ (shape) được chỉ
định. Ngoài ra có thể sử dụng hàm **randint** để tạo mảng với các số
nguyên ngẫu nhiên. Đối với thư viện Tensorflow chúng ta sử dụng hàm
**random.uniform**.''')
    
    plot_img("https://ia800408.us.archive.org/33/items/npt_20240623/random.png", "Minh họa và cú pháp sử dụng hàm random", width=840)
    
    st.markdown('''
Các hàm này giúp việc tạo dữ liệu ngẫu nhiên trở nên dễ dàng trong quá
trình phát triển mô hình Machine Learning, Deep Learning.''')

    st.markdown('''## **2. Bài tập**

Câu 1: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch
tensor trong khoảng \[0, 10) với step=1?

Câu 2: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch
tensor là ma trận đơn vị với kích thước (3, 3).

Câu 3: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch
tensor ngẫu nhiên trong khoảng giá trị \[0, 1\] với kích thước (3, 4).
Tiếp theo hãy tạo array, tensor với các giá trị là số nguyên trong
khoảng \[-10, 10\]. Lưu ý trong bài tập này, các bạn sẽ sử dụng seed =
2024 để dảm bảo ra kết quả giống đáp án, cách sử dụng như sau:

``` {.python language="Python"}
# Numpy code
import numpy as np
np.random.seed(2024)

# Pytorch code
import torch
torch.manual_seed(2024)

# Tensorflow code
import tensorflow as tf
tf.random.set_seed(2024)
```
''')
    st.markdown('''## **3. Đáp án**

Câu 1: ***arange, range***

Trong numpy chúng ta sử dụng hàm **np.arange** ''')

    ex_1 = '''\
# Numpy code
import numpy as np

# Tạo array trong khoảng [0, 10), 
# bước nhảy 1
arr_arange = np.arange(10)
print(arr_arange)'''

    generate_code_file(ex_1, "ex_1", data_dir)

    st.markdown('''Trong PyTorh, để tạo tensor chứa dãy số, ta sử dụng hàm
**torch.arange**:''')

    ex_2 = '''\
#Pytorch code
import torch

# Tạo tensor trong khoảng [0, 10), 
# bước nhảy 1
tensor_arange = torch.arange(10)
print(tensor_arange)'''

    generate_code_file(ex_2, "ex_2", data_dir)

    st.markdown('''Trong Tensorflow, ta có thể sử dụng hàm **tf.range** để thực hiện chức
năng tương tự:''')

    ex_3 = '''\
# Tensorflow code
import tensorflow as tf

# Tạo tensor trong khoảng [0, 10),
# bước nhảy 1
tensor_arange = tf.range(10)
print(tensor_arange)'''

    generate_code_file(ex_3, "ex_3", data_dir)

    st.markdown('''Câu 2: ***eye***

Trong numpy chúng ta sử dụng hàm np.eye để tạo ma trận đơn vị, trong đó
giá trị chúng ta truyền vào là số lượng hàng của ma trận đầu ra, số
lượng cột mặc định bằng số lượng hàng, nếu muốn số lượng cột khác bạn
cần truyền vào hàm eye số lượng cột chỉ định.''')
        
    ex_4 = '''\
# Numpy code
import numpy as np

# Tạo array với đường chéo chính là 1, 
# còn lại là 0
arr_eye = np.eye(3)
print(arr_eye)
'''
    generate_code_file(ex_4, 'ex_4', data_dir)
    
    st.markdown('''Trong Pytorch, để tạo tensor đơn vị, ta sử dụng hàm **torch.eye**:''')

    ex_5 = '''\
#Pytorch code
import torch

# Tạo tensor với đường chéo chính là 1, 
# còn lại là 0    
tensor_eye = torch.eye(3)
print(tensor_eye)'''

    generate_code_file(ex_5, 'ex_5', data_dir)
    
    st.markdown('''Trong Tensorflow, hàm **eye** cũng được sử dụng để tạo constant tensor
đơn vị:''')

    ex_6 = '''\
# Tensorflow code
import tensorflow as tf

# Tạo tensor với đường chéo chính là 1,
# còn lại là 0
tensor_eye = tf.eye(3)
print(tensor_eye)'''

    generate_code_file(ex_6, 'ex_6', data_dir)
    
    st.markdown('''Câu 3: ***random***
                
Trong Numpy, chúng ta sẽ sử dụng hàm **random.rand** để tạo mảng với các
giá trị ngẫu nhiên trong khoảng giá trị mặc định là \[0, 1). Để tạo mảng
với giá trị ngẫu nhiên là số nguyên chúng ta dùng **random.randint**,
khi sử dụng hàm này ta cần truyền vào khoảng giá trị lấy ngẫu nhiên và
kích thước đầu ra mong muốn.''')

    ex_7 = '''\
#Numpy code
import numpy as np

# Đặt seed để đảm bảo kết quả ngẫu nhiên 
# có thể tái tạo được
np.random.seed(2024)

# Tạo một mảng với các giá trị ngẫu nhiên trong khoảng [0, 1) với kích thước (3, 4)
arr_rand = np.random.rand(3, 4)
print("Mảng ngẫu nhiên trong khoảng [0, 1):\\n", arr_rand)

# Tạo một mảng với các giá trị ngẫu nhiên trong khoảng [-10, 10)
arr_randint = np.random.randint(-10, 10, size=(3, 4))
print("Mảng ngẫu nhiên trong khoảng [-10, 10):\\n", arr_randint)'''

    generate_code_file(ex_7, 'ex_7', data_dir)
    st.markdown('''Trong Pytorch, các hàm tương tự cũng có sẵn thông qua module torch.
**torch.rand** tạo tensor với các giá trị ngẫu nhiên từ phân phối đều
trong khoảng \[0.0, 1.0), **torch.randint** dùng để tạo tensor với các
số nguyên ngẫu nhiên trong một khoảng cụ thể.''')

    ex_8 = '''\
# Pytorch code
import torch

# Thiết lập seed để đảm bảo kết quả ngẫu nhiên có thể tái tạo được
torch.manual_seed(2024)

# Tạo tensor với các giá trị ngẫu nhiên trong khoảng [0, 1) với kích thước (3, 4)
tensor_rand = torch.rand((3, 4))
print("Tensor ngẫu nhiên trong khoảng [0, 1):\\n", tensor_rand)

# Tạo tensor với các giá trị ngẫu nhiên trong khoảng [-10, 10)
tensor_randint = torch.randint(-10, 10, size=(3, 4))
print("Tensor ngẫu nhiên trong khoảng [-10, 10):\\n", tensor_randint)'''
    generate_code_file(ex_8, 'ex_8', data_dir)
    st.markdown('''Trong Tensorflow, ta cũng có các hàm tương tự là **tf.random.uniform**
để tạo tensor với các giá trị ngẫu nhiên trong khoảng \[0.0, 1.0), và sử
dụng **tf.random.uniform** với **dtype = tf.dtypes.int32** để tạo tensor
với các số nguyên ngẫu nhiên trong một khoảng cụ thể.''')
        
    ex_9 = '''\
#TensorFlow code
import tensorflow as tf


# Thiết lập seed để đảm bảo kết quả ngẫu nhiên có thể tái tạo được
tf.random.set_seed(2024)

# Tạo tensor với các giá trị ngẫu nhiên trong khoảng [0, 1)
tensor_rand = tf.random.uniform((3, 4))
print("Tensor ngẫu nhiên trong khoảng [0, 1):\\n", tensor_rand)

# Tạo tensor với các giá trị ngẫu nhiên trong khoảng [-10, 10)
tensor_randint = tf.random.uniform((3, 4), minval=-10, maxval=10, dtype=tf.dtypes.int32)
print("Tensor ngẫu nhiên trong khoảng [-10, 10):\\n", tensor_randint)'''

    generate_code_file(ex_9, 'ex_9', data_dir)