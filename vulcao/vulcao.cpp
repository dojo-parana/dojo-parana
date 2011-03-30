/*
Modulo vulcao com o código a ser testado.
*/

#include <iostream>
using namespace std;

#include <stdlib.h>
#include <math.h>

char mapa[8][8];
int dia = 0;

void vulcao_init(int l, int c, int x1, int y1, int x0, int y0){
  for (int x = 0; x < l; x++){
    for (int y = 0; y < c; y++){
         if (x == x0 && y == y0){
	    mapa[x][y] = '*';
	 }else if(x == 1 && y == 1){
            mapa[x][y] = 'A';	
	 }else{
            mapa[x][y] = '.';
	 } 
    }
  }
}

void vulcao_fumaca()
{
    vulcao_init (8, 8, 5, 4, 0, 0);
    dia++;    
}

