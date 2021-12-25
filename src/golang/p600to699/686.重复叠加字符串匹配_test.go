package p600to699

import "testing"

func Test_repeatedStringMatch(t *testing.T) {
	type args struct {
		a string
		b string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{a: "abcd", b: "cdabcdab"},
			want: 3,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{a: "a", b: "aa"},
			want: 2,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{a: "aa", b: "a"},
			want: 1,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{a: "abcd", b: "abcdb"},
			want: -1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := repeatedStringMatch(tt.args.a, tt.args.b); got != tt.want {
				t.Errorf("repeatedStringMatch() = %v, want %v", got, tt.want)
			}
		})
	}
}
