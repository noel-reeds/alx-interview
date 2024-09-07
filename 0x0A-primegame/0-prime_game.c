#include <stdio.h>
#include <stdbool.h>
#include <string.h>
/**
 * sieve_of_eratosthenes - finds prime numbers.
 *
 *@n: number of elements in boolean array.
 *
 * Return: Always void
 */
void sieve_of_eratosthenes(int num) {
	/* create a boolean array and intialize it to true */
	int m, n;
	bool prime[n + 1];

	memset(prime, true, sizeof(prime));
	for (m = 2; m * m <= num; m++)
	{
		/* mark multiples of m, greater than or equal to 
		 * square of m since the previous ones are already
		 * handled. step size of n += m ensures increment from 
		 * m*m to the next multiple.
		 */
		for (n = m * m; n <= num; n += m)
		{
			prime[n] = false;
		}
	}
	/* output all prime. */
	for (m = 2; m <= num; m++)
	{
		if (prime[m])
			printf("%d, ", m);
	}
}
