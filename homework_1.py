def palindrome(a):
    b = len(a)
    for i in range(l//2):
        if a[i] == a[-1-i]:
            return True
    return False

a = input('Введите слово или строку без пробелов и других знаков: ')
print(palindrome(a))
