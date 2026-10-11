"""
Fixed-width binary counter supporting increment and decrement operations.
"""


class BinaryCounter:
    """
    Fixed-width binary counter stored in little-endian order.
    """

    def __init__(self, k: int) -> None:
        """
        Create a k-bit counter initialized to zero.
        """
        self.A: list[int] = [0] * k
        self.k: int = k

    def increment(self) -> None:
        """
        Increment the counter by one modulo 2^k.
        """
        i = 0

        while i < self.k and self.A[i] == 1:
            self.A[i] = 0
            i += 1

        if i < self.k:
            self.A[i] = 1

    def decrement(self) -> None:
        """
        Decrement the counter by one modulo 2^k.
        """
        i = 0

        while i < self.k and self.A[i] == 0:
            self.A[i] = 1
            i += 1

        if i < self.k:
            self.A[i] = 0

    def __str__(self) -> str:
        """
        Return the binary representation of the counter.
        """
        return "".join(reversed([str(b) for b in self.A]))


def main():
    bc = BinaryCounter(3)

    print("increment")
    for _ in range(10):
        bc.increment()
        print(bc, int(str(bc), 2))

    print("decrement")
    for _ in range(13):
        bc.decrement()
        print(bc, int(str(bc), 2))


if __name__ == "__main__":
    main()
