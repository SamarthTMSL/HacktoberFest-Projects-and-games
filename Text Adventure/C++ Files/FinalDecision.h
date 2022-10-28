//
//  FinalDecision.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef FinalDecision_h
#define FinalDecision_h

void finalDecision(int door, string name) {
    if(door == 1 || door == 3 || door == 5 || door == 6 || door == 8) {
        cout << "Hey, Hey there... Welcome back to your own world " << name << "." << endl;
        sleep(2);
        cout << "You have escaped from the time loop set by Grafflet..." << endl;
        sleep(2);
        cout << "You Won..." << endl;
    }
    else if(door == 2 || door == 4 || door == 7 || door == 9) {
        cout << "Haa.. haa.. haa.." << endl;
        sleep(2);
        cout << name << ", you have chosen the wrong path." << endl;
        sleep(2);
        cout << "You are now trapped into the World of Death..." << endl;
        sleep(2);
        cout << "You Lose..." << endl;
    }
}

#endif /* FinalDecision_h */
