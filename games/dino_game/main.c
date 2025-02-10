#include <conio.h>
#include <stdio.h>
#include <windows.h>
#include <time.h>

// Function to set the console cursor position
void moveTo(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void pause(unsigned int milliseconds) {
    clock_t goal = milliseconds + clock();
    while (goal > clock());
}

// Function to display the dinosaur at a certain height
void displayDino(int jumpHeight) {
    moveTo(2, 15 - jumpHeight);
    printf("               __ ");
    moveTo(2, 16 - jumpHeight);
    printf("              / _) ");
    moveTo(2, 17 - jumpHeight);
    printf("     _.----._/ /  ");
    moveTo(2, 18 - jumpHeight);
    printf("    /         /   ");
    moveTo(2, 19 - jumpHeight);
    printf(" __/ (  | (  |    ");
    moveTo(2, 20 - jumpHeight);
    printf("/__.-'|_|--|_|    ");
}

void eraseDinoUp(int jumpHeight) {
    moveTo(2, 15 - jumpHeight);
    printf("                  ");
    moveTo(2, 16 - jumpHeight);
    printf("                  ");
    moveTo(2, 17 - jumpHeight);
    printf("                  ");
    moveTo(2, 18 - jumpHeight);
    printf("                  ");
    moveTo(2, 19 - jumpHeight);
    printf("                  ");
    moveTo(2, 20 - jumpHeight);
    printf("                  ");
    moveTo(2, 21 - jumpHeight);
    printf("                  ");
}

void eraseDinoDown(int jumpHeight) {
    moveTo(2, 15 - jumpHeight);
    printf("                  ");
    moveTo(2, 16 - jumpHeight);
    printf("                  ");
    moveTo(2, 17 - jumpHeight);
    printf("                  ");
    moveTo(2, 18 - jumpHeight);
    printf("                  ");
    moveTo(2, 19 - jumpHeight);
    printf("                  ");
    moveTo(2, 20 - jumpHeight);
    printf("                  ");
}

// Function to display the floor (ground level)
void displayFloor() {
    moveTo(0, 21);
    for (int i = 0; i < 82; i++) {
        printf("_");
    }
}

// Function to display and erase the obstacle
void displayObstacle(int obstaclePos) {
    // Erase the obstacle at its current position
    moveTo(obstaclePos, 20);
    printf("O");  // Display the obstacle as "O"
    // Clear the previous obstacle position
    if (obstaclePos < 72) {
        moveTo(obstaclePos + 1, 20);
        printf(" ");
    }
}

// Function to update the obstacle position
int updateObstacle(int obstaclePos, int *score) {
    if (obstaclePos <= 0) {
        obstaclePos = 0;
        moveTo(obstaclePos, 20);
        printf(" "); // Deletes the previous obstacle
        // Obstacle out of view; increment score and reset obstacle
        obstaclePos = 80;
        (*score)++;
    } else {
        obstaclePos--;  // Move the obstacle left
    }
    return obstaclePos;
}

// Function to check for collision
int checkCollision(int obstaclePos, int jumpHeight, int score) {
    if (obstaclePos == 14 && jumpHeight == 0) {
        system("cls");
        moveTo(35, 10);
        printf("Game Over! Your score is: %d\n", score);
        printf("Press any key to exit...\n");
        getch();
        return 1;  // Return 1 to indicate game over
    }
    return 0;  // Return 0 if no collision
}

// Function to display game instructions
void displayInstructions(int score) {
    moveTo(10, 2);
    printf("Press X to Exit, Press Space to Jump");
    moveTo(62, 2);
    printf("SCORE : ");
    moveTo(70, 2);
    printf("%d", score);
}

// Function to control the speed of the game
void controlSpeed(int score) {
    if (score <= 1) {
        pause(40);
    } else if (score <= 3) {
        pause(35);
    } else if (score <= 5) {
        pause(30);
    } else if (score <= 7) {
        pause(25);
    } else if (score <= 9) {
        pause(20);
    } else {
        pause(10);
    }
}

// Jump handling function for non-blocking jump
void handleJump(int *jumpHeight, int *isJumping, int *isFalling) {
    if (*isJumping && !*isFalling) {
        (*jumpHeight)++;
        eraseDinoUp(*jumpHeight);
        if (*jumpHeight >= 5) {  // Peak height reached
            *isFalling = 1;
        }
    } else if (*isFalling) {
        eraseDinoDown(*jumpHeight);
        (*jumpHeight)--;
        if (*jumpHeight <= 0) {
            *isJumping = 0;
            *isFalling = 0;
            *jumpHeight = 0;
        }
    }
}

// Main function
int main() {
    system("mode con: lines=29 cols=82");  // Set the console window size
    int jumpHeight = 0;       // Current jump height
    int score = 0;            // Starting score
    int obstaclePos = 80;     // Starting position of the obstacle
    int isJumping = 0;        // Jump state: 0 = not jumping, 1 = jumping
    int isFalling = 0;        // Fall state: 0 = not falling, 1 = falling
    char input;

    // Display game instructions and score
    displayInstructions(score);

    while (1) {
        // Main game loop for obstacle and floor updates
        while (!isJumping) {
            displayDino(jumpHeight);
            displayFloor();
            displayObstacle(obstaclePos);
            displayInstructions(score);  // Update score display

            // Check for collision
            if (checkCollision(obstaclePos, jumpHeight, score)) {
                return 0;  // End the game if collision occurs
            }

            // Update the obstacle position
            obstaclePos = updateObstacle(obstaclePos, &score);

            // Handle input (jumping and exit)
            if (kbhit()) {
                input = getch();
                if (input == ' ' && !isJumping) {
                    isJumping = 1;  // Start the jump if space is pressed
                }
                if (input == 'x') {
                    return 0;  // Exit the game if 'X' is pressed
                }
            }

            // Control the speed of the game
            controlSpeed(score);
        }

        // Jump loop for handling jump mechanics separately
        while (isJumping) {
            handleJump(&jumpHeight, &isJumping, &isFalling);

            displayDino(jumpHeight);
            displayFloor();
            displayObstacle(obstaclePos);
            displayInstructions(score);  // Update score display

            // Check for collision during jump
            if (checkCollision(obstaclePos, jumpHeight, score)) {
                return 0;  // End the game if collision occurs
            }

            // Update the obstacle position during jump
            obstaclePos = updateObstacle(obstaclePos, &score);

            // Control speed during jump phase
            controlSpeed(score);
        }
    }

    return 0;
}