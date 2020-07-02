package offer

import (
	"testing"
)

func TestFindRepeatNumber(t *testing.T) {
	nums := []int{2, 3, 1, 0, 2, 5, 3}
	got := findRepeatNumber(nums)
	want := 2
	if got != want {
		t.Fail()
	}
}
