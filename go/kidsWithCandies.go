package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
	res := make([]bool, len(candies))
	highest := highestNumber(candies)

	for i, v := range candies {
		if v+extraCandies >= highest {
			res[i] = true
		} else {
			res[i] = false
		}
	}

	return res
}

func highestNumber(arr []int) int {
	highest := arr[0]
	for _, v := range arr {
		if v > highest {
			highest = v
		}
	}

	return highest
}
