//
//  Start.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef Start_h
#define Start_h

using namespace std;

pair<string, char> start(void){
    string name;
    char gender;
    
    cout << "Everything is Dark. The ground is cold, damp, and covered in thick vines." << endl;
    sleep(2);
    cout << "You feel a rock that sinks in the ground and on pressing it, the ground starts rumbling." << endl;
    sleep(2);
    cout << "Lights begin flooding in..." << endl;
    sleep(2);
    cout << endl;
    
    cout << "Enter your Name: ";
    cin >> name;
    sleep(2);
    cout << "Enter your Gender: (F/M/O) ";
    cin >> gender;
    sleep(3);
    cout << endl;
    
    pair<string, char> my_pair;
    my_pair.first = name;
    my_pair.second = gender;
    return my_pair;
}

#endif /* Start_h */
