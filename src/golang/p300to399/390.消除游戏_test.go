package p300to399

import "testing"

func Test_lastRemaining(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{n: 8},
			want: 6,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{n: 9},
			want: 6,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{n: 1},
			want: 1,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{n: 2},
			want: 2,
		},
		// Case 5
		{
			name: "Case 5",
			args: args{n: 2},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := lastRemaining(tt.args.n); got != tt.want {
				t.Errorf("lastRemaining() = %v, want %v", got, tt.want)
			}
		})
	}
}
