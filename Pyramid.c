
#include <bits/stdc++.h>

using namespace std;

class Solution {
  public:
int i,j;
    void printTriangle(int n) {
      
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n+(i-1);j++){
                if(j>=n-(i-1)&&j<=n+(i-1))
                cout << "*";      // printing '*' 
                else
                cout <<" ";      // printing "spaces/__" 
                
            }cout << "\n";      // going to next line
        }
    }
};


// main function start here
int main() {
    int t;
    cin >> t; // taking no. of test cases
    while (t--) {
        int n;
        cin >> n;  //taking value of rows

        Solution ob;
        ob.printTriangle(n);
    }
    return 0;
}
//  main function end here
