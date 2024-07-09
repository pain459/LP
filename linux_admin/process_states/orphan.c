#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
        // Child process
        sleep(2); // Ensure the parent terminates first
        printf("Child process (PID: %d) has been orphaned, new parent PID: %d\n", getpid(), getppid());
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        printf("Parent process (PID: %d) is exiting\n", getpid());
        exit(EXIT_SUCCESS);
    }
}
