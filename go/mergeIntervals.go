package main

func quickSort(arr [][]int, start, end int) {
	if start < end {
		pivot := partition(arr, start, end)
		quickSort(arr, start, pivot-1)
		quickSort(arr, pivot+1, end)
	}
}

func partition(arr [][]int, start, end int) int {
	pivot := arr[end][0]
	i := start - 1

	for j := start; j < end; j++ {
		if arr[j][0] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}

	arr[i+1], arr[end] = arr[end], arr[i+1]

	return i + 1
}

func mergeInterval(intervals [][]int) [][]int {
	res := [][]int{}

	quickSort(intervals, 0, len(intervals)-1)

	i := 0
	for i < len(intervals) {

		l1 := intervals[i]
		new := l1

		j := i

		for j < len(intervals) {
			l2 := intervals[j]
			if l1[1] >= l2[0] {
				if l1[1] < l2[1] {
					new[1] = l2[1]
				}
				if l1[0] > l2[0] {
					new[0] = l2[0]
				}
				j++
			} else {
				break
			}
		}

		res = append(res, new)
		i = j
	}

	return res
}
