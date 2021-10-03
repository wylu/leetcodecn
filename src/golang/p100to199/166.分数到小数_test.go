package p100to199

import "testing"

func Test_fractionToDecimal(t *testing.T) {
	type args struct {
		numerator   int
		denominator int
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
				numerator:   1,
				denominator: 2,
			},
			want: "0.5",
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				numerator:   2,
				denominator: 1,
			},
			want: "2",
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				numerator:   2,
				denominator: 3,
			},
			want: "0.(6)",
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				numerator:   4,
				denominator: 333,
			},
			want: "0.(012)",
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				numerator:   1,
				denominator: 5,
			},
			want: "0.2",
		},
		// Case 6
		{
			name: "Case 6",
			args: args{
				numerator:   -(1 << 31),
				denominator: -1,
			},
			want: "2147483648",
		},
		// Case 7
		{
			name: "Case 7",
			args: args{
				numerator:   -50,
				denominator: 8,
			},
			want: "-6.25",
		},
		// Case 8
		{
			name: "Case 8",
			args: args{
				numerator:   7,
				denominator: -12,
			},
			want: "-0.58(3)",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := fractionToDecimal(tt.args.numerator, tt.args.denominator); got != tt.want {
				t.Errorf("fractionToDecimal() = %v, want %v", got, tt.want)
			}
		})
	}
}
