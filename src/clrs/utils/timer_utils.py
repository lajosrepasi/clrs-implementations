from time import monotonic


class Timer:
    def __init__(self, name: str | None = None):
        self.start: float = monotonic()
        self.name: str | None = name

    def stop(self) -> None:
        if self.name == None:
            print(monotonic() - self.start)
        else:
            print(self.name + ": " + str(monotonic() - self.start))
