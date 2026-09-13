import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        mid = (len1+len2)/2

        #偶数，有两个mid
        if (len1+len2)%2==0:
            mid1 = mid-1
            mid2 = mid
        #奇数，有一个mid
        else:
            mid = math.floor(mid)

        res = []
        l1 = l2 = 0
        if (len1+len2)%2==0:
            while l1<len1 and l2<len2:
                if nums1[l1]<=nums2[l2]:
                    res.append(nums1[l1])
                    l1+=1
                else:
                    res.append(nums2[l2])
                    l2+=1
                if len(res)==mid1+1:
                    mid1_num = res[-1]
                if len(res)==mid2+1:
                    mid2_num = res[-1]
            if l1<len1:
                while l1<len1:
                    res.append(nums1[l1])
                    if len(res)==mid1+1:
                        mid1_num = res[-1]
                    if len(res)==mid2+1:
                        mid2_num = res[-1]
                    l1+=1
            if l2<len2:
                while l2<len2:
                    res.append(nums2[l2])
                    if len(res)==mid1+1:
                        mid1_num = res[-1]
                    if len(res)==mid2+1:
                        mid2_num = res[-1]
                    l2+=1

            output = (mid1_num+mid2_num)/2
        
        else:
            while l1<len1 and l2<len2:
                if nums1[l1]<=nums2[l2]:
                    res.append(nums1[l1])
                    l1+=1
                else:
                    res.append(nums2[l2])
                    l2+=1
                if len(res)==mid+1:
                    mid_num = res[-1]
            if l1<len1:
                while l1<len1:
                    res.append(nums1[l1])
                    if len(res)==mid+1:
                        mid_num = res[-1]
                    l1+=1
            if l2<len2:
                while l2<len2:
                    res.append(nums2[l2])
                    if len(res)==mid+1:
                        mid_num = res[-1]
                    l2+=1
            output = mid_num
        
        
        return output
            

        
      

        