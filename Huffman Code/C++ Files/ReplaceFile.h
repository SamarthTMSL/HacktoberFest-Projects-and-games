//
//  Header.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef Header_h
#define Header_h

using namespace std;

void Replace(string filePath, map<char, string> code) {
    string outFilePath = "/Users/arghyabandyopadhyay/Desktop/Huffman Coding/Huffman Coding/HuffmanFile.txt";
    
    ifstream myFile(filePath);
    ofstream outFile;
    outFile.open(outFilePath);
    
    if(!myFile.is_open()) {
        cout << "Sorry!!! Could not open the file." << endl;
    }
    cout << endl;
    char byte = 0;
    while(myFile.get(byte)) {
        outFile << code[byte];
    }
    
    outFile.close();
    myFile.close();
}

#endif /* Header_h */
