# arr=[1,2,3,4,5,6]
# ele=0
# def linear(arr,ele):
#     for i in range(len(arr)):
#         if (arr[i]==ele):
#             return True
#     return False
# print(linear(arr,ele))


# l1 = [4, 8, 1, 7, 3]
# max = l1[0]
# for i in l1:
#     if i > max:
#         max = i
# print(max)

# l1 = [4, 8, 1, 7, 3]
# max = l1[0]
# for i in l1:
#     if i < max:
#         max = i
# print(max)

# matrix = [[1, 2, 3],  
#           [4, 5, 6],  
#           [7, 8, 9]]  
# target = 5
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == target :
#             print("found in ", (i,j))

# arr = [2, 4, 6, 4, 8, 4, 9]  
# target = 4
# first = -1
# last = -1
# for i in range(len(arr)):
#     if arr[i] == target:
#         first += 1
#     else:
#         last += 1

# print(first)
# print(last)

# arr=[1,2,3,4,5,6,7,1,7]
# target=1
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(i)

# arr = [5, 12, 3, 7, 18]
# K = 6
# for i in arr:
#     if i > K:
#         print(i)

# string = "supriya"
# target = "r"
# for i in range(len(string)):
#     if target in string[i]:
#         print(i)
#         break

# arr = [4, 8, 1, 7, 3, 6]
# target = 7
# for i in range(1,4):
#     if arr[i] == target:
#         print(i)

# arr = [1, 3, 5, 2, 3, 4]
# dup = False
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             dup = True
#             break
#     if dup:
#         break
# print(dup)

# arr = [2, 4, 7, 9, 6]
# even_count=0
# odd_count=0
# for i in arr:
#     if i%2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print(even_count)
# print(odd_count)

# arr = [5, 8, 12, 3, 7]
# sort1= sorted(arr, reverse=True)
# second = sort1[1]
# print(second)

# def binarysearch(arr,target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [2,4,5,6,7,8,11,44,77,88,100]
# target = 88
# res = binarysearch(arr,target)

# if res != -1:
#     print("found",res)
# else:
#     print("not found")

# def binarysearch_first_occurrence(arr, target): 
#     left = 0
#     right = len(arr) - 1
#     result = -1  # to store the index of first occurrence
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             result = mid        # store current index
#             right = mid - 1     # keep looking on the left side
#         elif arr[mid] < target:
#             left = mid + 1
        
            
#     return result

# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# res = binarysearch_first_occurrence(arr, target)

# if res != -1:
#     print(target, "first occurrence at index", res)
# else:
#     print(target, "not found")






# def binarysearch_last_occurrence(arr, target): 
#     left = 0
#     right = len(arr) - 1
#     result = -1  # to store the index of last occurrence
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             result = mid  
#             left = mid + 1   # keep looking on the right side for last occurrence
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     return result

# # Example usage:
# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# res = binarysearch_last_occurrence(arr, target)

# if res != -1:
#     print(target, "last occurrence at index", res)
# else:
#     print(target, "not found")

# def first_occ(arr,target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left<= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def last_occ(arr,target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left<= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             left = mid + 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def count_occurrences(arr, target):
#     first = first_occ(arr, target)
#     if first == -1:
#         return 0
#     last = last_occ(arr, target)
#     return last - first + 1
# arr = [1, 2, 2, 2, 3, 4, 5]
# target = 2
# print("Count of", target, "is", count_occurrences(arr, target))

# def sort(nums):
#     count = 0
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#                 count += 1
#     print(count)
#     return nums
# nums = [4, 3, 2, 1]
# sort(nums)

# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] < nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# nums = [3, 1, 4, 2]
# sort(nums)
# print(nums)

# def sort(nums,k):
#     for i in range(k-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# nums = [9, 8, 7, 6, 5, 4, 3]
# k=4
# sort(nums,k)
# print(nums)


# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         swapp=False
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#         if not swapp:
#             print("Already sorted")
#             return
#     print("Not sorted but now sorted")

# nums=[1,2,3,4,5]
# sort(nums)

# def ss(arr):
#     for i in range(len(arr)-1):
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[index]: 
#                 index = j
#         arr[i], arr[index] = arr[index], arr[i]
#     return arr
# arr=[2,66,88,9,10]
# print(ss(arr))


# arr=[9,8,7,6,5,4,3,2,1,0]
# for i in range(len(arr)-1):
#     index=i
#     for j in range(i+1,len(arr)):
#         index=j
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
#     print(arr)
# print(arr)

# def ss(arr):
#     for i in range(len(arr)-1):
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[index]: 
#                 index = j
#         arr[i], arr[index] = arr[index], arr[i]
#     return arr
# arr=[9, 4, 7, 1, 3]
# ss(arr)
# print(arr[0])


# def ss(arr,k):
#     for i in range(k):
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[index]: 
#                 index = j
#         arr[i], arr[index] = arr[index], arr[i]
#     return arr[k-1]
# arr=[9, 4, 7, 1, 3]
# k=3
# print(ss(arr,k))

# def selection_sort_count_swaps(arr):
#     swaps = 0
#     for i in range(len(arr)-1):
#         index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[index]:
#                 index = j
#         if index != i:
#             arr[i], arr[index] = arr[index], arr[i]
#             swaps += 1
#     return swaps

# arr = [5, 4, 3, 2, 1]
# print(selection_sort_count_swaps(arr))  

# arr = ["banana", "apple", "cherry", "date"]
# n=len(arr)
# for i in range(n-1):
#     index=i
#     for j in range(i+1,n):
#         if arr[j]<arr[index]:
#             index=j
#     arr[i],arr[index]=arr[index],arr[i]
# print(arr)


# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] < nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j-1]
#                 nums[j-1] = temp
# nums = [3, 1, 4, 2]
# sort(nums)
# print(nums)

#FIRST METHOD
# def inssot(nums):
#     for i in range(1, len(nums)):
#         j = i
#         while j > 0 and nums[j-1] > nums[j]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]
#             j -= 1

# nums = [2, 4, 6, 79, 1, 3, 99]
# inssot(nums)
# print(nums)

arr = [7]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):  
        if arr[j] < arr[j - 1]:  
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
        else:
            break  
print(arr)


