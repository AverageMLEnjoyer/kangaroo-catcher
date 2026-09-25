from itertools import product


def hypotheses():
    """
    Generate every integer quadruple (x0, y0, a, b) exactly once.

    The quadruples are enumerated by increasing radius

        r = max(|x0|, |y0|, |a|, |b|).

    Only the new boundary of the 4D cube [-r, r]^4 is generated,
    thus previously visited quadruples are never checked again.
    """
    yield 0, 0, 0, 0

    radius = 1

    while True:
        inside = range(-radius + 1, radius)
        full = range(-radius, radius + 1)

        # We classify a point by the first coordinate that reaches
        # the boundary ±radius. This guarantees uniqueness.
        for boundary_index in range(4):
            for prefix in product(inside, repeat=boundary_index):
                for boundary_value in (-radius, radius):
                    for suffix in product(full, repeat=3 - boundary_index):
                        yield prefix + (boundary_value,) + suffix

        radius += 1


def kangaroo_position(x0, y0, a, b, step):
    """Return the kangaroo's position after 'step' moves."""
    return x0 + a * step, y0 + b * step


def catch_kangaroo(real_x0, real_y0, real_a, real_b, verbose=False):
    """
    Enumerate all possible trajectories and place one trap per step.

    At step t, if the current hypothesis is (x0, y0, a, b),
    the trap is placed at

        (x0 + a*t, y0 + b*t).

    The function returns as soon as the trap position equals the
    real kangaroo position.
    """
    for step, (x0, y0, a, b) in enumerate(hypotheses()):
        kangaroo = kangaroo_position(
            real_x0, real_y0, real_a, real_b, step
        )
        trap = kangaroo_position(x0, y0, a, b, step)

        if verbose:
            print(
                f"Step {step}: hypothesis={(x0, y0, a, b)}, "
                f"trap={trap}, kangaroo={kangaroo}"
            )

        if trap == kangaroo:
            return {
                "step": step,
                "position": kangaroo,
                "hypothesis": (x0, y0, a, b),
                "real_trajectory": (
                    real_x0,
                    real_y0,
                    real_a,
                    real_b,
                ),
            }


def read_integer(prompt):
    """Read one integer from standard input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")


def main():
    print("Kangaroo Catcher")
    print("================")
    print()
    print("Choose the kangaroo's hidden trajectory.")
    print("The kangaroo starts at (x0, y0) and moves")
    print("by the fixed integer vector (a, b) every step.")
    print()

    real_x0 = read_integer("Initial x-coordinate x0: ")
    real_y0 = read_integer("Initial y-coordinate y0: ")
    real_a = read_integer("x-coordinate step a: ")
    real_b = read_integer("y-coordinate step b: ")

    print()
    print("Catching...")

    result = catch_kangaroo(
        real_x0,
        real_y0,
        real_a,
        real_b,
    )

    print()
    print("The kangaroo has been caught.")
    print(f"Step: {result['step']}")
    print(f"Position: {result['position']}")
    print(f"Hypothesis used: {result['hypothesis']}")


if __name__ == "__main__":
    main()
