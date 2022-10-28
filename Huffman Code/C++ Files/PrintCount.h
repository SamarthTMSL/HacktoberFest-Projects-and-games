//
//  PrintCount.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef PrintCount_h
#define PrintCount_h

void PrintDetails(int actualSum, int charNum, int huffSum) {
    cout << "Number of Characters: " << charNum << endl;
    cout << "Total Frequency: " << actualSum << " bits" << endl;
    cout << "Total bits required to print in Characters: " << actualSum*8 << " bits" << endl;
    cout << "Total bits required to print in Huffman Coding: " << huffSum << " bits" << endl;
    cout << endl;
}

#endif /* PrintCount_h */
