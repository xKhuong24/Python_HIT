Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
Python là ngôn ngữ thông dịch (interpreted language).
Giải thích:
•	Khi bạn viết mã Python và chạy nó, mã nguồn không được biên dịch thành mã máy trực tiếp như C/C++.
•	Thay vào đó, trình thông dịch Python (Python Interpreter) sẽ đọc và thực thi từng dòng mã một cách tuần tự.
•	Quá trình này thường gồm 2 bước:
1.	Biên dịch nội bộ (ngầm) sang mã bytecode (.pyc) — đây không phải là mã máy, mà là mã trung gian.
2.	Mã bytecode này sau đó được thực thi bởi Python Virtual Machine (PVM).
 Do đó, Python là ngôn ngữ thông dịch, nhưng có một bước biên dịch nội bộ sang bytecode để tăng hiệu năng.
________________________________________
Bài 2: Kiến thức chuẩn bị trước buổi 2
1. Các kiểu dữ liệu trong Python (Data Types)
Kiểu dữ liệu	Ví dụ	Giải thích
int	5, -10, 0	Số nguyên
float	3.14, -2.0	Số thực (thập phân)
str	'Hello', "Python"	Chuỗi ký tự
bool	True, False	Kiểu logic
list	[1, 2, 3], ['a', 'b']	Danh sách
tuple	(1, 2), ('a', 'b')	Bộ giá trị
dict	{'name': 'Khuong', 'age': 20}	Từ điển (key-value)
set	{1, 2, 3}	Tập hợp (không trùng lặp)
________________________________________
2. Các toán tử trong Python (Operators)
•	Toán tử số học: +, -, *, /, //, %, **
•	Toán tử so sánh: ==, !=, >, <, >=, <=
•	Toán tử logic: and, or, not
•	Toán tử gán: =, +=, -=, *=, /=, //=, %=, **=
•	Toán tử thuộc tính / thành phần:
o	in, not in: kiểm tra phần tử có trong list, chuỗi,...
•	Toán tử bit (nâng cao): &, |, ^, ~, <<, >>
________________________________________
3. Mệnh đề điều kiện và vòng lặp
➤ Câu lệnh điều kiện if
python
CopyEdit
x = 5
if x > 0:
    print("Dương")
elif x == 0:
    print("Không")
else:
    print("Âm")
➤ Vòng lặp for
python
CopyEdit
for i in range(5):
    print(i)  # In ra từ 0 đến 4
➤ Vòng lặp while
python
CopyEdit
i = 0
while i < 5:
    print(i)
    i += 1
➤ Các từ khóa trong vòng lặp
•	break: thoát khỏi vòng lặp
•	continue: bỏ qua lần lặp hiện tại
•	pass: không làm gì cả (chỉ là chỗ giữ chỗ)

4. Kiểu dữ liệu True, False (kiểu bool)
•	Là kiểu dữ liệu logic, chỉ có hai giá trị: True và False
•	Thường dùng trong điều kiện, kiểm tra logic.
➤ Các giá trị được xem là False:
python
CopyEdit
False, None, 0, 0.0, "", [], (), {}
➤ Còn lại đều được xem là True
Ví dụ:
python
CopyEdit
x = 0
if x:
    print("True")
else:
    print("False")  # kết quả in ra là False vì 0 là giá trị sai

