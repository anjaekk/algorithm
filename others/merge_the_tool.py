#hackerrank

def merge_the_tools(string, k):
    chunk = []
    for i in range(0, len(string)):
        chunk.append(string[i])
        if len(chunk) == k:
            list = []
            for c in chunk:
                if c not in list: list.append(c)
            print(''.join(list))
            chunk = []

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
