package offer

import "testing"

func Test_cuttingRope2(t *testing.T) {
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
			args: args{n: 1000},
			want: 620946522,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := cuttingRope2(tt.args.n); got != tt.want {
				t.Errorf("cuttingRope2() = %v, want %v", got, tt.want)
			}
		})
	}
}
