package offer

/**
 * @File    :   05.替换空格.go
 * @Time    :   2020/07/03 23:41:03
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func replaceSpace(s string) string {
	res := []byte{}
	space := []byte("%20")
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			res = append(res, space...)
		} else {
			res = append(res, s[i])
		}
	}
	return string(res)
}
