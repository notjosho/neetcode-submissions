class Solution {
    public boolean hasDuplicate(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        while(i < nums.length){
            if (i == nums.length - 1){
                break;
            }
            if(nums[i] == nums[j]){
                return true;
            } else {
                if(j - 1 == i){
                    j = nums.length - 1;
                    i++;
                } else {
                    j--;
                }
            }
        }
        return false;
    }
}
