package p1to99

import "testing"

func TestLongestValidParentheses(t *testing.T) {
	got := longestValidParentheses("(()")
	if got != 2 {
		t.Fail()
	}

	got = longestValidParentheses(")()())")
	if got != 4 {
		t.Fail()
	}

	got = longestValidParentheses(")()(()")
	if got != 2 {
		t.Fail()
	}
}
