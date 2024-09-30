def main(
    a,
    b,
    c,
):
    p = a + b + c
    res = p * (p - a) * (p - b) * (p - c)
    return res
