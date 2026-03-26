def merge_sorted_arrays(nums1, nums2):
    i, j, k = 0, 0, 0
    left = nums1[: len(nums1) - len(nums2)]
    right = nums2
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums1[k] = left[i]
            i += 1
        else:
            nums1[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        nums1[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums1[k] = right[j]
        j += 1
        k += 1

    return nums1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    result = merge_sorted_arrays(nums1, nums2)
    val = [1, 2, 2, 3, 5, 6]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
