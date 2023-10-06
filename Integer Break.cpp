#include <cmath>
class Solution {
public:
    int integerBreak(int n) {
        if (n<=3){
            n= n-1;
        }
        else{
            int n1 = n/3;
            if(n%3 == 0){
                n = pow(3,n1);
            }
            else if(n%3 == 1){
                n = pow(3,n1-1)*pow(2,2);
            }
            else if(n%3 == 2){
                n = pow(3,n1)*2;
            }
    }
    return n;
    }
};