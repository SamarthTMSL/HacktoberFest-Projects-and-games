//
//  CountFrequencies.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 21/01/22.
//

#ifndef CountFrequencies_h
#define CountFrequencies_h

using namespace std;

map<char, int> Count(string filePath) {
    map<char, int> count;
    
    ifstream myFile(filePath);
    if(!myFile.is_open()) {
        cout << "Sorry!!! Could not open the file." << endl;
    }
    
    char byte = 0;
    while(myFile.get(byte)) {
        count[byte] += 1;
    }
    myFile.close();
    return count;
}

#endif /* CountFrequencies_h */
