import streamlit as st
import os
from aio_code_editor import ui, st_connect_data
import textwrap

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
    data_dir = "data/"+username+"/string/"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    st.button("Đăng xuất", on_click=st.session_state.clear)
    
    st.markdown("# LIST IN PYTHON - AIO 2024")
    
    
    st.markdown(r"""## 1. List là gì""" )
    st.markdown("""List là một trong 4 kiểu dữ liệu tập hợp(colections) trong Python, chứa không hay nhiều phần tử có thể có giá trị giống nhau có thứ tự và có thể thay đổi được.
List được tạo bởi cặp dấu ngoặc vuông [] bao quanh các phần tử, mỗi phần tử trong list được phân cách nhau bởi dấu phẩy ",".""")
    ex_1 = textwrap.dedent('''\
    #ai vietnam
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    ''')
    key = "ex_1"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_1, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""List không chứa phần tử nào là một list rỗng.""")
    ex_2 = textwrap.dedent('''\
    #ai vietnam
    empty_list = []
    print(empty_list)
    ''')
    key = "ex_2"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_2, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Các phần tử trong list có thể có giá trị giống nhau.""")
    ex_3 = textwrap.dedent('''\
    #ai vietnam
    duplicate_elements_list = [1, 2, 2, 3, 3, 3]
    print(duplicate_elements_list)
    ''')
    key = "ex_3"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_3, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Các phần tử trong list có thứ tự vì nó được lưu trữ theo thứ tự và có thể truy cập qua chỉ mục.""")
    ex_4 = textwrap.dedent('''\
    #ai vietnam
    ordered_list = ['a', 'b', 'c', 'd']
    print(ordered_list[0])
    print(ordered_list[2])
    ''')
    key = "ex_4"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_4, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Ta có thể thay đổi giá trị của các phần tử trong list sau khi đã tạo nó, tính chất này sẽ được giải thích rõ hơn ở phần 3. Sửa đổi phần tử trong list. 
                Ngoài ra list có thể chứa các phần tử thuộc các kiểu dữ liệu khác nhau.""")
    ex_5 = textwrap.dedent('''\
    #ai vietnam
    my_list = [1, "hello", 3.14, True, [1, 2, 3]]
    print(my_list)
    ''')
    key = "ex_5"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_5, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Chúng ta có thể ước lượng độ dài của list để xem list chứa bao nhiêu phần tử qua hàm len().""")
    ex_6 = textwrap.dedent('''\
    #ai vietnam
    my_list = ["apple", "banana", "durian", "orange"]
    print(f"length list = {len(my_list)}")
    ''')
    key = "ex_6"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_6, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Để kiểm tra một biến có kiểu dữ liệu là list hay không, chúng ta sử dụng hàm type().""")
    ex_7 = textwrap.dedent('''\
    #ai vietnam
    my_list = ["Hoa", "Đào", "Cúc"]
    print(type(my_list))
    ''')
    key = "ex_7"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_7, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""## 2. Truy cập phần tử 
                
Truy cập các phần tử trong list là một thao tác cơ bản và quan trọng. Bạn có thể truy cập các phần tử này thông qua chỉ mục (index) hoặc sử dụng kỹ thuật slicing để lấy một phần của list.""")
    
    st.markdown("""### 2.1. Truy cập phần tử qua chỉ mục
Mỗi phần tử trong list được xác định bởi một chỉ mục, bắt đầu từ 0 cho phần tử đầu tiên và tăng dần. Chúng ta cũng có thể dùng chỉ mục âm để truy cập phần tử từ cuối danh sách, ví dụ phần tử cuối cùng của list có index là -1.
Chúng ta thường sử dụng chỉ mục để truy cập và thay đổi các phần tử trong list.""")
    
    ex_21= textwrap.dedent('''\
    #ai vietnam
    # Indexing example
    my_list = [10, 20, 30, 40, 50]

    print("First element:", my_list[0])
    print("Third element:", my_list[2])
    print("Last element:", my_list[-1])
    print("Second to last element:", my_list[-2])

    ''')
    key = "ex_21"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_21, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 2.2. Truy cập phần tử qua slicing
Slicing cho phép bạn truy cập một phần của danh sách bằng cách sử dụng cú pháp [start:stop:step]. Trong đó, start là chỉ số bắt đầu, stop là chỉ số dừng và step là bước nhảy giữa các phần tử. Mặc định start là 0, stop là độ dài của danh sách và step là 1.""")
    ex_22 = textwrap.dedent('''\
    #ai vietnam
    # Slicing example
    my_list = [10, 20, 30, 40, 50]

    print("Elements from second to fourth:", my_list[1:4])
    print("Elements from start to third:", my_list[:3])
    print("Elements from third to end:", my_list[2:])
    print("Elements with step of 2:", my_list[::2])
    print("Elements in reverse order:", my_list[::-1])
    ''')
    key = "ex_22"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_22, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Dưới đây là bảng tổng hợp về cách truy cập phần tử trong danh sách (list) bằng cách sử dụng chỉ mục và slicing trong Python:

| Phương pháp     | Cú pháp            | Mô tả                                  | Ví dụ `my_list = [10, 20, 30, 40, 50]`                                                     |
|-----------------|--------------------|----------------------------------------|------------------------------------------------------------|
| Chỉ mục (Indexing) | `list[index]`      | Truy cập phần tử tại vị trí `index`        | `my_list[0]` => Truy cập phần tử đầu tiên: 10            |
|                 |                    |                                        | `my_list[2]` => Truy cập phần tử thứ ba: 30               |
|                 |                    |                                        | `my_list[-1]` => Truy cập phần tử cuối cùng: 50           |
|                 |                    |                                        | `my_list[-2]` => Truy cập phần tử thứ hai từ cuối: 40     |
| Slicing         | `list[start:stop]` | Truy cập các phần tử từ `start` đến `stop-1` | `my_list[1:4]` => Các phần tử từ thứ hai đến thứ tư: [20, 30, 40] |
|                 | `list[:stop]`      | Truy cập các phần tử từ đầu đến `stop-1`   | `my_list[:3]` => Các phần tử từ đầu đến thứ ba: [10, 20, 30] |
|                 | `list[start:]`     | Truy cập các phần tử từ `start` đến hết danh sách | `my_list[2:]` => Các phần tử từ thứ ba đến hết: [30, 40, 50] |
|                 | `list[start:stop:step]` | Truy cập các phần tử từ `start` đến `stop-1` với bước nhảy `step` | `my_list[::2]` => Các phần tử với bước nhảy 2: [10, 30, 50] |
|                 | `list[::-1]`       | Truy cập các phần tử theo thứ tự ngược lại | `my_list[::-1]` => Các phần tử theo thứ tự ngược: [50, 40, 30, 20, 10] |""")
    
    
    st.markdown("""## 3. Sửa đổi giá trị phần tử

Theo định nghĩa, các phần tử trong list có thể thay đổi được, tức là có thể thêm, sửa, xóa. Trong phần này sẽ trình bày hai cách cơ bản để sửa đổi giá trị phần tử trong list là:

- Indexing: dùng để thay đổi một phần tử cụ thể.
- Slicing: dùng để thay đổi một hoặc nhiều phần tử liên tiếp.""")
    
    st.markdown("""### 3.1. Sửa đổi giá trị phần tử theo indexing
Ta có thể thay đổi giá trị của một phần tử cụ thể trong danh sách bằng cách sử dụng chỉ mục của nó.""")
    ex_31 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    my_list[1] = 25  # Thay đổi phần tử thứ hai thành 25
    print("Modified list by index:", my_list)  # Kết quả: [10, 25, 30, 40, 50]
    ''')
    key = "ex_31"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_31, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 3.2. Sửa đổi giá trị phần tử theo slicing

Slicing cho phép bạn thay đổi nhiều phần tử trong danh sách cùng một lúc bằng cách gán một danh sách mới cho một đoạn (slice) của danh sách hiện tại.""")
    ex_32 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    my_list[1:3] = [25, 35]  # Thay đổi các phần tử thứ hai và thứ ba
    print("Modified list by slicing:", my_list)

    # Thay đổi nhiều phần tử hơn số lượng phần tử trong slicing
    my_list[2:4] = [33, 37, 39]  # Thay đổi các phần tử thứ ba và thứ tư, thêm một phần tử mới
    print("Modified list by extended slicing:", my_list)
    ''')
    key = "ex_32"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_32, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Dưới đây là bảng tổng hợp về cách sửa đổi phần tử trong danh sách bằng chỉ mục và slicing trong Python:

| Phương pháp         | Cú pháp                  | Mô tả                                                 | Ví dụ                                                      |
|---------------------|--------------------------|-------------------------------------------------------|------------------------------------------------------------|
| Sửa đổi theo chỉ mục (Indexing) | `list[index] = value`      | Thay đổi giá trị của phần tử tại vị trí `index`         | `my_list[1] = 25` => `my_list` trở thành `[10, 25, 30, 40, 50]` |
| Sửa đổi theo slicing | `list[start:stop] = new_list` | Thay đổi các phần tử từ `start` đến `stop-1` với `new_list` | `my_list[1:3] = [25, 35]` => `my_list` trở thành `[10, 25, 35, 40, 50]` |
|                     |                          |                                                       | `my_list[2:4] = [33, 37, 39]` => `my_list` trở thành `[10, 25, 33, 37, 39, 50]` |""")
    
    st.markdown("""## 4. Thêm phần tử vào list

Trong phần này, chúng ta tìm hiểu về ba cách để thêm phần tử mới vào danh sách:

- Sử dụng phương thức append() thêm một phần tử vào cuối danh sách.

- Sử dụng phương thức insert() thêm một phần tử vào vị trí chỉ định trong danh sách.

- Sử dụng phương thức extend() thêm tất cả các phần tử của một iterable (như danh sách khác) vào cuối danh sách hiện tại.""")
    
    ex_41 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30]

    # Sử dụng append() để thêm phần tử vào cuối danh sách
    my_list.append(40)
    print("List after append:", my_list)

    # Sử dụng insert() để thêm phần tử vào vị trí chỉ định
    my_list.insert(1, 15)  # Chèn phần tử 15 vào vị trí thứ hai
    print("List after insert:", my_list)

    # Sử dụng extend() để thêm nhiều phần tử vào cuối danh sách
    my_list.extend([50, 60])
    print("List after extend:", my_list)

    # Phép cộng
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_list = list1 + list2
    print("concatenated_list:",concatenated_list)

    # Phép nhân
    original_list = [1, 2, 3]
    multiplied_list = original_list * 3
    print("multiplied_list:",multiplied_list)
    ''')
    key = "ex_41"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_41, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Dưới đây là bảng tổng hợp các phương pháp để thêm phần tử vào danh sách:

| Phương pháp       | Cú pháp                      | Mô tả                                               | Ví dụ    `my_list = [10, 20, 30]`                                                |
|-------------------|------------------------------|-----------------------------------------------------|-------------------------------------------------------------|
| `append()`        | `list.append(element)`       | Thêm một phần tử vào cuối danh sách                 | `my_list.append(40)` => `[10, 20, 30, 40]`                  |
| `insert()`        | `list.insert(index, element)`| Thêm một phần tử vào vị trí chỉ định trong danh sách| `my_list.insert(1, 15)` => `[10, 15, 20, 30]`               |
| `extend()`        | `list.extend(iterable)`      | Thêm tất cả các phần tử của một iterable vào cuối danh sách| `my_list.extend([40, 50])` => `[10, 20, 30, 40, 50]` |
| Phép cộng (`+`)  | `list1 + list2`              | Nối hai danh sách lại với nhau                      | `my_list + [40, 50]` => `[10, 20, 30, 40, 50]`              |
| Phép nhân (`*`)  | `list * n`                   | Tạo một danh sách mới bằng cách lặp lại danh sách ban đầu n lần| `my_list * 2` => `[10, 20, 30, 10, 20, 30]`           |""")
    
    st.markdown("""## 5. Xóa phần tử

Để xóa phần tử trong list, chúng ta có thể xóa theo các cách sau:

- Xóa phần tử theo giá trị
- Xóa phần tử theo vị trí
- Xóa toàn bộ tất cả phần tử trong list""")
    
    st.markdown("""### 5.1. Xóa phần tử theo giá trị

Chúng ta có thể sử dụng phương thức remove() để xóa phần tử đầu tiên có giá trị được chỉ định ra khỏi danh sách.""")
    ex_51 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50, 30, 40]
    my_list.remove(30)  # Xóa phần tử có giá trị 30
    print("List after remove:", my_list)
    ''')
    key = "ex_51"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_51, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown("""### 5.2. Xóa phần tử theo vị trí
Phương thức pop() và từ khóa del xóa phần tử tại vị trí chỉ định trong danh sách.""")
    
    st.markdown("""### 5.1. Xóa phần tử theo giá trị

Chúng ta có thể sử dụng phương thức remove() để xóa phần tử đầu tiên có giá trị được chỉ định ra khỏi danh sách.""")
    ex_52 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    removed_element = my_list.pop(2)  # Xóa phần tử tại vị trí thứ ba
    print("Removed element:", removed_element)
    print("List after pop:", my_list)
    ''')
    key = "ex_52"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_52, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Chúng ta cũng có thể sử dụng từ khóa del để xóa phần tử tại vị trí chỉ định trong list""")
    ex_53 = textwrap.dedent('''\
    #ai vietnam
    # Xóa theo indexing
    my_list = [10, 20, 30, 40, 50]
    del my_list[1]  # Xóa phần tử tại vị trí thứ hai
    print("List after del by index:", my_list)

    # Xóa theo slicing
    my_list = [100, 200, 300, 400, 500] 
    del my_list[1:3] 
    print("List after del by slice:", my_list)
    ''')
    key = "ex_53"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_53, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown("""### 5.3. Xóa toàn bộ danh sách

Có hai cách để xóa toàn bộ danh sách là:
- Sử dụng từ khóa del
- Sử dụng phương thức clear()

Khi sử dụng từ khóa del thì toàn bộ list khỏi bộ nhớ máy tính, khi đó list không thể truy cập được nữa.""")
    
    ex_54 = textwrap.dedent('''\
    #ai vietnam
    # Xóa toàn bộ danh sách
    my_list = [10, 20, 30, 40, 50]
    del my_list
    # print(my_list)
    ''')
    key = "ex_54"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_54, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Khi sử dụng phương thức clear() nó sẽ xóa toàn bộ phần tử trong list, khi đó list sẽ rỗng nhwung vẫn truy cập được.""")
    ex_55 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    my_list.clear()  # Xóa tất cả các phần tử trong danh sách
    print("List after clear:", my_list)  # Kết quả: []
    ''')
    key = "ex_55"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_55, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown("""Dưới đây là bảng tổng hợp các phương pháp xóa phần tử trong danh sách với các ví dụ sử dụng các danh sách khác nhau:

| Nhóm                | Cú pháp                 | Mô tả                                               | Ví dụ                                     |
|---------------------|-------------------------|-----------------------------------------------------|-------------------------------------------|
| Xóa theo giá trị    | `list.remove(value)`    | Xóa phần tử đầu tiên có giá trị `value` trong danh sách | ```my_list = [1, 2, 3, 4, 5] my_list.remove(3) print(my_list)  # Kết quả: [1, 2, 4, 5]``` |
| Xóa theo vị trí     | `list.pop(index)`       | Xóa và trả về phần tử tại vị trí `index` (hoặc phần tử cuối nếu không có `index`) | ```my_list = ['a', 'b', 'c', 'd'] removed_element = my_list.pop(2) print(my_list)  # Kết quả: ['a', 'b', 'd'] print(removed_element)  # Kết quả: 'c'``` |
|                     | `del list[index]`       | Xóa phần tử tại vị trí chỉ định trong danh sách     | ```my_list = [10, 20, 30, 40, 50] del my_list[1] print(my_list)  # Kết quả: [10, 30, 40, 50]``` |
|                     | `del list[start:end]`   | Xóa các phần tử từ vị trí `start` đến `end-1`       | ```my_list = [100, 200, 300, 400, 500] del my_list[1:3] print(my_list)  # Kết quả: [100, 400, 500]``` |
| Xóa tất cả phần tử  | `list.clear()`          | Xóa tất cả các phần tử trong danh sách              | ```my_list = ['apple', 'banana', 'cherry'] my_list.clear() print(my_list)  # Kết quả: []``` |
| Xóa toàn bộ danh sách | `del list`              | Xóa toàn bộ danh sách                               | ```my_list = [1, 2, 3, 4, 5] del my_list # print(my_list)  # Sẽ gây lỗi vì my_list đã bị xóa``` |""")
    
    st.markdown("""## 6. Tìm kiếm phần tử

Trong Python, chúng ta có thể tìm kiếm phần tử trong danh sách bằng cách sử dụng phương thức index() hoặc sử dụng từ khóa in. Ngoài ra chúng ta có thể sử dụng vòng lặp, phương thức count() hoặc hàm any().""")
    
    st.markdown("""### 6.1. Sử dụng phương thức `index()`

Phương thức này trả về vị trí đầu tiên của phần tử có giá trị cụ thể trong danh sách. Nếu phần tử không tồn tại, sẽ gây ra lỗi ValueError.""")
    
    ex_61 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    value_to_find = 30
    try:
        index = my_list.index(value_to_find)
        print("Index of", value_to_find, ":", index)
    except ValueError:
        print(value_to_find, "not found in the list")
    ''')
    key = "ex_61"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_61, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 6.2. Sử dụng từ khóa `in`

Bạn có thể sử dụng từ khóa in để kiểm tra xem một phần tử cụ thể có tồn tại trong danh sách hay không. Kết quả trả về là True nếu phần tử tồn tại và False nếu không tồn tại.""")
    
    ex_62 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    value_to_find = 30
    if value_to_find in my_list:
        print(value_to_find, "found in the list")
    else:
        print(value_to_find, "not found in the list")
    ''')
    key = "ex_62"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_62, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 6.3. Sử dụng vòng lặp `for`
Duyệt qua danh sách và so sánh từng phần tử với giá trị tìm kiếm. Nếu phần tử được tìm thấy, bạn có thể lấy vị trí của nó.""")
    
    ex_63 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    value_to_find = 30
    for index, value in enumerate(my_list):
        if value == value_to_find:
            print("Index of", value_to_find, ":", index)
            break
    else:
        print(value_to_find, "not found in the list")
    ''')
    key = "ex_63"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_63, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 6.4. Sử dụng phương thức `count()`

Phương thức này trả về số lần xuất hiện của một phần tử trong danh sách.""")
    
    ex_64 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 30, 50]
    value_to_find = 30
    count = my_list.count(value_to_find)
    print("Count of", value_to_find, ":", count)
    ''')
    key = "ex_64"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_64, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 6.5. Sử dụng hàm any()
Hàm này trả về True nếu có ít nhất một phần tử trong danh sách thỏa mãn một điều kiện nào đó, ngược lại trả về False.""")
    
    ex_65 = textwrap.dedent('''\
    #ai vietnam
    my_list = [10, 20, 30, 40, 50]
    condition = any(item > 30 for item in my_list)
    print("Any item greater than 30:", condition)
    ''')
    key = "ex_65"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_65, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Dưới đây là bảng tổng hợp các phương pháp tìm kiếm phần tử trong danh sách trong Python:

| Phương pháp               | Cú pháp                     | Mô tả                                                         |
|---------------------------|-----------------------------|---------------------------------------------------------------|
| `index(value)`            | `list_name.index(value)`    | Trả về vị trí của phần tử đầu tiên có giá trị `value` trong danh sách. Nếu không tìm thấy, gây ra lỗi `ValueError`. |
| `in`                      | `value in list_name`        | Kiểm tra xem một phần tử cụ thể có tồn tại trong danh sách hay không. Trả về `True` nếu tồn tại và `False` nếu không tồn tại. |
| Vòng lặp(`for`, `while`)  |                             | Duyệt qua danh sách và so sánh từng phần tử với giá trị tìm kiếm. Nếu phần tử được tìm thấy, bạn có thể lấy vị trí của nó. |
| `count(value)`            | `list_name.count(value)`    | Trả về số lần xuất hiện của một phần tử có giá trị cụ thể trong danh sách. |
| `any(condition)`         | `any(item for item in list_name if condition)` | Trả về `True` nếu có ít nhất một phần tử trong danh sách thỏa mãn điều kiện `condition`, ngược lại trả về `False`. |""")
    
    st.markdown("""## 7. Sắp xếp các phần tử trong list

Sắp xếp danh sách là quá trình sắp xếp các phần tử trong danh sách theo một thứ tự nhất định. Trong Python, có nhiều cách để thực hiện việc sắp xếp danh sách, bao gồm sử dụng vòng lặp, phương thức sort(), hàm sorted(), và phương thức reverse().""")
    
    st.markdown("""### 7.1 Sắp xếp phần tử sử dụng vòng lặp

Chúng ta hoàn toàn có thể sử dụng vòng lặp để duyệt phần tử trong list và sắp xếp chúng.""")
    ex_71 = textwrap.dedent('''\
    #ai vietnam
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    sorted_list = []
    while my_list:
        min_value = min(my_list)
        sorted_list.append(min_value)
        my_list.remove(min_value)
    print("Sorted list using loop:", sorted_list)
    ''')
    key = "ex_71"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_71, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown("""### 7.2. Sắp xếp phần tử sử dụng phương thức `sort()`

Chúng ta có thể sử dụng phương thức sort() để sắp xếp danh sách trong chính nó.""")
    ex_72 = textwrap.dedent('''\
    #ai vietnam
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    my_list.sort()
    print("Sorted list using sort():", my_list)
    ''')
    key = "ex_72"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_72, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""### 7.3. Sắp xếp phần tử sử dụng hàm `sorted()`
                
Ta có thể sử dụng hàm sorted() để tạo `một danh sách mới` chứa các phần tử đã sắp xếp từ danh sách ban đầu. Đây là sự khác biệt so với phương thức sort() sắp xếp trực tiếp trên list, còn sorted() trả về list mới. Khi sử dụng thì tùy trường hợp mà các bạn chọn để tối ưu chương trình.""")
    ex_73 = textwrap.dedent('''\
    #ai vietnam
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    sorted_list = sorted(my_list)
    print("Sorted list using sorted():", sorted_list)
    ''')
    key = "ex_73"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_73, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown("""### 7.4. Đảo ngược thứ tự các phần tử trong danh sách

Đôi khi việc sắp xếp đơn giản là chỉ muốn đảo ngược lại vị trí các phần tử, chúng ta có thể sử dụng phương thức reverse() để đảo ngược thứ tự các phần tử trong danh sách.""")
    
    ex_74 = textwrap.dedent('''\
    #ai vietnam
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    my_list.reverse()
    print("Reversed list:", my_list)
    ''')
    key = "ex_74"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_74, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.markdown("""Dưới đây là bảng tổng hợp các phương pháp sắp xếp phần tử trong danh sách:

| Phương pháp               | Cú pháp                    | Mô tả                                                         |
|---------------------------|----------------------------|---------------------------------------------------------------|
| `sort()`                  | `list_name.sort()`         | Sắp xếp danh sách trong chính nó theo một thứ tự nhất định.   |
| `sorted()`                | `sorted_list = sorted(list_name)` | Tạo một danh sách mới chứa các phần tử đã sắp xếp từ danh sách ban đầu. |
| `reverse()`               | `list_name.reverse()`      | Đảo ngược thứ tự các phần tử trong danh sách.                 |
| Sử dụng vòng lặp          |                            | Duyệt qua danh sách và thực hiện sắp xếp các phần tử.        |

Hầu hết các phương pháp trên đều là các hàm hoặc phương thức đã có sẵn, các bạn chỉ cần học cách sử dụng chúng. Các bạn có thể luyện tập thêm bằng cách tự tìm hiểu và lập trình những thuật toán cơ bản về sắp xếp... cũng khá thú vị đó.""")
    
    st.markdown("""## 8. List comprehension

List comprehension là một cú pháp trong Python cho phép bạn tạo một danh sách mới một cách nhanh chóng và dễ đọc từ một danh sách có sẵn. Cú pháp của list comprehension rất ngắn gọn và mạnh mẽ.

Cú pháp chung của list comprehension là:

```
new_list = [expression for item in iterable if condition]
```

Trong đó:
- `expression` là biểu thức được tính toán cho mỗi phần tử trong `iterable`.
- `item` là phần tử hiện tại trong `iterable`.
- `iterable` là một đối tượng có thể lặp lại như danh sách, bộ hoặc chuỗi.
- `condition` là một biểu thức điều kiện để lọc các phần tử (tùy chọn).""")
    
    ex_81 = textwrap.dedent('''\
    #ai vietnam
    # Tạo một danh sách chứa bình phương của các số từ 0 đến 9
    squares = [x**2 for x in range(10)]
    print("squares: ",squares)

    # Lọc các số chẵn từ 0 đến 9
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print("even_numbers: ", even_numbers)

    # Kết hợp hai danh sách thành một danh sách kết quả
    pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print("pairs: ", pairs)
    ''')
    key = "ex_81"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_81, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.write("""## 9. Các lỗi thường gặp khi sử dụng list""")
    st.write("""### 9.1. Lỗi cú pháp (`SyntaxError`)""")
    ex_91 = textwrap.dedent('''\
    #ai vietnam
    # Sai cú pháp khi khai báo danh sách
    my_list = [1, 2, 3

    # Sử dụng sai cú pháp trong các phương thức của danh sách
    my_list.append(4)
    my_list.insert(1, 5
    ''')
    key = "ex_91"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_91, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.write("""### 9.2. Lỗi chỉ mục (`Index Error`)""")
    
    ex_92 = textwrap.dedent('''\
    #ai vietnam
    my_list = [1, 2, 3]
    print(my_list[3])
    ''')
    key = "ex_92"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_92, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.write("""### 9.3. Lỗi kiểu dữ liệu (`Type Error`)""")

    ex_93 = textwrap.dedent('''\
    #ai vietnam
    my_list = [1, 2, 3]
    print(my_list + 4)
    ''')
    key = "ex_93"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_93, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    
    
    
    
    st.success('Chúc mừng bạn đã hoàn thành bài học nha!', icon="✅")
    
    # # Ý kiến góp ý, báo lỗi
    # with st.expander("Đóng góp ý kiến của bạn/Báo lỗi"):
    #     st.write("Nếu bạn có bất kỳ ý kiến đóng góp hoặc phát hiện lỗi, vui lòng để lại ý kiến của bạn ở đây để chúng tôi cải thiện chất lượng hơn. Xin cảm ơn!")
    #     feedback = st.text_area("Nhập ý kiến của bạn hoặc báo lỗi", key="feedback", height=20)
    #     st.button("Gửi"):
            
    