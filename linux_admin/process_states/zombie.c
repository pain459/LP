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
        printf("Child process (PID: %d) is exiting\n", getpid());
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        printf("Parent process (PID: %d) sleeping\n", getpid());
        sleep(10); // Child will be a zombie during this time
        printf("Parent process (PID: %d) waking up\n", getpid());
        wait(NULL); // Collect child process exit status
        printf("Zombie child process has been reaped\n");
    }
    return 0;
}
