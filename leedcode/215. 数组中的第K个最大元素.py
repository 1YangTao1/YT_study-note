class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def adjust_heap(nums_list,index):
            l,r,largest = 2*index+1,2*index+2,index

            if l<len(nums_list) and nums_list[l]>nums_list[largest]:
                largest = l
            if r<len(nums_list) and nums_list[r]>nums_list[largest]:
                largest = r

            if nums_list[largest]!=nums_list[index]:
                nums_list[largest],nums_list[index] = nums_list[index],nums_list[largest]
                adjust_heap(nums_list,largest)

        def build_heap(nums_list):
            for i in range(len(nums_list)//2-1,-1,-1):
                adjust_heap(nums_list,i)

        def find_max(nums_list):
            build_heap(nums_list)
            for i in range(k-1):
                nums_list[0],nums_list[-1] = nums_list[-1],nums_list[0]
                nums_list.pop()
                adjust_heap(nums_list,0)
            return nums_list[0]

        return find_max(nums)