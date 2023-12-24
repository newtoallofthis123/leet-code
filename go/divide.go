package main

func divide(dividend int, divisor int) int {
	isNegative := false
	if dividend < 0 || divisor < 0 {
		if dividend < 0 && divisor < 0 {
			isNegative = false
		} else {
			isNegative = true
		}
	}

	dividend = abs(dividend)
	divisor = abs(divisor)

	if abs(divisor) == 1 {
		if isNegative {
			return checkOverflow(-dividend)
		}
		return checkOverflow(dividend)
	}

	quotient := 0
	for dividend >= divisor {
		dividend -= divisor
		quotient++
	}

	if isNegative {
		return checkOverflow(-quotient)
	}

	return checkOverflow(quotient)
}

func checkOverflow(res int) int {
	if res > 2147483647 {
		res = 2147483647
	} else if res < -2147483648 {
		res = -2147483648
	}
	return res
}
