// Helper functions for music
#include "helpers.h"
#include <stdio.h>
#include <math.h>

#include <string.h>
// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
   int x= fraction[2]-'0';
   int y = 8/x;
   int z = fraction[0]-'0';
   return(z*y);
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    int n;
    int m;
    int l;
    float f;
    char note1 = note[0];
    char note2 = note[1];
    l= note[strlen(note)-1]-'0';

    if (note[0]=='A'){
        n=0;
    }
    else if (note[0]=='B'){
        n=2;
    }
    else if (note[0]=='C'){
        n=9;
    }
    else if (note[0]=='D'){
        n=7;
    }
    else if (note[0]=='E'){
        n=5;
    }
    else if (note[0]=='F'){
        n=4;
    }
    else if (note[0]=='G'){
        n=2;
    }
    if (note[1]=='#'){
        n=n+1;
    }
    else if(note[1]=='b'){
        n=n-1;
    }
    f = 440.0*(pow(2.0,n/12.0));
    m=l-4;
    if (l > 4)
    {
        f *= pow(2.0, l - 4);
    }
    else if (l < 4)
    {
        f /= pow(2.0, 4 - l);
    }
    return round(f);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    return strlen(s) == 0;
}
