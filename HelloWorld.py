largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if str(num)=="done":
        print("\nMaximum is", largest)
        print("Minimum is", smallest)
        quit("\ndone")
    try:
        num=int(num)

    except:
        continue

    if smallest is None:
        smallest=num
    elif num < smallest :
        smallest=num
    if largest is None:
        largest=num
    elif num > largest:
        largest=num
    if num=="done":break
