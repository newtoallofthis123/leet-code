package main

import "math"

func distance(x1, y1, x2, y2 int) float64 {
	return math.Sqrt(math.Pow(float64(x2-x1), 2) + math.Pow(float64(y2-y1), 2))
}

func countPoints(points [][]int, queries [][]int) []int {
	res := make([]int, len(queries))

	for i, circle := range queries {
		xc, yc, r := circle[0], circle[1], circle[2]

		for _, point := range points {
			x, y := point[0], point[1]
			if distance(xc, yc, x, y) <= float64(r) {
				res[i]++
			}
		}
	}

	return res
}
