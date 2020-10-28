package p1to99

import (
	"math"
	"testing"
)

func Test_divide(t *testing.T) {
	type args struct {
		dividend int
		divisor  int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				dividend: 10,
				divisor:  3,
			},
			want: 3,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				dividend: math.MinInt32,
				divisor:  -1,
			},
			want: math.MaxInt32,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				dividend: math.MinInt32,
				divisor:  1,
			},
			want: math.MinInt32,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := divide(tt.args.dividend, tt.args.divisor); got != tt.want {
				t.Errorf("divide() = %v, want %v", got, tt.want)
			}
		})
	}
}
