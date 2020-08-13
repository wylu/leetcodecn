package p1to99

import "testing"

func Test_isValid(t *testing.T) {
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
			args: args{
				s: "()",
			},
			want: true,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				s: "()[]{}",
			},
			want: true,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				s: "(]",
			},
			want: false,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				s: "([)]",
			},
			want: false,
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				s: "{[]}",
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValid(tt.args.s); got != tt.want {
				t.Errorf("isValid() = %v, want %v", got, tt.want)
			}
		})
	}
}
