# 잃어버린 괄호(백준 1541번)

# 입력
# 55-50+40
# 출력
# -35


expression = input()

nums = expression.split("-")
results = []
if "-" not in expression:
    print(sum(list(map(int, expression.split("+")))))
else:
    for num in nums:
        num_list = map(int, num.split("+"))
        results.append(sum(num_list))
    result = results[0]
    for i in range(1, len(results)):
        result -= results[i]
    print(result)
