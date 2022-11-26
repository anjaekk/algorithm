from collections import Counter

def company_logo(s: str) -> None:
    counters = Counter(sorted(s)).most_common(3) 
    for k, y in counters:
        print(k, y)

if __name__ == '__main__':
    s = input()
    company_logo(str(s))
