//
//  ReadTree.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 22/01/22.
//

#ifndef ReadTree_h
#define ReadTree_h

using namespace std;

int actualSum = 0, charNum = 0, huffSum = 0;
map<char, string> code;

int isLeaf(Node* root) {
    return !(root->left) && !(root->right);
}

void PrintCodes(Node* root, string str) {
    if (root->left) {
        PrintCodes(root->left, str+"0");
    }

    if (root->right) {
        PrintCodes(root->right, str+"1");
    }
    
    if (isLeaf(root)) {
  
        cout<< root->ch << " : " << root->data << " = " << str << endl;
        
        code[root->ch] = str;
        
        huffSum += root->data*str.length();
        actualSum += root->data;
        charNum++;
    }
}

#endif /* ReadTree_h */
