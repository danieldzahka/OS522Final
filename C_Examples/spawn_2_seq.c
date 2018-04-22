/**
 * Spawn_2_seq.c : A program to run two cpu bound functions
 * sequentially
 *
 * Daniel Zahka ~ daniel.zahka@wustl.edu
 * Anish Naik ~ anish,r.naik@wustl.edu
 *
 */

#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>

#define ITERATIONS (1000000000)

void * thread_func(void * args){
    long long i, k;
    for (i = 0; i < ITERATIONS; ++i){
        k = i * 3;
    }
    return 0;
}


int main(){
    printf("Spawning Threads\n");
    thread_func(0);
	thread_func(0);
	printf("Joined Threads\n");
 
    return 0;
}
