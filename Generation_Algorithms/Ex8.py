# Bài 10: Mã Gray 1
# Trong hệ thống số học, số nhị phân là cách mặc định để biểu diễn các số. Tuy nhiên, trong nhiều ứng dụng của điện tử và truyền thông, người ta thường sử dụng một biến thể của nhị phân gọi là mã Gray.

# Mã Gray độ dài n là một danh sách các xâu nhị phân độ dài n, trong đó:

# Mã đầu tiên là một xâu toàn số 0.

# Mỗi mã kế tiếp chỉ khác mã trước đó đúng một bit.

# Ví dụ:
# Với n = 3, ta có các mã Gray như sau:

# 000, 001, 011, 010, 110, 111, 101, 100
# Viết chương trình liệt kê tất cả các mã Gray có độ dài n.

# Dòng đầu tiên là một số nguyên T — số lượng bộ test.

# T dòng tiếp theo, mỗi dòng chứa một số nguyên n — độ dài của mã Gray.

# 1 ≤ T, n ≤ 10

# Output:
# Với mỗi test, in ra một dòng chứa các mã Gray độ dài n, cách nhau bởi dấu cách.

# Ví dụ:
# Input:
# 2
# 3
# 4
# Output:
# 000 001 011 010 110 111 101 100  
# 0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000
# Bài Làm 
# ----------------Cách1------------------------- #
n = int(input("Nhập n: "))
results = []
for i in range(2**n):
    gray = i ^ (i >> 1)
    results.append(format(gray, f'0{n}b'))
print(' '.join(results))
 