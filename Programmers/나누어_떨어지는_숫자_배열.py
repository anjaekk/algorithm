def solution(arr, divisor):
  answer = []
  for i in arr:
    if i % divisor == 0:
      answer.append(i)
    else:
      continue
  if answer == []:
    answer.append(-1)
  return sorted(answer)
