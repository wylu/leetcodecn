package p200to299

import "testing"

func Test_numberToWords(t *testing.T) {
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
				num: 123,
			},
			want: "One Hundred Twenty Three",
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				num: 12345,
			},
			want: "Twelve Thousand Three Hundred Forty Five",
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				num: 1234567,
			},
			want: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				num: 1234567891,
			},
			want: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				num: 0,
			},
			want: "Zero",
		},
		// Case 6
		{
			name: "Case 6",
			args: args{
				num: 14,
			},
			want: "Fourteen",
		},
		// Case 7
		{
			name: "Case 7",
			args: args{
				num: 110,
			},
			want: "One Hundred Ten",
		},
		// Case 8
		{
			name: "Case 8",
			args: args{
				num: 115,
			},
			want: "One Hundred Fifteen",
		},
		// Case 9
		{
			name: "Case 9",
			args: args{
				num: 1000,
			},
			want: "One Thousand",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberToWords(tt.args.num); got != tt.want {
				t.Errorf("numberToWords() = %v, want %v", got, tt.want)
			}
		})
	}
}
