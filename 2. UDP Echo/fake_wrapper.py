import udp_echo_client
from typing import Iterator
import random

random.seed(42)

# or just use a global...


class FakeTime:
    def __iter__(self) -> "FakeTime":
        self.a = 0.0
        return self

    def __next__(self) -> float:
        x = self.a
        self.a += random.random()
        return x


thing = iter(FakeTime())
udp_echo_client.time.time = thing.__next__  # type: ignore
udp_echo_client.main()
