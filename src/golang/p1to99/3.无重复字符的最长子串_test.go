package p1to99

import "testing"

func Test_lengthOfLongestSubstring(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{s: "abcabcbb"},
			want: 3,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{s: "bbbbb"},
			want: 1,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{s: "pwwkew"},
			want: 3,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{s: ""},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := lengthOfLongestSubstring(tt.args.s); got != tt.want {
				t.Errorf("lengthOfLongestSubstring() = %v, want %v", got, tt.want)
			}
		})
	}
}
