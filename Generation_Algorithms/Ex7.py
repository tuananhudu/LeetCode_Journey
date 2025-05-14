# Bài 8: Xâu Nhị Phân Có K Bit 1
# Đề bài:
# Cho hai số nguyên dương N và K, hãy liệt kê tất cả các xâu nhị phân có độ dài N mà trong đó có đúng K bit bằng 1. Các xâu được in ra theo thứ tự từ điển tăng dần.

# Input:
# Dòng đầu tiên là số nguyên T — số lượng bộ test (1 ≤ T ≤ 20).

# Tiếp theo là T dòng, mỗi dòng gồm hai số nguyên N và K (1 ≤ K ≤ N ≤ 16) — tương ứng với độ dài xâu và số lượng bit 1 cần có trong xâu.

# Output:
# Với mỗi test case, in ra tất cả các xâu nhị phân độ dài N có đúng K bit 1, theo thứ tự từ điển tăng dần.

# Mỗi xâu in trên một dòng.

# Sau khi in xong kết quả của mỗi test case, không cần in dòng trống.

# Ví dụ:
# 2
# 4 2
# 3 2
# Output:
# 0011
# 0101
# 0110
# 1001
# 1010
# 1100
# 011
# 101
# 110

# Bài Làm 
# ----------------Cách1------------------------- #
class SinhNhiPhan():
    def __init__(self , n , k):
        self.n = n 
        self.k = k 
        self.ok = True 
        self.a = ['0'] * n 
    def ktao(self):
        for i in range(self.n):
            self.a[i] = '0'
    def sinh(self):
        i = self.n -1 
        while(i >= 0 and self.a[i] == '1'):
            self.a[i] = '0'
            i -=1 
        if i < 0 : 
            self.ok = False 
        else : 
            self.a[i] = '1'
    def sinh_all(self):
        results = []
        self.ktao()
        while(self.ok):
            cnt = 0  
            res = ''
            for i in range(self.n):
                if self.a[i] == '1':
                    cnt += 1 
                res += self.a[i]
            if cnt == self.k :
                results.append(res)
            self.sinh()
        for x in results : 
            print(x)
        print("________________Hello______________")
if __name__ =='__main__':
    t = int(input())
    a = [list(map(int , input().split())) for _ in range(t)]
    for i in range(t):
        ta = SinhNhiPhan(a[i][0] , a[i][1])
        ta.sinh_all()

# ----------------Cách1------------------------- #
# def ktao(n , a):
#     for i in range(n):
#         a[i] = '0'

# def sinh():
#     global ok , a , n
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
#         n , k = map(int , input().split())
#         ok = 1 
#         a = ['0'] * n
#         results = []
#         ktao(n , a)
#         while ok: 
#             cnt = 0
#             res = ''
#             for i in range(n):
#                 if a[i] == '1':
#                     cnt += 1
#                 res += a[i]
#             if cnt == k:
#                 results.append(res)
#             sinh()
#         for x in results : 
#             print(x)
#         print("________________Hello______________")

