package p100to199

import "testing"

func Test_maxProfit4(t *testing.T) {
	type args struct {
		k      int
		prices []int
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
				k:      2,
				prices: []int{3, 2, 6, 5, 0, 3},
			},
			want: 7,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				k:      2,
				prices: []int{2, 1, 2, 0, 1},
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit4(tt.args.k, tt.args.prices); got != tt.want {
				t.Errorf("maxProfit4() = %v, want %v", got, tt.want)
			}
		})
	}
}
