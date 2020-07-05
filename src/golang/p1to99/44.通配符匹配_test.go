package p1to99

import "testing"

func TestIsMatch(t *testing.T) {
	if isMatch("aa", "a") != false {
		t.Fail()
	}

	if isMatch("aa", "*") != true {
		t.Fail()
	}

	if isMatch("cb", "?a") != false {
		t.Fail()
	}

	if isMatch("adceb", "*a*b") != true {
		t.Fail()
	}

	if isMatch("acdcb", "a*c?b") != false {
		t.Fail()
	}
}
