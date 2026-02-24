import random
from os import getenv
from unittest import TestCase

if getenv("TESTING") != "1":
    raise OSError(  # noqa: TRY003
        "Environment is not ready for testing",  # noqa: EM101
    )


def total(a: int, b: int) -> int:
    return a + b


class TotalTesCase(TestCase):
    def test_total(self) -> None:
        num_a = random.randint(1, 20)
        num_b = random.randint(1, 20)
        result = total(num_a, num_b)
        expected_result = num_a + num_b
        self.assertEqual(expected_result, result)
