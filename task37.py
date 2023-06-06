# последовательность в обратном порядке

n = 5
# l = [3, 4, 5, 6, 7]

# l[::-1]
# print(l[::-1])
def print_revers(n):
    if n == 0:
        return ''
    k = int(input())
    return print_revers(n - 1) + ' ' + str(k)

print(print_revers(n))