#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int isprime(int n) {
  if (n == 1) {
    return 0;
  } else if (n == 2 || n == 3) {
    return 1;
  } else if (n % 2 == 0) {
    return 0;
  } else if (n < 9) {
    return 1;
  } else if (n % 3 == 0) {
    return 0;
  } else {
    int r = floor(sqrt(n));
    for (int f = 5; f <= r; f+=6) {
      if (n % f == 0) {
        return 0;
      }
      if (n % (f + 2) == 0) {
        return 0;
      }
    }
    return 1;
  }
}

int n_seq_prime(int q){
    printf("Searching for the prime number %d.\n", q);
	int count = 1;
	for (int i = 1; ;i += 2) {
		if (isprime(i)) {
			count++;
			if (count == q) {
                printf("%d is prime number %d.\n", i, count);
                return count;
            }
		}
	}
}

long sum_seq_prime(int q) {
	long sum = 2;
	for (int i = 1; q >= i ;i += 2) {
		if (isprime(i)) {
            sum += (long)i;
		}
	}
    printf("%ld is the sum of prime numbers below %d.\n", sum, q);
    return sum;
}

int main(int argc, char **argv) {
    printf("INT_MAX value is %d. Using long.\n", INT_MAX);
    int q = atoi(argv[1]);
    int r = n_seq_prime(q);
    long s = sum_seq_prime(q);
    printf("%d is prime with the index %d.\n", r, q);
}
