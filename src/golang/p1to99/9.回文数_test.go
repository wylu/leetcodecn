package p1to99

import "testing"

func Test_isPalindrome(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{x: 0},
			want: true,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{x: -121},
			want: false,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{x: 121},
			want: true,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{x: 10},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.x); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
