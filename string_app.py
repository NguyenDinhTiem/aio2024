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
    
    st.markdown("# STRING IN PYTHON - AIO 2024")
    
    
    st.markdown(r"""## 1. Giới thiệu về String""" )
    st.markdown("""String là một kiểu dữ liệu trong Python được bao quanh bởi dấu ngoặc kép hoặc cặp dấu nháy đơn, cặp 3 dấu nháy.""")
    ex_1 = textwrap.dedent('''\
    #ai vietnam
    print("AI VIETNAM")
    print('AI VIETNAM')
    print("""
    This is a comment
    written in
    more than just one line
    """)
    ''')
    key = "ex_1"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_1, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.write(st.session_state)
    
    st.markdown(r"""## 2. Khởi tạo String""" )
    
    st.markdown(r"""### 2.1 Gán giá trị string cho một biến""")
    st.markdown("""Khi chúng ta tạo một string mà không dùng lệnh print để hiển thị nó hay gán nó vào bất kỳ biến nào thì khi chạy chương trình Python sẽ bỏ qua nó và coi nó như là comment.
                Để tạo một biến string, ta gán string cho biến đó bởi dấu bằng.""")
    
    ex_21 = textwrap.dedent('''\
    #ai vietnam
    name = "Tom"
    print(name)
    ''')
    key = "ex_21"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_21, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown(r"""### 2.2 Index trong string""")
    st.markdown("""String là một tập hợp các ký tự được đánh số thứ tự (index) bắt đầu từ 0. 
                Ta có thể truy cập và thao tác với từng ký tự trong chuỗi bằng cách sử dụng chỉ số của nó.
                Chỉ số âm cũng có thể được sử dụng, với -1 là chỉ số của ký tự cuối cùng.""")
    ex_22 = textwrap.dedent('''\
    #ai vietnam
    name = "AI VIETNAM"
    print(name[0])
    print(name[5])
    print(name[-1])
    ''')
    key = "ex_22"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_22, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown("""Chúng ta cũng có thể duyệt từng phần tử trong string với vòng lặp for.""")
    ex_23 = textwrap.dedent('''\
    #ai vietnam
    fruit = 'banana'
    for i in fruit:
        print(i)
    ''')
    key = "ex_23"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_23, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown(r"""### 2.3 Slicing""")
    st.markdown(r"""Slicing string trong Python là một phương pháp mạnh mẽ và linh hoạt để trích xuất các phần cụ thể của chuỗi. 
                Bằng cách sử dụng cú pháp s[start:end:step], bạn có thể chọn ra một đoạn con từ chuỗi gốc, nơi start là chỉ số bắt đầu,
                end là chỉ số kết thúc (không bao gồm), và step là khoảng cách giữa các chỉ số. Slicing cho phép:
                
* Lấy một đoạn chuỗi con từ vị trí start đến end (không bao gồm).

* Bỏ qua một số lượng ký tự xác định bằng cách sử dụng step.

* Đảo ngược chuỗi bằng cách sử dụng step âm.

* Trích xuất các phần tử từ cuối chuỗi bằng chỉ số âm.""")
    
    ex_24 = textwrap.dedent('''\
    #ai vietnam
    b = "Hello, World!"
    print("b[2:5]=", b[2:5])
    print("b[:5]=", b[:5])
    print("b[2:]=",b[2:])
    print("b[-5:-2]=",b[-5:-2])                                                    
    ''')
    key = "ex_24"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_24, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown(r"""Qua các ví dụ trên chúng ta có thể thấy slicing rất hữu ích trong quá trình xử lý string và ta tóm gọn lại như sau:

* Sclicing giúp truy xuất dễ dàng các phần của chuỗi mà không cần lặp qua từng ký tự.
* Tăng cường khả năng xử lý chuỗi và thao tác dữ liệu văn bản trong lập trình Python.
* Giúp viết mã ngắn gọn, trực quan và dễ hiểu hơn.

Dưới đây là bảng tổng hợp lại các cách sử dụng slicing:

| Biểu thức         | Mô tả                                                        | Ví dụ                                                                 |
|-------------------|--------------------------------------------------------------|-----------------------------------------------------------------------|
| `s[start:end]`    | Trả về chuỗi con từ vị trí `start` đến `end` (không bao gồm) | ```python s = "Hello World"; s[0:5] # "Hello" ```                     |
| `s[start:]`       | Trả về chuỗi con từ vị trí `start` đến hết chuỗi             | ```python s = "Hello World"; s[6:] # "World" ```                      |
| `s[:end]`         | Trả về chuỗi con từ đầu chuỗi đến vị trí `end` (không bao gồm)| ```python s = "Hello World"; s[:5] # "Hello" ```                      |
| `s[start:end:step]` | Trả về chuỗi con từ vị trí `start` đến `end` (không bao gồm), lấy mỗi `step` ký tự | ```python s = "Hello World"; s[0:5:2] # "Hlo" ```                      |
| `s[::-1]`         | Đảo ngược chuỗi                                             | ```python s = "Hello World"; s[::-1] # "dlroW olleH" ```              |
| `s[start:end:-1]` | Trả về chuỗi con từ vị trí `start` đến `end` (không bao gồm), theo thứ tự ngược lại | ```python s = "Hello World"; s[5:0:-1] # "olleH" ```                 |
| `s[-start:-end]`  | Trả về chuỗi con với các vị trí bắt đầu và kết thúc từ cuối chuỗi | ```python s = "Hello World"; s[-5:-1] # "Worl" ```                    |
| `s[:end:-1]`      | Trả về chuỗi con từ cuối chuỗi đến vị trí `end` theo thứ tự ngược lại | ```python s = "Hello World"; s[:5:-1] # "dlroW " ```               |
| `s[start::step]`  | Trả về chuỗi con từ vị trí `start` đến hết chuỗi, lấy mỗi `step` ký tự | ```python s = "Hello World"; s[1::2] # "el ol" ```                     |
| `s[::step]`       | Trả về chuỗi con từ đầu đến cuối chuỗi, lấy mỗi `step` ký tự | ```python s = "Hello World"; s[::2] # "HloWrd" ```                    |
| `s[-start:]`      | Trả về chuỗi con từ vị trí `-start` (từ cuối) đến hết chuỗi  | ```python s = "Hello World"; s[-5:] # "World" ```                     |
| `s[:-end]`        | Trả về chuỗi con từ đầu chuỗi đến vị trí `-end` (từ cuối)    | ```python s = "Hello World"; s[:-5] # "Hello " ```                    |""")
    
    st.markdown(r"""## 3. Phép + và * string""" )
    st.markdown("""Phép cộng (+) và phép nhân (*) được sử dụng để thực hiện các phép toán trên string.
                Phép cộng nối các string lại với nhau, trong khi phép nhân lặp lại string một số lần.""")
    ex_31 = textwrap.dedent('''\
    #ai vietnam
    # Phép cộng chuỗi
    string_1 = "Hello"
    string_2 = "World"
    result_1 = string_1 + " " + string_2
    print("string_1 + string_2 = ", result_1) 

    # Phép nhân chuỗi
    string_3 = "Hello"
    result_2 = string_3 * 3
    print("string_3 * 3 = ", result_2)                                     
    ''')
    key = "ex_31"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_31, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown("""Tuy nhiên, không thể thực hiện các phép tính này trên các chuỗi chứa các ký tự không phải số.""")
    ex_32 = textwrap.dedent('''\
    #ai vietnam
    number_string = "123"
    result_3 = number_string + 456                                 
    ''')
    key = "ex_32"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_32, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)

    st.markdown(r"""## 4. Fstring""" )
    st.markdown("""F-string (formatted string literals) là một cách tiện lợi và dễ đọc để định dạng chuỗi trong Python,
                được giới thiệu từ Python 3.6. Bằng cách đặt chữ 'f' hoặc 'F' trước dấu ngoặc kép mở của chuỗi, 
                ta có thể nhúng biểu thức Python trực tiếp bên trong chuỗi sử dụng cặp dấu ngoặc nhọn {}. 
                F-string cung cấp cách định dạng chuỗi hiệu quả và dễ hiểu, hỗ trợ cả biểu thức và hàm.""")
    
    ex_4 = textwrap.dedent('''\
    #ai vietnam
    age = 36
    txt_1 = f"My name is Tom, I am {age}"
    print(txt_1)

    price = 59.7899999
    txt_2 = f"The price is {price:.2f} dollars"
    print(txt_2)                               
    ''')
    key = "ex_4"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_4, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""## 5. Escape characters - Các ký tự đặc biệt""" )
    st.markdown(r"""Trong Python, các ký tự escape được sử dụng để biểu diễn các ký tự đặc biệt trong chuỗi mà không thể được 
                biểu diễn trực tiếp. Theo chức năng, ta phân thành 3 loại escape sau:
                
* Escape cho ký tự đặc biệt

* Escape cho ký tự điều khiển

* Escape cho ký tự unicode

* Escape cho ký tự Escape""")
    
    st.markdown(r"""### 5.1. Escape cho ký tự đặc biệt

- \': Dùng để chèn dấu nháy đơn (') trong chuỗi.
- \": Dùng để chèn dấu nháy kép (") trong chuỗi.
- \ \\: Dùng để chèn dấu chéo ngược (\\) trong chuỗi.""")
    
    ex_51 = textwrap.dedent('''\
    #ai vietnam
    # Dấu nháy đơn (single quote)
    print('Escape cho dấu nháy đơn: It\'s a test.')

    # Dấu nháy kép (double quote)
    print("Escape cho dấu nháy kép: He said, \"Hello\"")

    # Ký tự gạch chéo ngược (backslash)
    print("Escape cho dấu gạch chéo ngược: C:\\path\\to\\file")               
    ''')
    key = "ex_51"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_51, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 5.2. Escape cho ký tự điều khiển

- \n: Tạo một dòng mới trong string
- \t: Tạo một khoảng trắng bằng tab(thông thường 1 tab bằng 4 khoảng trắng) trong chuỗi""")
    
    ex_52 = textwrap.dedent('''\
    #ai vietnam
    # Dòng mới (newline)
    print("Escape cho dòng mới: First line.\nSecond line.")

    # Tab ngang (horizontal tab)
    print("Escape cho tab ngang: Hello\tWorld")               
    ''')
    key = "ex_52"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_52, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 5.3. Escape cho ký tự unicode

Ký tự Unicode là một tiêu chuẩn quốc tế để đại diện cho các ký tự và biểu tượng từ các ngôn ngữ và văn hóa khác nhau trên thế giới. Dưới đây là cách chúng ta biểu diễn chúng trong string.""")
    ex_53 = textwrap.dedent('''\
    #ai vietnam
    # Ký tự Unicode của chuỗi "Hello"
    print("\u0048\u0065\u006C\u006C\u006F")

    # Ký tự Unicode với tên được chỉ định
    print("Escape cho ký tự Unicode với tên được chỉ định: \N{cat}")
             
    ''')
    key = "ex_53"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_53, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 5.4. Escape cho giá trị octal và hex

- \ooo : ooo là ba chữ số bát phân, đại diện cho giá trị ASCII của ký tự
- \xhh : \x là tiền tố cho biết rằng các ký tự tiếp theo là mã thập lục phân, hh là hai chữ số thập lục phân, mỗi chữ số có thể là từ 0-9 hoặc A-F (hoặc a-f).""")
    ex_54 = textwrap.dedent('''\
    #ai vietnam
    # Ký tự với giá trị octal(8, bát phân)
    print("Escape cho ký tự với giá trị octal: \101\102\103")

    # Ký tự với giá trị hex(16, thập lục phân)
    print("Escape cho ký tự với giá trị hex: \x41\x42\x43")            
    ''')
    key = "ex_54"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_54, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""Dưới đây là bảng tổng hợp các ký tự escape trong Python, được phân loại theo nhóm chức năng và bao gồm ví dụ minh họa cho từng loại:

| Nhóm               | Ký tự Escape | Mô tả                            | Ví dụ                                                       |
|--------------------|--------------|----------------------------------|-------------------------------------------------------------|
| Ký tự đặc biệt     | `\'`         | Dấu nháy đơn (')                 | `print('It\'s a test.')`                                    |
|                    | `\"`         | Dấu nháy kép (")                 | `print("He said, \"Hello\"")`                               |
|                    | `\\`         | Dấu gạch chéo ngược (\\)          | `print("Escape cho dấu gạch chéo ngược: C:\\path\\to\\file")`|
| Ký tự điều khiển   | `\n`         | Dấu xuống dòng                   | `print("Dòng 1\nDòng 2")`                                   |
|                    | `\t`         | Tab ngang                        | `print("Hello\tWorld")`                                     |
| Ký tự Unicode      | `\uXXXX`     | Ký tự Unicode| `print("\u0048\u0065\u006C\u006C\u006F")  # Hello`          |
|                    | `\N{name}`   | Ký tự Unicode theo tên          | `print("\N{grinning face}")  # 😀`                          |
| Ký tự số bát phân  | `\ooo`       | Ký tự số bát phân (hệ 8)  | `print("\101\102\103")  # ABC`                              |
| Ký tự số thập lục phân | `\xhh`   | Ký tự số thập lục phân (hệ 16) | `print("\x41\x42\x43")  # ABC`                             |
""")
    st.markdown(r"""## 6. Các phương thức biến đổi String

Có nhiều phương thức có sẵn cho String giúp thực hiện nhiều thao tác xử lý nó đơn giản mà không phải bỏ nhiều công sức. Đối với cách sử dụng phương thức thì đều có cấu trúc chung là `string_của_bạn.tên_phương_thức()`

Dựa vào chức năng của các phương thức, chúng được chia thành 3 nhóm:



1.   Các phương thức liên quan đến kiểm tra và so sánh
2.   Các phương thức liên quan đến chuyển đổi và định dạng
3.   Các phương thức liên quan đến tìm kiếm và thay thế


""" )
    
    st.markdown(r"""### 6.1. Các phương thức liên quan đến kiểm tra và so sánh
- isalnum(): trả về True nếu tất cả các ký tự là chữ và số, nghĩa là chữ cái trong bảng chữ cái (a-z) và số (0-9)
- isalpha(): Kiểm tra xem chuỗi có chứa ít nhất một ký tự và tất cả các ký tự đều là chữ cái(a-z).
- isdigit(): Kiểm tra xem chuỗi có chứa ít nhất một ký tự và tất cả các ký tự đều là số.
- islower(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ thường không.
- isupper(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ hoa không.""")
    
    ex_61 = textwrap.dedent('''\
    #ai vietnam
    # Các phương thức liên quan đến kiểm tra và so sánh
    example_string = "Hello123"
    print(example_string.isalnum())
    print(example_string.isalpha())
    print(example_string.isdigit())
    print(example_string.islower())
    print(example_string.isupper())            
    ''')
    key = "ex_61"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_61, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 6.2. Các phương thức liên quan đến chuyển đổi và định dạng:
- capitalize(): Chuyển đổi ký tự đầu tiên của chuỗi thành chữ hoa.
- lower(): Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường.
- upper(): Chuyển đổi tất cả các ký tự trong chuỗi thành chữ hoa.
- swapcase(): Chuyển đổi chữ hoa thành chữ thường và ngược lại.
- title(): Chuyển đổi ký tự đầu tiên của mỗi từ trong chuỗi thành chữ hoa.""")
    
    ex_62 = textwrap.dedent('''\
    #ai vietnam
    # Các phương thức liên quan đến chuyển đổi và định dạng
    example_string = "hello world"
    print(example_string.capitalize())
    print(example_string.lower())
    print(example_string.upper())
    print(example_string.swapcase())
    print(example_string.title()) 
    ''')
    key = "ex_62"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_62, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 6.3. Các phương thức liên quan đến tìm kiếm và thay thế:
- count(): Đếm số lần xuất hiện của một chuỗi con trong chuỗi.
- find(): Tìm vị trí của một chuỗi con trong chuỗi. Trả về chỉ số đầu tiên nếu tìm thấy, -1 nếu không tìm thấy.
- replace(): Thay thế một chuỗi con trong chuỗi bằng một chuỗi con khác.""")
    
    ex_63 = textwrap.dedent('''\
    #ai vietnam
    # Các phương thức liên quan đến tìm kiếm và thay thế
    example_string = "apple orange apple banana"
    print(example_string.count("apple"))
    print(example_string.find("orange"))
    print(example_string.replace("apple", "pear"))
    ''')
    key = "ex_63"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_63, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""Dưới đây là bảng tổng hợp các phương thức của string trong Python:

| Nhóm        | Phương thức | Mô tả chức năng                                  | Ví dụ                                                         |
|-------------|-------------|---------------------------------------------------|---------------------------------------------------------------|
| Kiểm tra và so sánh | isalnum()   | Kiểm tra xem chuỗi có chứa ký tự và số không    | `"Hello123".isalnum()` => `True`                              |
|             | isalpha()   | Kiểm tra xem chuỗi chỉ chứa ký tự không          | `"Hello".isalpha()` => `True`                                  |
|             | isdigit()   | Kiểm tra xem chuỗi chỉ chứa số không             | `"123".isdigit()` => `True`                                    |
|             | islower()   | Kiểm tra xem tất cả các ký tự trong chuỗi là chữ thường không | `"hello".islower()` => `True`                       |
|             | isupper()   | Kiểm tra xem tất cả các ký tự trong chuỗi là chữ hoa không    | `"HELLO".isupper()` => `True`                       |
| Chuyển đổi và định dạng | capitalize()| Chuyển đổi ký tự đầu tiên thành chữ hoa          | `"hello".capitalize()` => `"Hello"`                           |
|             | lower()     | Chuyển đổi tất cả các ký tự thành chữ thường    | `"Hello".lower()` => `"hello"`                                |
|             | upper()     | Chuyển đổi tất cả các ký tự thành chữ hoa       | `"hello".upper()` => `"HELLO"`                                |
|             | swapcase()  | Chuyển đổi chữ hoa thành chữ thường và ngược lại | `"Hello World".swapcase()` => `"hELLO wORLD"`                 |
|             | title()     | Chuyển đổi ký tự đầu tiên của mỗi từ thành chữ hoa | `"hello world".title()` => `"Hello World"`                   |
| Tìm kiếm và thay thế | count()     | Đếm số lần xuất hiện của một chuỗi con trong chuỗi | `"apple".count("p")` => `2`                                   |
|             | find()      | Tìm vị trí của một chuỗi con trong chuỗi         | `"banana".find("na")` => `2`                                  |
|             | replace()   | Thay thế một chuỗi con bằng một chuỗi khác      | `"apple".replace("p", "b")` => `"abble"`                       |
""")
    st.markdown(r"""## 7. Các hàm trong String
                
Trong Python, ngoài các phương thức (methods) có thể gọi trên đối tượng chuỗi, còn có một số hàm tích hợp (built-in functions) hữu ích cho việc làm việc với chuỗi.""" )
    
    st.markdown(r"""### 7.1. Nhóm kiểm tra string
Các hàm này kiểm tra các thuộc tính của chuỗi và trả về giá trị boolean.

- len(): Trả về độ dài của chuỗi.
- isinstance(): Kiểm tra nếu một đối tượng là một thể hiện của một lớp cụ thể.""")
    
    ex_71 = textwrap.dedent('''\
    #ai vietnam
    s = "Hello"
    print(f"len(s): {len(s)}")
    print(f"isinstance(s, str): {isinstance(s, str)}")
    ''')
    key = "ex_71"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_71, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 7.2. Nhóm chuyển đổi kiểu
Các hàm này chuyển đổi chuỗi sang kiểu dữ liệu khác.

- str(): Chuyển đổi một đối tượng thành chuỗi.
- int(): Chuyển đổi chuỗi thành số nguyên.
- float(): Chuyển đổi chuỗi thành số thực.""")
    
    ex_72 = textwrap.dedent('''\
    #ai vietnam
    num = 123
    s_num = str(num)
    print(f"str(num): {s_num}")

    s = "123"
    i_num = int(s)
    print(f"int(s): {i_num}")

    s_float = "123.45"
    f_num = float(s_float)
    print(f"float(s_float): {f_num}")
    ''')
    key = "ex_72"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_72, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 7.3. Nhóm định dạng cấu trúc
Định dạng chuỗi theo một cấu trúc cụ thể""")
    
    ex_73 = textwrap.dedent('''\
    #ai vietnam
    s = "Hello, {}"
    print(s.format("world"))
    ''')
    key = "ex_73"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_73, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 7.4. Nhóm mã hóa và giải mã
Các hàm này mã hóa và giải mã chuỗi.

- ord(): Trả về giá trị Unicode của một ký tự.
- chr(): Trả về ký tự tương ứng với giá trị Unicode.""")
    
    ex_74 = textwrap.dedent('''\
    #ai vietnam
    c = 'a'
    unicode_value = ord(c)
    print(f"ord(c): {unicode_value}")

    code = 97
    character = chr(code)
    print(f"chr(code): {character}")
    ''')
    key = "ex_74"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_74, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 7.5. Nhóm kiểm tra ký tự
Các hàm này kiểm tra ký tự trong chuỗi.

- all(): Kiểm tra nếu tất cả các phần tử của một iterable là True.
- any(): Kiểm tra nếu bất kỳ phần tử nào của một iterable là True.""")
    
    ex_75 = textwrap.dedent('''\
    #ai vietnam
    s = "abc"
    all_alpha = all(c.isalpha() for c in s)
    print(f"all(c.isalpha() for c in s): {all_alpha}")

    s_with_digits = "abc123"
    any_digit = any(c.isdigit() for c in s_with_digits)
    print(f"any(c.isdigit() for c in s_with_digits): {any_digit}")     
    ''')
    key = "ex_75"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_75, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 7.6. Nhóm thao tác trên chuỗi
Các hàm này thao tác trực tiếp trên chuỗi.

- max(): Trả về ký tự lớn nhất trong chuỗi.
- min(): Trả về ký tự nhỏ nhất trong chuỗi.
- sorted(): Trả về một danh sách các ký tự trong chuỗi đã được sắp xếp.
- reversed(): Trả về một iterator với các ký tự trong chuỗi theo thứ tự ngược lại.""")
    
    ex_76 = textwrap.dedent('''\
    #ai vietnam
    s = "cba"
    max_char = max(s)
    print(f"max(s): {max_char}")

    min_char = min(s)
    print(f"min(s): {min_char}")

    sorted_chars = sorted(s)
    print(f"sorted(s): {sorted_chars}")

    reversed_s = ''.join(reversed(s))
    print(f"''.join(reversed(s)): {reversed_s}")
    ''')
    key = "ex_76"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_76, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""| Nhóm             | Hàm          | Mô tả chức năng                              | Ví dụ                                         |
|------------------|--------------|----------------------------------------------|----------------------------------------------|
| Kiểm tra chuỗi   | `len()`      | Trả về độ dài của chuỗi                      | `len("Hello")`  # Trả về 5                   |
|                  | `isinstance()` | Kiểm tra nếu một đối tượng là một thể hiện của một lớp cụ thể | `isinstance("Hello", str)`  # Trả về True  |
| Chuyển đổi kiểu  | `str()`      | Chuyển đổi một đối tượng thành chuỗi         | `str(123)`  # Trả về '123'                   |
|                  | `int()`      | Chuyển đổi chuỗi thành số nguyên             | `int("123")`  # Trả về 123                   |
|                  | `float()`    | Chuyển đổi chuỗi thành số thực               | `float("123.45")`  # Trả về 123.45           |
| Định dạng        | `format()`   | Định dạng chuỗi                              | `"Hello, {}".format("world")`  # Trả về 'Hello, world' |
| Mã hóa và giải mã | `ord()`      | Trả về giá trị Unicode của một ký tự         | `ord('a')`  # Trả về 97                      |
|                  | `chr()`      | Trả về ký tự tương ứng với giá trị Unicode    | `chr(97)`  # Trả về 'a'                      |
| Kiểm tra ký tự   | `all()`      | Kiểm tra nếu tất cả các phần tử của một iterable là True | `all(c.isalpha() for c in "abc")`  # Trả về True |
|                  | `any()`      | Kiểm tra nếu bất kỳ phần tử nào của một iterable là True | `any(c.isdigit() for c in "abc123")`  # Trả về True |
| Thao tác với chuỗi | `max()`     | Trả về ký tự lớn nhất trong chuỗi            | `max("cba")`  # Trả về 'c'                   |
|                  | `min()`      | Trả về ký tự nhỏ nhất trong chuỗi            | `min("cba")`  # Trả về 'a'                   |
|                  | `sorted()`   | Trả về một danh sách các ký tự trong chuỗi đã được sắp xếp | `sorted("cba")`  # Trả về ['a', 'b', 'c']  |
|                  | `reversed()` | Trả về một iterator với các ký tự trong chuỗi theo thứ tự ngược lại | `''.join(reversed("abc"))`  # Trả về 'cba' |""")
    
    st.markdown(r"""## 8. Các lỗi thường gặp khi làm việc với String""" )
    st.markdown(r"""### 8.1 Sử dụng chỉ số ngoài phạm vi (IndexError)""" )
    ex_81 = textwrap.dedent('''\
    #ai vietnam
    s = "hello"
    print(s[5])
    ''')
    key = "ex_81"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_81, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 8.2 Sử dụng phương thức trên kiểu dữ liệu không phù hợp (TypeError)""" )
    ex_82 = textwrap.dedent('''\
    #ai vietnam
    num = 123
    print(num.lower())  # TypeError: 'int' object has no attribute 'lower'
    ''')
    key = "ex_82"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_82, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    st.markdown(r"""### 8.3 Sử dụng sai cú pháp (SyntaxError)""" )
    ex_83 = textwrap.dedent('''\
    #ai vietnam
    name = "ai viet nam'
    ''')
    key = "ex_83"
    file_name = data_dir+key+".py"
    result, code_ex, key = ui.code_io(ex_83, key=key, file_name=file_name, type_out="python", show_now=True)
    ui.ai(result, code_ex, key)
    
    st.success('Chúc mừng bạn đã hoàn thành bài học nha!', icon="✅")