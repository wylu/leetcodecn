package p300to399

import "testing"

func Test_getMoneyAmount(t *testing.T) {
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
			args: args{n: 4},
			want: 4,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{n: 5},
			want: 6,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{n: 6},
			want: 8,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{n: 10},
			want: 16,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getMoneyAmount(tt.args.n); got != tt.want {
				t.Errorf("getMoneyAmount() = %v, want %v", got, tt.want)
			}
		})
	}
}
