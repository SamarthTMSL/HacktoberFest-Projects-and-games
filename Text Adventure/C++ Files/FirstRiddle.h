//
//  FirstRiddle.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef FirstRiddle_h
#define FirstRiddle_h

using namespace std;

int firstRiddle(void){
    cout << "You enter in a cave..." << endl;
    sleep(2);
    cout << "Three paths are revealed and the entrances are blocked with boulders..." << endl;
    sleep(2);
    cout << "The key to access the paths, is to crack the riddle." << endl;
    sleep(2);
    cout << "The riddle appears..." << endl;
    sleep(3);
    
    cout << endl;
    cout << "Add 1000 to 40." << endl;
    sleep(2);
    cout << "Now add 1000." << endl;
    sleep(2);
    cout << "Now add 30." << endl;
    sleep(2);
    cout << "Add 1000 again." << endl;
    sleep(2);
    cout << "Now add 20." << endl;
    sleep(2);
    cout << "Add 1000 again." << endl;
    sleep(2);
    cout << "Now add 10." << endl;
    sleep(2);
    cout << endl;
    
    int ans;
    cout << "What is the answer? ";
    cin >> ans;
    cout << endl;
    
    return ans;
}


#endif /* FirstRiddle_h */
