Two Sum:
Approach - 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        for i in range(len(nums)):
            remSum = target-nums[i]
            if remSum in Hmap:
                return [i,Hmap[remSum]]
            Hmap[nums[i]] = i

Approach - 2
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
   int i,j;
    *returnSize=2;
    int *a=malloc(2 * sizeof(int));
   for(i=0;i<numsSize;i++){
       for(j=0;j<numsSize;j++){
           if(nums[i]+nums[j]==target && i!=j){
               a[0]=i;
               a[1]=j;
               return a;}
           }
       }
return (int *) -1;
}
