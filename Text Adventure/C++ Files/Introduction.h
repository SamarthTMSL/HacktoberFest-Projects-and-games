//
//  Introduction.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef Introduction_h
#define Introduction_h

using namespace std;

int introduction(void){
    char start;

    cout << "Wha... What happened? Where am I?" << endl;
    sleep(2);
    cout << "It's too dark to see anything..." << endl;
    cout << endl;
    sleep(2);
    cout << "You are trapped into a time loop by Grafflet - A Troublemaker in Arthurian Legend..." << endl;
    sleep(2);
    cout << "Would you like to start the game? (Y/N) ";

    cin >> start;
    cout << endl;
    
    if(start == 'Y' || start == 'y') {
        return 1;
    }
    else {
        return 0;
    }
}

#endif /* Introduction_h */
