//
//  FirstRiddleDecision.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef FirstRiddleDecision_h
#define FirstRiddleDecision_h

int firstRiddleDecision() {
    int ans = firstRiddle();
    while(ans != 4100) {
        cout << "Sorry, the answer was wrong... Try Again." << endl;
        cout << "What is the answer? ";
        cin >> ans;
        cout << endl;
    }
    int door;
    cout << "Boulders removed chose any one path..." << endl;
    sleep(2);
    cout << "Enter the path Number: (1/2/3) ";
    cin >> door;
    
    return door;
}

#endif /* FirstRiddleDecision_h */
