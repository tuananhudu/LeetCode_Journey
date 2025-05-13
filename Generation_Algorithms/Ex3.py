# Bài toán: Sinh hoán vị của n phần tử

# Đề bài:
# Cho số nguyên dương n. Hãy liệt kê tất cả các hoán vị của n phần tử (có thể là các số từ 1 đến n).

# Yêu cầu:
# In ra tất cả các hoán vị của dãy số từ 1 đến n.

# Các hoán vị có thể in theo thứ tự bất kỳ (nếu đề không yêu cầu tăng dần).

# Bài Làm 

# ----------------Cách1------------------------- #
class SinhHoanVi():
    def __init__(self , n ):
        self.n = n 
        self.ok = True 
        self.a = [0] * (n+1)
    def ktao(self):
        for i in range(1 , self.n + 1):
            self.a[i] = i 
    def sinh(self):
        i = self.n - 1 
        while(i > 0 and self.a[i] > self.a[i+1]):
            i -= 1 
        if i == 0 : 
            self.ok = False 
        else : 
            j = self.n 
            while(i < j):
                if(self.a[i] < self.a[j]): 
                    self.a[i],self.a[j] = self.a[j] , self.a[i]
                    self.a[i+1:] = self.a[i+1:][::-1]
                    return 
                else : 
                    j -= 1 
    def sinh_all(self):
        self.ktao()
        while(self.ok):
            for i in range(1 , self.n +1):
                print(self.a[i] , end = '')
            print()
            self.sinh()

if __name__ == '__main__':
    n = int(input())
    a = SinhHoanVi(n)
    a.sinh_all()


# ----------------Cách2------------------------- #
# n = int(input())
# a = [0] * (n+1)
# ok = 1 

# def ktao():
#     for i in range(1 , n+1):
#         a[i] = i

# def sinh():
#     global ok 
#     i = n - 1 
#     while(i> 0 and a[i] > a[i+1]):
#         i -= 1 
#     if i == 0 : 
#         ok = 0 
#     else : 
#         j = n 
#         while(i < j):
#             if (a[i] < a[j]):
#                 a[i] , a[j] = a[j] , a[i]
#                 a[i+1:] = a[i+1:][::-1]
#             else : 
#                 j -= 1 
# if __name__ == '__main__':
#     ktao()
#     while(ok):
#         for i in range(1 , n+1):
#             print(a[i] , end = '')
#         print(end = '\n')
#         sinh()


