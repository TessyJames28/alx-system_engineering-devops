#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>


/**
 * infinite_while - function that loops inifitely
 *
 * Return: success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry point
 *
 * Return: EXIT_SUCCESS
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(0);
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
