class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        candi_counter,num_counter,res = {},{},[]
        for n in nums:
            if len(candi_counter) ==3 and n not in candi_counter:
                min_key = min(candi_counter,key=candi_counter.get)
                candi_counter[min_key] -=1
                if candi_counter[min_key] == 0: candi_counter.pop(min_key)
                continue
            candi_counter[n] = candi_counter.get(n,0)+1
        for i,n in enumerate(nums,1):
            if n in candi_counter:
                num_counter[n] = num_counter.get(n,0)+1
        for k,v in num_counter.items():
            if v > int(i/3): res.append(k)
        return res