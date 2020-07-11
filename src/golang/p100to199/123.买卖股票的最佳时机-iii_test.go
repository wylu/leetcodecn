package p100to199

import "testing"

func Test_maxProfit3(t *testing.T) {
	type args struct {
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
				prices: []int{1, 2, 3, 4, 5},
			},
			want: 4,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				prices: []int{3,3,5,0,0,3,1,4},
			},
			want: 6,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit3(tt.args.prices); got != tt.want {
				t.Errorf("maxProfit3() = %v, want %v", got, tt.want)
			}
		})
	}
}
