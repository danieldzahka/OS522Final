/**
 * Spawn_2.c : A program to spawn two cpu bound threads 
 * Daniel Zahka ~ daniel.zahka@wustl.edu
 * Anish Naik ~ anish,r.naik@wustl.edu
 *
 */

#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>

#define ITERATIONS (10000000000)

void * thread_func(void * args){
    long long i, k;
    for (i = 0; i < ITERATIONS; ++i){
        k = i * 3;
    }
    return 0;
}


int main(){
    /*Check return values maybe...*/
    pthread_t tid1, tid2;
    printf("Spawning Threads\n");
    pthread_create(&tid1, 0, thread_func, 0); 
    pthread_create(&tid2, 0, thread_func, 0);
    pthread_join(tid1, 0);
    pthread_join(tid2, 0); 
    printf("Joined Threads\n");
 
    return 0;
}
