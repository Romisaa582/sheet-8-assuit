def check(num,arr1,arr2):
    sum_arr1=sum(arr1)
    sum_arr2=sum(arr2)

    if sum_arr1==sum_arr2:
        return "Yes"
    else:
        return "No"

num=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(check(num,arr1,arr2))