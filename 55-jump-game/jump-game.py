class Solution(object):
    def canJump(self, nums):
        t=[]
        bool = False 
        if nums == [0]:
            return True
        if nums [0] == 0:
            return bool
        b = len(nums)-1
        for i in range (len(nums)):
            if nums [i] == 0:
                t.append(i)
        if nums [b] == 0:
            count = 1
            for m in range (b,1,-1):
                if nums [b-1] == 0:
                    count +=1
                else:
                    if nums[b-1] < count:
                        bool = False
            t.remove(b)
        if not t:
            return True
        for a in t:
            count = 2
            for m in range (a,0,-1):
                bool = False
                if nums [m-1] < count:
                    count += 1
                else:
                    bool = True
                    break 
            if bool == False:
                return bool
        return bool
                    
                


