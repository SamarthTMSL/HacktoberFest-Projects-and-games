//
//  main.cpp
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#include <iostream>
#include <utility>
#include <unistd.h>
#include "Start.h"
#include "FirstRiddle.h"
#include "SecondRiddle.h"
#include "Introduction.h"
#include "FinalDecision.h"
#include "ConvertStrings.h"
#include "FirstRiddleDecision.h"
#include "SecondRiddleDecision.h"
using namespace std;

int main(int argc, const char * argv[]) {
    if(introduction()) {
        string name;
        char gender;
        pair<string, char> my_pair = start();
        name = my_pair.first;
        gender = my_pair.second;
        name = nameConversion(name);
        
        int firstAns = firstRiddleDecision();
        int secondAns = secondRiddleDecision(firstAns);
        finalDecision(secondAns, name);
    }
    return 0;
}
