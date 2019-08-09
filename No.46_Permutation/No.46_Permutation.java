    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        permutation(ans, nums.length, nums);
        return ans;
    }
    private void permutation(List<List<Integer>> ans, int n, int[] nums)
    {
        if(n == 1)
        {
            List<Integer> per = new ArrayList<Integer>();
            for (int i : nums)
                per.add(i);
            ans.add(per);
        }
        else
        {
            for(int i = 0 ; i < n-1 ; i++)
            {
                permutation(ans, n-1, nums);
                if(n % 2 == 0)
                    swap(nums, i, n-1);
                else
                    swap(nums, 0, n-1);
            }
            permutation(ans, n-1, nums);
        }
    }
    private void swap(int[] nums, int a, int b)
    {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }