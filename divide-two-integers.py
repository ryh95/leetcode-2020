class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos_flag = True
        # handle the case that one of numbers are negatives
        if (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            pos_flag = False
            dividend,divisor = abs(dividend),abs(divisor)
        if dividend <= 0 and divisor < 0:
            dividend, divisor = abs(dividend), abs(divisor)

        num_arr,e,id = [],divisor,1
        id_arr = []
        while True:
            num_arr.append(e)
            id_arr.append(id)
            e += e
            id += id
            if e > dividend:
                break
        num_arr = [0] + num_arr
        id_arr = [0] + id_arr
        l,h = num_arr[-1],num_arr[-1] + num_arr[-1]
        l_id,h_id = id_arr[-1],id_arr[-1] + id_arr[-1]
        j = len(num_arr) - 2
        while l < h:
            mid_num = l + num_arr[j]
            if mid_num > dividend:
                h = mid_num
                h_id = id_arr[j] + l_id
            else:
                l = mid_num
                l_id = id_arr[j] + l_id
            j -= 1
            if h_id - l_id <= 1:
                break
        res = h_id - 1 if pos_flag else 1 - h_id
        # final check
        if res <= (1 << 31) -1 and res >= - (1 << 31):
            return res
        else:
            return (1 << 31) -1

dividend,divisor = 28,3
dividend,divisor = 10,3
dividend,divisor = 0,3
dividend,divisor = -1,-1
dividend,divisor = -2147483648,-1
print(Solution().divide(dividend,divisor))
