package main

func moveZeroes(nums []int) {
	var i, j int
	for i < len(nums) {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
		i++
	}
	for j < len(nums) {
		nums[j] = 0
		j++
	}
}
