from typing import Type, Union


class OddStream():
    def __init__(self) -> None:
        self.current = 1

    def get_next(self) -> int:
        result = self.current
        self.current += 2
        return result



class EvenStream():
    def __init__(self) -> None:
        self.current = 0

    def get_next(self) -> int:
        result = self.current
        self.current += 2
        return result


def print_from_stream(
    n: int, 
    stream_name: Union[Type[OddStream], Type[EvenStream]] = EvenStream()
) -> None:
    stream_name.__init__()
    for _ in range(int(n)):
        print(stream_name.get_next())


q = int(input())
for _ in range(q):
    stream_name, n = input().split()
    if stream_name == "odd":
        print_from_stream(n, stream_name=OddStream())
    else:
        print_from_stream(n)
