class Solution {
    public int reverse(int x) {
        int rev=0;
        while(x!=0){
            int digit=x%10;
            
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && digit > 7) || rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && digit < -8)) {
                return 0;
            }
            // if () {
            //     return 0;
            // }
             rev=rev*10+digit;
            x/=10;
        }
        return rev;
    }
    public static void main(String args[]){
        Solution s1=new Solution();
        int n=111;
        int reverse=s1.reverse(n);
        System.out.println(reverse);
    }
}