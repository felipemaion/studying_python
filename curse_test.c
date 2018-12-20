
#include <ncurses.h>
#define MAXCHAR 8
int main()
{	
	initscr();			/* Start curses mode 		  */
    int i;
    char input;
    char string[MAXCHAR + 1];
    addstr( "Digite a string > " );
    refresh();
      for(i = 0; i <= MAXCHAR; i++){
        input = getch();
        // refresh();
        if(i == MAXCHAR){
            break;
        }
        else{
            string[i] = input;
        }
    }
    printw("\n%s\n", string);
    refresh();
    printw("Pressione qualquer tecla para sair");
    refresh();
	getch();			/* Wait for user input */
	endwin();			/* End curses mode		  */
	return 0;
}