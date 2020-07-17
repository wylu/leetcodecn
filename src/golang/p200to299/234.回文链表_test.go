package p200to299

import (
	"testing"
)

func Test_isPalindrome(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				head: MakeList(1, 1, 2, 1),
			},
			want: false,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				head: MakeList(1, 2, 3, 2, 1),
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.head); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
