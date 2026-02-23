import random
from os import getenv
from unittest import TestCase

TESTING_ENV_ERROR = "Environment is not ready testing"

if getenv("TESTING") != "1":
    raise OSError(
        TESTING_ENV_ERROR,
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
