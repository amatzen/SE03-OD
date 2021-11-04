#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void print_number( void *ptr );
int counter;

// Declare lock
pthread_mutex_t lock;

int main()
{
	pthread_t thread1, thread2;
	int ret;

	// Initialize lock
	pthread_mutex_init(&lock, NULL);

	// Create cpuset for thread A, lock to core0
        cpu_set_t cpusetA;
	CPU_ZERO(&cpusetA);
        CPU_SET(0, &cpusetA);

	// Create cpuset for thread B, lock to core1
        cpu_set_t cpusetB;
	CPU_ZERO(&cpusetB);
        CPU_SET(1, &cpusetB);

	// Create and start thread A, pass identifier to thread
        char * iden = "A";
	pthread_create( &thread1, NULL, (void*)print_number, iden);

	// Lock thread to core 0
	ret = pthread_setaffinity_np(thread1, sizeof(cpu_set_t), &cpusetA);

	// Create and start thread B, pass identifier to thread
        iden = "B";
	pthread_create( &thread2, NULL, (void*)print_number, iden);

	// Lock thread to core 1
	ret = pthread_setaffinity_np(thread2, sizeof(cpu_set_t), &cpusetB);

	// Wait for threads to exit
	pthread_join( thread1, NULL);
	pthread_join( thread2, NULL); 

	return 0;
}

void print_number( void *ptr )
{
	int i;
	counter = 0;

	char * identifier = (char*)ptr; 
	for( i = 0 ; i < 500 ; i++ ) 
	{
		pthread_mutex_lock(&lock);
		counter++;
		printf("%s%d \n", identifier, counter);
		pthread_mutex_unlock(&lock);
	}
}

