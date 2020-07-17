package p600to699

import "testing"

func Test_validPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{s: "aba"},
			want: true,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{s: "abca"},
			want: true,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{s: "eeccccbebaeeabebccceea"},
			want: false,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{s: "acupxxpucua"},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := validPalindrome(tt.args.s); got != tt.want {
				t.Errorf("validPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
