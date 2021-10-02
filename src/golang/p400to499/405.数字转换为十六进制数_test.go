package p400to499

import "testing"

func Test_toHex(t *testing.T) {
	type args struct {
		num int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				num: 0,
			},
			want: "0",
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				num: 1,
			},
			want: "1",
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				num: -1,
			},
			want: "ffffffff",
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				num: (1 << 31) - 1,
			},
			want: "7fffffff",
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				num: (1 << 31),
			},
			want: "80000000",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toHex(tt.args.num); got != tt.want {
				t.Errorf("toHex() = %v, want %v", got, tt.want)
			}
		})
	}
}
