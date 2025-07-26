def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    ans = [0] * (len(lst_a) + len(lst_b))
    a = 0
    b = 0
    while a < len(lst_a) and b < len(lst_b):
        if lst_a[a] >= lst_b[b]:
            ans[a + b] = lst_b[b]
            b += 1
        else:
            ans[a + b] = lst_a[a]
            a += 1
    while a < len(lst_a):
        ans[a + b] = lst_a[a]
        a += 1
    while b < len(lst_b):
        ans[a + b] = lst_b[b]
        b += 1
    return ans


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a + lst_b)
