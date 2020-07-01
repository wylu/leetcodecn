package p700to799

import (
	"testing"
)

func TestFindLength(t *testing.T) {
	A := []int{1, 2, 3, 2, 1}
	B := []int{3, 2, 1, 4, 7}
	got := findLength(A, B)
	want := 3
	if got != want {
		t.Fail()
	}
}
