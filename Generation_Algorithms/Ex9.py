"""
Bài 13. Xâu AB đặc biệt

Đề bài:
Một xâu ký tự S = (s1, s2, ..., sn) được gọi là xâu AB độ dài N nếu mỗi ký tự si trong S
chỉ là ký tự 'A' hoặc 'B'.

Cho hai số tự nhiên N và K (với 1 < K < N < 15). Hãy liệt kê tất cả các xâu AB có độ dài N,
sao cho trong mỗi xâu chỉ chứa duy nhất một dãy gồm K ký tự 'A' liên tiếp (không có dãy
nào khác gồm K hoặc nhiều hơn K ký tự 'A').

Dữ liệu vào:
    - Một dòng duy nhất chứa hai số nguyên N và K.

Dữ liệu ra:
    - Dòng đầu tiên ghi số lượng xâu AB thỏa mãn yêu cầu.
    - Các dòng tiếp theo, mỗi dòng ghi một xâu AB hợp lệ, theo thứ tự từ điển.

Ví dụ:
Input:
5 3

Output:
5
AAABA
AAABB
ABAAA
BAAAB
BBAAA
"""
# Bài Làm 
# ----------------Cách1------------------------- #
def ktao(n , a):
    for i in range(n):
        a[i] = '0'

def sinh():
    global ok , a , n 
    i = n -1 
    while(i >= 0 and a[i] == '1'):
        a[i] = '0'
        i -=1
    if i < 0 : 
        ok = 0 
    else : 
        a[i] = '1'
    
if __name__ =='__main__':
    n , k = map(int , input().split())
    a = ['0'] * n 
    ok = 1 
    ktao(n , a)
    result = []
    while(ok):
        res = ''
        for i in range(n):
            if a[i] == '0' : 
                res += 'A'
            else : 
                res += 'B'
        result.append(res)
        res = ''
        sinh()
    ans = []
    for x in result:
        cnt = 0
        segments = []  
        valid = True

        for i in range(len(x)):
            if x[i] == 'A':
                cnt += 1
            else:
                if cnt > 0:
                    segments.append(cnt)
                cnt = 0

        if cnt > 0:
            segments.append(cnt)

        count_k = segments.count(k)
       
        if count_k == 1 and all(seg <= k for seg in segments):
            ans.append(x)

    print(len(ans))
    for x in sorted(ans):
        print(x)
