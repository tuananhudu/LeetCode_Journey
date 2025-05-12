# Cho tập hợp gồm n phần tử đánh số từ 1 đến n. Hãy liệt kê tất cả các tổ hợp gồm đúng k phần tử khác nhau được chọn ra từ tập hợp đó.

# Một tổ hợp là một tập con gồm k phần tử, trong đó thứ tự các phần tử không quan trọng.

# Các phần tử trong mỗi tổ hợp phải được in ra theo thứ tự tăng dần.

# Các tổ hợp phải được liệt kê theo thứ tự từ điển tăng dần.

#  Dữ liệu vào:
# Hai số nguyên dương n và k (1 ≤ k ≤ n ≤ 20).

#  Dữ liệu ra:
# In ra tất cả các tổ hợp k phần tử, mỗi tổ hợp trên một dòng.

# Các phần tử trong tổ hợp được in cách nhau bởi dấu cách và theo thứ tự tăng dần.

# Bài Làm 
# ----------------Cách1------------------------- #
class SinhToHop():
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.ok = True
        self.a = [0] * (k + 1)

    def ktao(self):
        for i in range(1, self.k + 1):
            self.a[i] = i

    def sinh(self):
        i = self.k
        while i > 0 and self.a[i] == self.n - self.k + i:
            i -= 1
        if i == 0:
            self.ok = False
        else:
            self.a[i] += 1
            for j in range(i + 1, self.k + 1):
                self.a[j] = self.a[j - 1] + 1

    def sinh_all(self):
        self.ktao()  # <-- Nhớ khởi tạo tổ hợp ban đầu
        while self.ok:
            for i in range(1, self.k + 1):
                print(self.a[i], end='')
            print()
            self.sinh()

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = SinhToHop(n, k)
    a.sinh_all()

# ----------------Cách2------------------------- #
# n, k = map(int, input().split())
# ok = 1 
# a = [0] * (k+1) 
# def ktao():
#     for i in range(1 , k+1):
#         a[i] = i 

# def sinh():
#     global ok 
#     i = k 
#     while(i >=0 and a[i] == n-k+i):
#         i -=1 
#     if i == 0 : 
#         ok = 0
#     else : 
#         a[i] += 1 
#         j = i +1 
#         while(j <= k):
#             a[j] = a[j-1] + 1 
#             j += 1 
# if __name__ =='__main__':
#     ktao()
#     while(ok):
#         for i in range(1,k+1):
#             print(a[i] , end = '')
#         print()
#         sinh()
