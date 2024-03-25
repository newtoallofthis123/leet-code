package main

func mergeSortedArray(nums1 []int, m int, nums2 []int, n int) {
	temp := append(nums1[:m], nums2...)

	nums1 = temp

	for i := 0; i < len(nums1); i++ {
		for j := i; j < len(nums1); j++ {
			if nums1[i] > nums1[j] {
				tempNum := nums1[i]
				nums1[i] = nums1[j]
				nums1[j] = tempNum
			}
		}
	}
}
