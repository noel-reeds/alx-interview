#include <stdio.h>
#include "prime.h"
/**
 * main - test case for prime numbers.
 *
 *Return: returns a arry of prime numbers.
 */
int main() {
	int m = 30;
	printf("prime numbers smaller than or equal to %d\n", m);
	sieve_of_eratosthenes(m);
	return 0;
}
