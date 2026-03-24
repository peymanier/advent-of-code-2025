# def merge(nums1, nums2):
#     result = []
#
#     i = 0
#     j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] <= nums2[j]:
#             result.append(nums1[i])
#             i += 1
#         else:
#             result.append(nums2[j])
#             j += 1
#
#     if i < len(nums1):
#         result.extend(nums1[i:])
#
#     if j < len(nums2):
#         result.extend(nums2[j:])
#
#     return result
#
#
# def sort_array(nums: list[int]) -> list[int]:
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#     left = sort_array(nums[:mid])
#     right = sort_array(nums[mid:])
#     return merge(left, right)


# def merge(arr: list[int], l: int, m: int, r: int):
#     nums1 = arr[l : m + 1]
#     nums2 = arr[m + 1 : r + 1]
#     k = l
#
#     i = 0
#     j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] <= nums2[j]:
#             arr[k] = nums1[i]
#             i += 1
#         else:
#             arr[k] = nums2[j]
#             j += 1
#
#         k += 1
#
#     while i < len(nums1):
#         arr[k] = nums1[i]
#         i += 1
#         k += 1
#
#     while j < len(nums2):
#         arr[k] = nums2[j]
#         j += 1
#         k += 1
#
#     return
#
#
# def sort_array(nums: list[int]) -> list[int]:
#     def merge_sort(arr: list[int], l: int, r: int):
#         if l == r:
#             return arr
#
#         m = (l + r) // 2
#         merge_sort(arr, l, m)
#         merge_sort(arr, m + 1, r)
#         merge(arr, l, m, r)
#         return arr
#
#     return merge_sort(nums, 0, len(nums) - 1)


def merge2(nums: list[int], l: int, mid: int, r: int):
    k = l
    i = 0
    left = nums[l : mid + 1]
    j = 0
    right = nums[mid + 1 : r + 1]

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return


def sort_array(nums: list[int]) -> list[int]:
    def merge_sort(l: int, r: int):
        if l >= r:
            return

        mid = (l + r) // 2
        merge_sort(l, mid)
        merge_sort(mid + 1, r)
        merge2(nums, l, mid, r)
        return

    merge_sort(0, len(nums) - 1)
    return nums


def main():
    nums = [5, 2, 3, 1]
    result = sort_array(nums)
    val = [1, 2, 3, 5]
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
