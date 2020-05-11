import random

PIVOT_FIRST = 0
PIVOT_MIDDLE = 1
PIVOT_MEDIAN_3 = 3

pivot_method = PIVOT_MEDIAN_3

total_count = 0

def quick_sort(alist):
   global total_count
   total_count = 0
   quick_sort_helper(alist,0,len(alist)-1)

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1,last)

def partition(alist,first,last):
   global total_count
   mid = (first+last)//2
   if pivot_method == PIVOT_FIRST:
      piv_index = first
   elif pivot_method == PIVOT_MIDDLE:
      piv_index = mid
   else:
      median_list = [alist[first], alist[mid], alist[last]]
      median_list.sort()
#      print("med:", median_list, median_list[1])
      if alist[first] == median_list[1]:
          piv_index = first
      elif alist[mid] == median_list[1]:
          piv_index = mid
      else:
          piv_index = last

#   piv_index = (first+last)//2
   pivotvalue = alist[piv_index]
   temp = alist[first] # move pivot out of the way
   alist[first] = alist[piv_index]
   alist[piv_index] = temp
#   print("list start:", alist)
#   print("pivot:", pivotvalue)

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           total_count += 1
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           total_count += 1
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]          # put pivot into splitpoint
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

#   print("list done :", alist) print()

   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(total_count, alist)

n = 100
my_randoms = random.sample(range(10000), n)
quick_sort(my_randoms)
print ("n =", n, "Final:", my_randoms, "\n count =", total_count)

n = 200
my_randoms = random.sample(range(10000), n)
quick_sort(my_randoms)
print ("n =", n, "Final:", my_randoms, "\n count =", total_count)

n = 400
my_randoms = random.sample(range(10000), n)
quick_sort(my_randoms)
print ("n =", n, "Final:", my_randoms, "\n count =", total_count)

n = 800
my_randoms = random.sample(range(10000), n)
quick_sort(my_randoms)
print ("n =", n, "Final:", my_randoms, "\n count =", total_count)

n = 100
my_list = list(range(n))
quick_sort(my_list)
print ("n =", n, "Final:", my_list, "\n count =", total_count)

n = 200
my_list = list(range(n))
quick_sort(my_list)
print ("n =", n, "Final:", my_list, "\n count =", total_count)

n = 400
my_list = list(range(n))
quick_sort(my_list)
print ("n =", n, "Final:", my_list, "\n count =", total_count)

n = 800
my_list = list(range(n))
quick_sort(my_list)
print ("n =", n, "Final:", my_list, "\n count =", total_count)