# 📝 Đề bài:
# Cho hai số nguyên dương N và K. Hãy liệt kê tất cả các tập con gồm K phần tử được chọn từ tập {1, 2, 3, ..., N}.

# Các tập con được liệt kê theo thứ tự từ điển tăng dần. Mỗi tập con được in ra trên một dòng, các phần tử viết liền nhau.

# 📥 Input:
# Dòng đầu tiên là số nguyên T — số lượng test case.

# T dòng tiếp theo, mỗi dòng gồm 2 số nguyên N và K — tương ứng với một test case.

# ⚙️ Ràng buộc:
# 1 ≤ T ≤ 100

# 1 ≤ K ≤ N ≤ 15

# 📤 Output:
# Với mỗi test case, in ra tất cả các tổ hợp K phần tử từ tập {1, 2, ..., N}.

# Các tổ hợp được in nối tiếp nhau trên một dòng, mỗi tổ hợp cách nhau đúng 1 khoảng trắng.

# 📌 Ví dụ:
# Input:
# 2
# 4 3
# 5 3
# Output:
# 123 124 134 234
# 123 124 125 134 135 145 234 235 245 345

# Bài Làm 
# ----------------Cách1------------------------- #
class SinhToHop():
    def __init__(self , n , k):
        self.n = n 
        self.k = k 
        self.a = [0] * (k+1)
        self.ok = True 
    def ktao(self):
        for i in range(1 , self.k+1):
            self.a[i] = i 
        return self 
    def sinh(self):
        i = self.k 
        while(i > 0 and self.a[i] == self.n - self.k + i):
            i -= 1 
        if i == 0 : 
            self.ok = False 
        else : 
            self.a[i] +=1 
            j = i +1 
            while(j <= self.k):
                self.a[j] = self.a[j-1] + 1 
                j+=1
        return self 
    def sinh_all(self):
        self.ktao()
        while(self.ok):
            for i in range(1 , self.k+1):
                print(self.a[i] , end ='')
            self.sinh()
            print(end =' ')
        print()
        return self 

if __name__ == '__main__':
    t = int(input())
    a = [list(map(int, input().split())) for _ in range(t)]
    for i in range(len(a)):
        X = SinhToHop(a[i][0] , a[i][1])
        X.sinh_all()


# ----------------Cách2------------------------- #
# def ktao(k , a):
#     for i in range(1 , k+1):
#         a[i] = i 

# def sinh():
#     global ok , a , n  , k 
#     i = k 
#     while(i > 0 and a[i] == n-k+i):
#         i -= 1 
#     if i == 0 : 
#         ok = False 
#     else : 
#         a[i] +=1 
#         j = i+1 
#         while(j <=k ):
#             a[j] = a[j-1]+1 
#             j +=1

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         ok = True
#         n,k = map(int , input().split())
#         a = [0] * (k+1)
#         ktao(k , a)
#         while(ok):
#             for i in range(1 , k+1):
#                 print(a[i] , end = '')
#             sinh()
#             print(end = ' ')
#         print()


        