
"""
def add_numbers():
    answer = 0
    for number in range(1, 10 + 1):
        print(number)
        answer = answer + number
    return answer


answer = add_numbers()
print(answer)
print(answer)
"""

def add_numbers(x, y):
    ans = 0
    for number in range(x, y+1):
        ans = ans + number
    return ans

ans = add_numbers(333,778)
print(ans)
