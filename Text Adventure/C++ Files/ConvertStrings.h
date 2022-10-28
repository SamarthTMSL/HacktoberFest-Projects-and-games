//
//  ConvertToLower.h
//  Text Adventure
//
//  Created by Arghya Bandyopadhyay on 19/01/22.
//

#ifndef ConvertToLower_h
#define ConvertToLower_h

string lower(string str) {
    for(int i=0; i<str.length(); i++) {
        str[i] = tolower(str[i]);
    }
    return str;
}

string nameConversion(string str) {
    for(int i=0; i<str.length(); i++) {
        if(i == 0)
            str[i] = toupper(str[i]);
        else
            str[i] = tolower(str[i]);
    }
    return str;
}

#endif /* ConvertToLower_h */
