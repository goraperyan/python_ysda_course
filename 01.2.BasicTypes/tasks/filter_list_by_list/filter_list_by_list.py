def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    ans = []
    it_a = 0
    it_b = 0

    while it_b < len(lst_b) and it_a < len(lst_a):
        if lst_a[it_a] < lst_b[it_b]:
            ans.append(lst_a[it_a])
            it_a += 1
        elif lst_a[it_a] == lst_b[it_b]:
            it_a += 1
        else:
            it_b += 1

    while it_a < len(lst_a):
        ans.append(lst_a[it_a])
        it_a += 1

    return ans
