//
//  Decoding.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef Decoding_h
#define Decoding_h

using namespace std;

string Decode(string outfilePath, map<string, char> recode) {
    ifstream outFile(outfilePath);
    if(!outFile.is_open()) {
        cout << "Sorry!!! Could not open the file." << endl;
    }
    
    char byte = 0;
    string temp = "", actual = "";
    while(outFile.get(byte)) {
        temp.push_back(byte);
        if(recode[temp] != NULL) {
            actual += recode[temp];
            temp = "";
        }
    }
    outFile.close();
    return actual;
}

#endif /* Decoding_h */
