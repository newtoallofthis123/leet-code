package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	res := make([][]int, 2)

	for _, v := range nums1 {
		if !containsIntInArr(nums2, v) && !containsIntInArr(res[0], v) {
			res[0] = append(res[0], v)
		}
	}

	for _, v := range nums2 {
		if !containsIntInArr(nums1, v) && !containsIntInArr(res[1], v) {
			res[1] = append(res[1], v)
		}
	}

	return res
}

func containsIntInArr(arr []int, b int) bool {
	for _, v := range arr {
		if v == b {
			return true
		}
	}

	return false
}
