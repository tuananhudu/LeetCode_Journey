# ### **Đề bài: Sinh tất cả chuỗi nhị phân có độ dài n**

# **Mô tả:**

# Cho một số nguyên **n** (1 ≤ n ≤ 10), sinh tất cả các chuỗi nhị phân có độ dài **n**.

# **Input:**
# - Một số nguyên **n** (1 ≤ n ≤ 10).

# **Output:**
# - In tất cả các chuỗi nhị phân có độ dài **n**.

# Bài Làm 

# ----------------Cách1------------------------- #
class SinhNhiPhan():
    def __init__(self , n ):
        self.n = n 
        self.ok = True 
        self.a = ['0'] * n
    def sinh(self):
        i = self.n - 1 
        while(i >= 0 and self.a[i] == '1'):
            self.a[i] = '0'
            i -=1
        if i < 0 : 
            self.ok = False 
        else :
            self.a[i] ='1'
    def sinh_all(self):
        while(self.ok):
            print(''.join(self.a))
            self.sinh()

if __name__ == '__main__':
    n = int(input())
    a = SinhNhiPhan(n)
    a.sinh_all()
# ----------------Cách2------------------------- #
# n = int(input())
# ok = 1 
# a = ['0'] * n 

# def sinh():
#     global ok , a 
#     i = n -1 
#     while(i >= 0 and a[i] == '1'):
#         a[i] = '0'
#         i -=1 
#     if(i < 0 ):
#         ok = 0 
#     else :
#         a[i] = '1'

# if __name__ == '__main__':
#     while(ok):
#         print(''.join(a))
#         sinh()
