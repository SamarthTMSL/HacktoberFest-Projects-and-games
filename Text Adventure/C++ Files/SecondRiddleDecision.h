//
//  SecondRiddleDescision.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef SecondRiddleDescision_h
#define SecondRiddleDescision_h

int secondRiddleDecision(int path){
    if(path == 1) {
        string ans = secondRiddle(1);
        ans = lower(ans);
        while(ans.compare("once") && ans.compare("1") && ans.compare("one")) {
            cout << "Sorry, the answer was wrong... Try Again." << endl;
            cout << "What is the answer? ";
            cin >> ans;
            cout << endl;
        }
    }
    else if(path == 2) {
        string ans = secondRiddle(2);
        ans = lower(ans);
        while(ans.compare("mother") && ans.compare("mom")) {
            cout << "Sorry, the answer was wrong... Try Again." << endl;
            cout << "What is the answer? ";
            cin >> ans;
            cout << endl;
        }
    }
    else if(path == 3) {
        string ans = secondRiddle(3);
        ans = lower(ans);
        while(ans.compare("nine") && ans.compare("9")) {
            cout << "Sorry, the answer was wrong... Try Again." << endl;
            cout << "What is the answer? ";
            cin >> ans;
            cout << endl;
        }
    }
    
    int door;
    cout << "Boulders removed chose any one path..." << endl;
    sleep(2);
    cout << "The correct path will lead you to your own world else..." << endl;
    sleep(2);
    cout << "You steps into the world of death..." << endl;
    sleep(2);
    cout << "Enter the path Number: (1/2/3) ";
    cin >> door;
    cout << endl;
    sleep(3);
    
    if(path == 1) {
        if(door == 1) {
            return 1;
        }
        else if(door == 2) {
            return 2;
        }
        else if(door == 3) {
            return 3;
        }
    }
    else if(path == 2) {
        if(door == 1) {
            return 4;
        }
        else if(door == 2) {
            return 5;
        }
        else if(door == 3) {
            return 6;
        }
    }
    else if(path == 3) {
        if(door == 1) {
            return 7;
        }
        else if(door == 2) {
            return 8;
        }
        else if(door == 3) {
            return 9;
        }
    }
    return -1;
}

#endif /* SecondRiddleDescision_h */
