/*A number is automorphic when the square of the number has the last digit like the number.. 
for 5 its 25 and it has last digit as 5 .. 
and.. 25 .. when squared gives 625 and it has 25 as its last digits.. so its also an sutomorphic number. @voiDXDOps*/
#include <stdio.h>

void main()
{
    int n,s,i=1,m;
    printf("Enter the number: ");
    scanf("%d", &n);
    s=n*n; m=s;
    while(s!=0)
    {
        i=i*10;
        s=s/10;
    }
    i=i/10;
    if(n==(m%i))
    {
        printf("Congo!! Its an Automorphic No.");
    }
    else
    {
        printf("Not Automorphic No.");
    }  
}
