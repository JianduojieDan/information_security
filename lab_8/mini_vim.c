#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>
#include <ctype.h>

struct termios orig_termios;

void disableRawMode() {
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios);
}

void enableRawMode() {
    tcgetattr(STDIN_FILENO, &orig_termios);
    atexit(disableRawMode);

    struct termios raw = orig_termios;
    raw.c_lflag &= ~(ECHO | ICANON | ISIG | IEXTEN);
    raw.c_iflag &= ~(IXON | ICRNL);

    tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
}

int main() {
    enableRawMode();

    printf("Mini-Vim (Raw Mode) | Ctrl+Q to quit\r\n");

    char c;
    while (read(STDIN_FILENO, &c, 1) == 1 && c != 17) {
        if (c == 13) {
            printf("\r\n");
        } else if (iscntrl(c)) {
            printf("[%d]", c);
            if (c == 10 || c == 13) printf("\r\n");
        } else {
            printf("%c", c);
            fflush(stdout);
        }
    }

    return 0;
}
