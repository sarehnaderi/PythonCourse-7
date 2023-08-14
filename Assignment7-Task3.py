def sort():
    list = []
    num = int(input("Enter how many items that you want to check:"))
    i = 1
    while i <= num:
        list_member = int(input("Enter the number:"))
        list.append(list_member)
        i += 1 
    print("Your list:",list)
    list1=list.copy()
    list.sort()
    
    if list1 == list:
        print("Your list is sorted.")
    else:
        print("Initial list is not sorted.")
        print("Here is your sorted list:",list)
sort()