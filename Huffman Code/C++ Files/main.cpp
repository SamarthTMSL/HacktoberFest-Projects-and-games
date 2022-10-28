//
//  main.cpp
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 21/01/22.
//

#include <iostream>
#include <fstream>
#include <utility>
#include <string>
#include <queue>
#include <map>
#include "FormTree.h"
#include "ReadTree.h"
#include "Decoding.h"
#include "PrintCount.h"
#include "ReplaceFile.h"
#include "CountFrequencies.h"
#include "SortingFrequencies.h"
#include "PrerequirementsForDecoding.h"
using namespace std;

int main(int argc, const char * argv[]) {
    cout << "Huffman Encoding:" << endl;
    
    string filePath = "/Users/arghyabandyopadhyay/Desktop/Huffman Coding/Huffman Coding/File.txt";
    
    map<char, int> count = Count(filePath);
    vector<pair<char, int>> A = Sort(count);
    Node *root = CreateTree(A);
    PrintCodes(root, "");
    Replace(filePath, code);
    PrintDetails(actualSum, charNum, huffSum);
    
    cout << "Huffman Decoding:" << endl;
    
    string outFilePath = "/Users/arghyabandyopadhyay/Desktop/Huffman Coding/Huffman Coding/HuffmanFile.txt";
    
    map<string, char> recode = Replace(code);
    string actual = Decode(outFilePath, recode);
    cout << actual << endl;
    cout << endl;
    return 0;
}
