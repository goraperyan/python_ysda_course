def find_value(nums: list[int] | range, value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if value > nums[mid]:
            left = mid + 1
        elif value < nums[mid]:
            right = mid
        else:
            return True
    return False
