#include <p18f2431.h>
	
#define TEMPS_BLOQUEJAT 10000
	
	
def baixar_porta():
	pass
	
def pujar_porta():
	pass
	
def tirar_enrere():
	pass
	
def mini_tirar_enrere():
	pass
	
def premsar_briketa():
	pass
	
def empenyer_briketa():
	pass
	
def empenyer_3_briketes():
	pass
	
def tirar_virutes():
	pass
	
def mas_madera():
	pass
	
def main():
	pass
	

	
	
	
void baixar_porta(){
	if (PORTBbits.RB1 == 1) PORTAbits.RA2 = 1; // engegar baixar porta
	while ( PORTBbits.RB1 == 1); // esperar sensor de porta tancada
	PORTAbits.RA2 = 0; // parar motor baixar porta
}

void pujar_porta(){
    if (PORTBbits.RB2 == 1) PORTAbits.RA1 = 1; // obrir porta
	while (PORTBbits.RB2 == 1); // esperar sensor porta oberta
	PORTAbits.RA1 = 0; // parar obrir porta
}

void tirar_enrera (){
    
    if (PORTBbits.RB0 ==1) PORTAbits.RA3 = 1; // engegar motor treure pressio/compressio
    while (PORTBbits.RB0 == 1); // esperar final pressio/compressio
	PORTAbits.RA3 = 0; // parar motor treure pressio/compressio 
}

void mini_tirar_enrera(){
	PORTAbits.RA3 = 1; // tirar enrera pressio/compressio
	delay_1ms(); //while (PORTBbits.RB3 == 0); // esperar que pressio/descompressio baixi
	PORTAbits.RA3 = 0; // parar motor treure pressio/compressio
}	

void premsar_briketa(){
	PORTAbits.RA0 = 1; // engegar pressio/compressio
	while ( PORTBbits.RB3 == 1);
	delay_2ms();
	delay_2ms();
	PORTAbits.RA0 = 0; // parar pressio/compressio
}	

void espenyer_briketa(){
	PORTAbits.RA0 = 1; // engegar pressio/compressio per espenyer briketa
	while ( PORTBbits.RB3 == 1); // espera pressio maxima sensor 1/2/3 -- briketa expulsada
	PORTAbits.RA0 = 0; // para pressio/compressio
}

void espenyer_3briketes(){
	PORTAbits.RA0 = 1; // engegar pressio/compressio per espenyer briketa
	while ( PORTBbits.RB3 == 1); // espera pressio maxima sensor 1/2/3 -- briketa expulsada
	delay_2ms();
	PORTAbits.RA0 = 0; // para pressio/compressio	
}	

void tirar_virutes(){
	unsigned int cnt;
	unsigned int temps_remenador;
		
	temps_remenador = calcul_t_remenador();
		
	PORTAbits.RA4 = 1;
	for (cnt=0; cnt<=temps_remenador; cnt++) delay_10us();
   	PORTAbits.RA4 = 0;
}

void mas_madera(){
	tirar_enrera();
	delay_50us();

	tirar_virutes();

	premsar_briketa();
	delay_50us();
}

void main (void)
{
	  
	unsigned int cnt;
	unsigned int temps_remenador = 0;
	unsigned int cnt_remenador = 0;
	unsigned int estat = 0;
	unsigned int error_bloqueig = 0;
	unsigned int temps_bloqueig = 0;
	unsigned int cnt_briquetes = 0;  	
	unsigned int i = 0;

	unsigned int pos_switch_temps;
	unsigned int pos_switch_numero;

	TRISB = 0XFF;	
	TRISA = 0; // defineix si es bit del port es input(1) o output(0)
	ANSEL0 = 0; // per fer servir el portA com entrades/sortides digitals, no com entrades dels ADCs
	LATA = 0xFF; // Important posar-ho a 1 si el port es de sortida, sino no activa els outputs
	PORTA = 0; 
	TRISC = 0xfF; // defineix si es bit del port es input(1) o output(0)

	// inicialitzem posicio
	tirar_enrera();
	delay_1ms();
	baixar_porta();
	delay_1ms();

	/*	
	while (1) {
		estat = def_estat();
		if (estat == 0) pujar_porta();	
		if (estat == 1) baixar_porta();
		if (estat == 2) tirar_enrera();
		if (estat == 3) espenyer_briketa();

		delay_1ms();

	}*/

	// loop produccio briquetes
	while (1) {
    	estat = def_estat();

		pos_switch_temps = calc_pos_switch_temps();
		pos_switch_numero = calc_pos_switch_numero();

		cnt_briquetes = 0;

		if (estat == 0) {

			tirar_enrera();
		 	delay_1ms();
			pujar_porta();
		 	delay_1ms();

		} else {

			baixar_porta();
			delay_50us();

			// netejem cada 10 briquetes
			if (cnt_briquetes == 10) {
				cnt_briquetes = 0;
			} else {
				tirar_virutes();
				cnt_briquetes++;	
			}

			premsar_briketa();
			delay_1ms();
		
			if (estat == 2) mas_madera();
			if (estat == 3) {
				mas_madera();
				mas_madera();
			}

			mini_tirar_enrera();
			delay_1ms();

			pujar_porta();
			delay_50us();
	
			if (estat == 3) espenyer_3briketes();
			else 			espenyer_briketa();
			delay_1ms();

			baixar_porta();		
			delay_50us();
		
			tirar_enrera();
			delay_50us();

		}

		delay_50us();
	}
	
}

	
