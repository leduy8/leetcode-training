package main

// * https://leetcode.com/problems/missing-number/

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(missingNumber([]int{3, 0, 1}))                   // 2
	fmt.Println(missingNumber([]int{0, 1}))                      // 2
	fmt.Println(missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1})) // 8
}
	
func missingNumber(nums []int) int {
	slices.Sort(nums)

	for i := 0; i < nums[len(nums)-1]; i++ {
		if !slices.Contains(nums, i) {
			return i
		}
	}

	return len(nums)
}
