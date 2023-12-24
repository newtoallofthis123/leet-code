package main

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	res := []int{}
	common1 := []int{}
	common2 := []int{}

	for _, num := range nums1 {
		if isInArray(nums2, num) {
			common1 = append(common1, num)
		}
	}

	for _, num := range nums2 {
		if isInArray(nums1, num) {
			common2 = append(common2, num)
		}
	}

	res = append(res, len(common1))
	res = append(res, len(common2))

	return res
}

func isInArray(arr []int, val int) bool {
	for _, v := range arr {
		if v == val {
			return true
		}
	}
	return false
}

// https://leetcode.com/problems/find-common-elements-between-two-arrays/submissions/1127322277/
// Runtime: 16 ms, beats 79.39% of go submissions.
// Memory usage: 6.7 MB, beats 100.00% of go submissions.
