cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[0:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))