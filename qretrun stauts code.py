import requests
x=requests.get('https://w3schools.com')
print(x.status_code)

# row=3
# for i in range(row):
#     for j in range(row-i):
#         print(' ', end='') 
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==row-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print() 


# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()    



# size=int(input("enter the the size"))
# i=1
# while i<(size):
#     j=1
#     while j<(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         j+=1
#     i+=1        
# print()    

# n = 6
# for i in range(1, n+1):
#     for j in range(i):
#         if j == 0 or j == i-1:
#             print('*', end='')
#         else:
#             if i != n:
#                 print(' ', end='')
#             else:
#                 print('*', end='')
#     print()    





# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for j in range(2 * i + 1):
#         print('*', end='')
#     print()
# for i in range(n - 1):
#     for j in range(i + 1):
#         print(' ', end='')
#     for j in range(2*(n - i - 1) - 1):
#         print('*', end='')
#     print()





# n = 5
# # downward pyramid
# for i in range(n-1):
#     for j in range(i):
#         print(' ', end='')
#     for k in range(2*(n-i)-1):
#         print('*', end='')
#     print()
# # upward pyramid
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end='')
#     for k in range(2*i+1):
#         print('*', end='')
#     print()    





# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == j or i + j == size - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()    