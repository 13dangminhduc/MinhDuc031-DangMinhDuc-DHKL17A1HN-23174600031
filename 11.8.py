# xac dinh danh sach co chua so may man hay khong
nums=[2,6,7,9]
def has_lucky_number(nums):
    for i in nums:
        if i%7==0:
            return True
print(has_lucky_number(nums))