package main

import "fmt"

func myPow(x float64, n int) float64 {
	result := 1.0
	if(n == 0){
		return result
	} else if(n == 1){
		return x
	} else if(n > 1){
		for i:=0; i<n ; i++{
			result *= x
		}
	} else if(n < 1){
		for i:=0; i > n; i --{
			result *= 1/x
		}
	}
	return result
}

func main(){
	fmt.Println(myPow(1.00000, -2147483648))
}
