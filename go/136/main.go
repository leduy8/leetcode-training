package main

// * https://leetcode.com/problems/single-number/

import "fmt"

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))       // 1
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2})) // 4
	fmt.Println(singleNumber([]int{1}))             // 1
}

// * |A	|B	|A ^ B|
// * |0	|0	|0	  |
// * |0	|1	|1	  |
// * |1	|0	|1	  |
// * |1	|1	|0	  |

func singleNumber(nums []int) int {
	result := 0

	for _, num := range nums {
		result = result ^ num // XOR operator
	}

	return result
}
