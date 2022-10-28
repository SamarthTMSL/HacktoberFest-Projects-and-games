//
//  PrerequirementsForDecoding.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef PrerequirementsForDecoding_h
#define PrerequirementsForDecoding_h

using namespace std;

map<string, char> Replace(map<char, string> code) {
    map<string, char> recode;
    map<char, string>::iterator itr;
    
    for (itr = code.begin(); itr != code.end(); ++itr) {
        char ch = itr->first;
        string str = itr->second;
        recode[str] = ch;
    }
    return recode;
}

#endif /* PrerequirementsForDecoding_h */
