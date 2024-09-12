n = int(input())
s = input()

word = ""
for i in range(n):
    length = len(s)
    middle = length // 2
    word += s[middle]
    s = s[:middle] + s[middle+1:]

print(word)