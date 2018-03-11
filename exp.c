#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(int argc, char *argv[])
{
	printf("hello world\n");
	char *command, *buffer;
	command=(char *)malloc(100);
	strcpy(command, "this is command");
	printf("the content of command is %d \n", *command);
	free(command);

}
