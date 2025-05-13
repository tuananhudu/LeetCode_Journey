# Bài 4: Xâu AB
# Đề bài:
# Một xâu ký tự str được gọi là xâu AB nếu mỗi ký tự trong xâu hoặc là ký tự 'A' hoặc là ký tự 'B'.

# Ví dụ:

# str = "ABBABB" là xâu AB có độ dài 6.

# Yêu cầu:
# Hãy liệt kê tất cả các xâu AB có độ dài n.

# Input:
# Dòng đầu tiên là số lượng bộ test T.

# Tiếp theo là T dòng, mỗi dòng là một số nguyên dương n — độ dài của xâu AB cần liệt kê.

# Ràng buộc:

# 1 ≤ T ≤ 10

# 1 ≤ n ≤ 10

# Output:
# Với mỗi test, in ra tất cả các xâu AB có độ dài n trên một dòng.

# Các xâu cách nhau đúng 1 khoảng trắng.

# Ví dụ:
# Input:
# 2
# 2
# 3
# Output:
# AA AB BA BB
# AAA AAB ABA ABB BAA BAB BBA BBB
# Bài Làm 
# ----------------Cách1------------------------- #
class SinhNhiPhan:
    def __init__(self  , n):
        self.n = n
        self.ok = True
        self.a = ['0'] * n

    def sinh(self):
        i = self.n - 1
        while i >= 0 and self.a[i] == '1':
            self.a[i] = '0'  
            i -= 1
        if i < 0:
            self.ok = False
        else:
            self.a[i] = '1'

    def sinh_all(self):
            while self.ok:
                for i in range(self.n):
                    print('A' if self.a[i] == '0' else 'B', end='')
                print()
                self.sinh()

if __name__ == '__main__':
    t = int(input())
    n = [int(input()) for i in range(t)]
    for i in range(len(n)):
        a = SinhNhiPhan(n[i])
        a.sinh_all()
        print()
# ----------------Cách2------------------------- #
# def sinh():
#     global ok, a, n
#     i = n - 1
#     while i >= 0 and a[i] == '1':
#         a[i] = '0'
#         i -= 1
#     if i < 0:
#         ok = 0
#     else:
#         a[i] = '1'

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         a = ['0'] * n
#         ok = 1
#         while ok:
#             for i in range(n):
#                 print('A' if a[i] == '0' else 'B', end='')
#             print()
#             sinh()
