import functools


def to_32bit_string(x: str) -> int:
    return "{0:b}".format(x).zfill(32)


def hamming_distance(x: int, y: int) -> int:
    return functools.reduce(
        lambda total, pair: total + (0 if pair[0] == pair[1] else 1),
        zip(to_32bit_string(x), to_32bit_string(y)),
        0)
