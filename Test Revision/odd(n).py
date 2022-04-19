def odd (n):
    if n == 1:
        return 1
    else: 
        result = odd(n//2) + n
        return result

print(odd(8))