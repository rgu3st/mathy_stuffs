""" Dynamic programming version of calculating fib(n). """

def fib(n:int)->int:
    '''Use DP to fill in a table and return the fib number.'''
    if n <= 2:
        return 1
    table = []
    table.append(1)
    table.append(1)
    for i in range(2, n):
        table.append( table[i-1] + table[i-2] )
    return table[n-1]  # The count is 1-indexed but we stored these zero-indexed


if __name__ == "__main__":
    n = input("Which fib?")
    n = int(n)
    if n > 0:
        fib_num = fib(n)
        print(f"Fib number {n} is {fib_num}")