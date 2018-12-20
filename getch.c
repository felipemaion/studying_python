#include <stdio.h>
#include <curses.h>
#include <term.h>
#define MAXCHAR 8

#define CONTROL(x)  ((x) & 0x1F)

int main(void)
{
    // FILE *fp = fopen("x", "w");
    // if (fp == 0)
    //     return(-1);
    SCREEN *s = newterm(NULL, stdin, stdout);
    if (s == 0)
        return(-1);
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    int i;
    char input;
    char string[MAXCHAR + 1];
    addstr( "What is your name> " );
    refresh();
      for(i = 0; i <= MAXCHAR; i++){
        
        
        input = getch();
        refresh();
        

        // printf("%c\n", input);
        if(i == MAXCHAR){
            break;
        }
        else{
            string[i] = input;
        }
    }
    printf("%s\n", string);
    endwin();

    return 0;
}