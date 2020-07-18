package p200to299

import (
	"reflect"
	"testing"
)

func Test_findWords(t *testing.T) {
	type args struct {
		board [][]byte
		words []string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				board: [][]byte{
					[]byte{'o', 'a', 'a', 'n'},
					[]byte{'e', 't', 'a', 'e'},
					[]byte{'i', 'h', 'k', 'r'},
					[]byte{'i', 'f', 'l', 'v'},
				},
				words: []string{"oath", "pea", "eat", "rain"},
			},
			want: []string{"oath", "eat"},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findWords(tt.args.board, tt.args.words); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("findWords() = %v, want %v", got, tt.want)
			}
		})
	}
}
