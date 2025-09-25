''' with open('sample.txt','r') as f:
f1=f.read(1)
print(f1)
'''
try:

    with open("sample.txt", "r") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()

        print("Line 1:", line1)
        print("Line 2:", line2)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

