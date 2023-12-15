package main

func twoSum(nums []int, target int) []int {
	res := make([]int, 2)

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[j]+nums[i] == target {
				res[0] = i
				res[1] = j
			}
		}
	}

	return res
}
