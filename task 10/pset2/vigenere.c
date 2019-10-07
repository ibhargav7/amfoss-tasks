#include <stdio.h>

int main()
{
	char message[100],ch;
	int i, key;
    int k[3]={0,1,2};
	printf("plaintext:\n");
	scanf("%s", message);


	for(i = 0; message[i] != '\0'; ++i){
	    key=k[i%3];
		ch = message[i];

		if(ch >= 'a' && ch <= 'z'){
			ch = ch + key;

			if(ch > 'z'){
				ch = ch - 'z' + 'a' - 1;
			}

			message[i] = ch;
		}
		else if(ch >= 'A' && ch <= 'Z'){
			ch = ch + key;

			if(ch > 'Z'){
				ch = ch - 'Z' + 'A' - 1;
			}

			message[i] = ch;
		}
	}

	printf("%s\n", message);
}
