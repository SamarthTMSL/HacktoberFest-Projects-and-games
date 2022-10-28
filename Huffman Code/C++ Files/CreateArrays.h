//
//  Header.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef Header_h
#define Header_h

using namespace std;

pair<vector<char>, vector<int>> createArray(vector<pair<char, int>> A) {
    vector<char> letter;
    vector<int> frequency;
    
    for(auto it:A) {
        letter.push_back(it.first);
        frequency.push_back(it.second);
    }
    return make_pair(letter, frequency);
}

#endif /* Header_h */
