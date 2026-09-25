from itertools import islice

from main import hypotheses, kangaroo_position, catch_kangaroo


def test_first_hypotheses_are_unique():
    sample = list(islice(hypotheses(), 5000))
    assert len(sample) == len(set(sample))


def test_small_cube_is_fully_enumerated():
    expected = {
        (x0, y0, a, b)
        for x0 in range(-1, 2)
        for y0 in range(-1, 2)
        for a in range(-1, 2)
        for b in range(-1, 2)
    }

    generated = set(islice(hypotheses(), len(expected)))

    assert generated == expected


def test_position():
    assert kangaroo_position(2, -1, 3, 4, 5) == (17, 19)


def test_catcher_eventually_catches_small_examples():
    examples = [
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (-1, 1, 1, 0),
        (0, -1, 0, 1),
        (1, 1, -1, -1),
    ]

    for trajectory in examples:
        result = catch_kangaroo(*trajectory)
        assert result["position"] == kangaroo_position(
            *trajectory,
            result["step"],
        )
