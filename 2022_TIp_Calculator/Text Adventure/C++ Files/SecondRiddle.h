//
//  SecondRiddle.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef SecondRiddle_h
#define SecondRiddle_h

using namespace std;

string secondRiddle(int path){
    cout << endl;
    if(path == 1)
        cout << "You stepped into the first path..." << endl;
    else if(path == 2)
        cout << "You stepped into the second path..." << endl;
    else if(path == 3)
        cout << "You stepped into the third path..." << endl;
    sleep(2);
    cout << "New three paths are revealed and the entrances are blocked with boulders..." << endl;
    sleep(2);
    cout << "You need to crack the second riddle to unlock the paths." << endl;
    sleep(2);
    cout << "The riddle appears..." << endl;
    sleep(3);
    
    cout << endl;
    if(path == 1) {
        cout << "How  many times can you subtract 10 from 100?" << endl;
        sleep(2);
        cout << endl;
        cout << "What is the answer? ";
    }
    else if(path == 2) {
        cout << "A boy and a doctor are fishing." << endl;
        sleep(2);
        cout << "The boy is the doctor's son; the doctor isn't the boy's father." << endl;
        sleep(2);
        cout << endl;
        cout << "Who is the doctor? ";
    }
    else if(path == 3) {
        cout << "Mr. and Mrs. Anderson have 6 boys." << endl;
        sleep(2);
        cout << "Each boy has one sister." << endl;
        sleep(2);
        cout << endl;
        cout << "Can you count how many people there are in the family? ";
    }
    
    string ans;
    cin >> ans;
    cout << endl;
    
    return ans;
}

#endif /* SecondRiddle_h */
