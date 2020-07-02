package p300to399

import (
	"testing"
)

func TestKthSmallest(t *testing.T) {
	matrix := [][]int{
		{1, 2},
		{1, 3},
	}
	got := kthSmallest(matrix, 3)
	want := 2
	if got != want {
		t.Fail()
	}

	matrix = [][]int{
		{1, 9, 10},
		{5, 11, 13},
		{6, 13, 15},
	}
	got = kthSmallest(matrix, 3)
	want = 6
	if got != want {
		t.Fail()
	}
}
