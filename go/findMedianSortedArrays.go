package main

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	nums := returnSorted(nums1, nums2)
	var median float64

	if len(nums)%2 != 0 {
		median = float64(nums[len(nums)/2])
	} else {
		avg := nums[len(nums)/2] + nums[(len(nums)/2)-1]
		median = float64(avg) / 2.0
	}

	return median
}

func returnSorted(nums1, nums2 []int) []int {
	nums := append(nums1, nums2...)

	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums)-1; j++ {
			if nums[j+1] < nums[j] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}

	return nums
}
