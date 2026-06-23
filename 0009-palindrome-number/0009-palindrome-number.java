class Solution {
    public boolean isPalindrome(int x) {
        int org=x;
        int rev=0;
        boolean isPal;
         if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        while(x>rev){
            int digit=x%10;
            rev=rev*10+digit;
            x/=10;
        }
        // if( rev==org){
        //    isPal=true;
        // }
        // else
        // {
        //     isPal=false;
           
        // }
        // return isPal;
        return (x == rev || x == rev / 10);
    }
    public static void main(String args[]){
        Solution s1=new Solution();
        int n=121;
        s1.isPalindrome(n);
    }
}