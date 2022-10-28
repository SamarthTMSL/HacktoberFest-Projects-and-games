//
//  FormTree.h
//  Huffman Coding
//
//  Created by Arghya Bandyopadhyay on 21/01/22.
//

#ifndef FormTree_h
#define FormTree_h

using namespace std;

class Node {
    public:
        char ch;
        int data;
        Node *left, *right;
    
        Node(char ch, int data) {
            this->ch = ch;
            this->data = data;
            this->left = NULL;
            this->right = NULL;
        }
};

struct cmp {
    bool operator()(Node* L, Node* R) {
        return (L->data > R->data);
    }
};
  

Node* CreateTree(vector<pair<char, int>> A) {
    Node* L, *R, *T;
    
    priority_queue<Node*, vector<Node*>, cmp> Tree;
    for(int i=0; i<A.size(); i++) {
        Tree.push(new Node(A[i].first, A[i].second));
    }
    
    while(Tree.size() != 1) {
        L = Tree.top();
        Tree.pop();
        
        R = Tree.top();
        Tree.pop();
        
        T = new Node('`', L->data + R->data);
        T->left = L;
        T->right = R;
        
        Tree.push(T);
    }
    
    return Tree.top();
}

#endif /* FormTree_h */
