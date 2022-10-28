//
//  SortingFrequencies.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 21/01/22.
//

#ifndef SortingFrequencies_h
#define SortingFrequencies_h

using namespace std;

bool cmp(pair<char, int>& a, pair<char, int>& b) {
    return (a.second < b.second);
}

vector<pair<char, int>> Sort(map<char, int> count) {
    vector<pair<char, int>> A;
    
    for(auto& it:count)
        A.push_back(it);
    
    sort(A.begin(), A.end(), cmp);
    return A;
}

#endif /* SortingFrequencies_h */
