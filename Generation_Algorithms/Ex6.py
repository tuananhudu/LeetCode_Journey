# 📝 Đề bài:
# Cho số nguyên dương N. Nhiệm vụ của bạn là liệt kê tất cả các hoán vị của dãy số {1, 2, 3, ..., N} theo thứ tự ngược từ lớn đến bé (từ điển ngược).

# 📥 Input:
# Dòng đầu tiên là số nguyên T — số lượng test case.

# T dòng tiếp theo, mỗi dòng là một số nguyên N tương ứng với từng test case.

# ⚙️ Ràng buộc:
# 1 ≤ T ≤ 10

# 1 ≤ N ≤ 10

# 📤 Output:
# Với mỗi test case, in ra tất cả các hoán vị của dãy {1, 2, ..., N} trên một dòng.

# Các hoán vị được in nối tiếp nhau, cách nhau đúng 1 khoảng trắng.

# 📌 Ví dụ:
# Input:
# 2
# 2
# 3
# Output:
# 21 12
# 321 312 231 213 132 123

# Bài Làm 
# ----------------Cách1------------------------- #
class SinhHoanVi():
    def __init__(self , n):
        self.n = n 
        self.ok = True 
        self.a = [0] * (n+1)
    def ktao(self):
        for i in range(1 , self.n+1):
            self.a[i] = i 
        return self 
    def sinh(self):
        i = self.n - 1 
        while(i > 0 and self.a[i] >self.a[i+1]):
            i -= 1 
        if i == 0 : 
            self.ok = False 
        else : 
            j = self.n
            while(i < j):
                if (self.a[i] < self.a[j]):
                    self.a[i] , self.a[j] = self.a[j] , self.a[i]
                    self.a[i+1:] = self.a[i+1:][::-1]
                    break 
                else : 
                    j -= 1
    def sinh_all(self):
        self.ktao()
        res = ''
        results = []
        while(self.ok):
            for i in range(1 , self.n+1):
                res += str(self.a[i])
            results.append(res)
            res = ''
            self.sinh()
        for i in results[::-1]:
            print(int(i) , end = ' ')
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = SinhHoanVi(n)
        a.sinh_all()
        print()

# ----------------Cách2------------------------- #
# def ktao(n , a):
#     for i in range(1, n+1):
#         a[i] = i 

# def sinh():
#     global ok , a , n 
#     i = n - 1 
#     while(i > 0 and a[i] > a[i+1]):
#         i -=1 
#     if i == 0 : 
#         ok = False 
#     else : 
#         j = n 
#         while(i < j):
#             if (a[i] < a[j]):
#                 a[i] , a[j] = a[j] , a[i]
#                 a[i+1:] = a[i+1:][::-1]
#                 break
#             else : 
#                 j -= 1 

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         ok = 1
#         a = [0] * (n+1)
#         ktao(n , a)
#         res = ''
#         result = []
#         while(ok):
#             for i in range(1 , n+1):
#                 # res += (a[i] - '0')
#                 res += str(a[i])
#             result.append(res)
#             res = ''
#             sinh()
#         for i in result[::-1] :
#             print(int(i) , end =' ') 
#         print()

