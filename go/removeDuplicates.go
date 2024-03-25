package main

func removeDuplicates(nums []int) int {
	visted := []int{}

	for i, num := range nums {
		if containsIntInArr(visted, num) {
			nums[i] = -1
		} else {
			visted = append(visted, num)
		}
	}

	moveToStart(nums)

	return len(visted)
}
