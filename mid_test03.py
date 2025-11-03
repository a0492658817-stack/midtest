def rot(ops, r, c, n):
    for op in reversed(ops):
        if op == 'R':
            r, c = n - 1 - c, r
        elif op == 'L':
            r, c = c, n - 1 - r
        elif op == 'H':
            c = n - 1 - c
        elif op == 'V':
            r = n - 1 - r
    return r * n + c + 1

def main():
    n = int(input().strip())
    ops = input().strip()
    for r in range(n):
        for c in range(n):
            val = rot(ops, r, c, n)
            end = ' ' if c < n - 1 else '\n'
            print(val, end=end)
main()
