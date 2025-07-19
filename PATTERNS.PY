# for i in range(1,6):
#     row=""
#     for j in range(i):
#         row+="*"
#     print(row)
#
# for i in range(1,6):
#     row=0
#     for j in range(1,i+1):
#         row=row*10+j
#     print(row)

# row = ""
# for i in range(1, 6):
#     row += chr(96 + i)  
#     print(row)


# for i in range(6,1,-1):
#     row=0
#     for y in range(i):
#         row = row * 10+y
#     print(row)

# for i in range(5,0,-1):
#     row = 0
#     for y in range(i):
#         row = row * 10+i
#     print(row)

# for i in range(5,0,-1):
#     row=0
#     for y in range(i,0,-1):
#         row = row * 10+y
#     print(row)

for i in range(5,0,-1):
    row=''
    for y in range(5,5-i,-1):
        row += chr(97+y)
    print(row)






