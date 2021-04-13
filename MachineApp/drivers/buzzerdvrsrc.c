/*
 * buzzerdvrsrc.c
 *
 * Created: 4/13/2021 5:22:10 PM
 * Author: Alexander Alexandrov
 */ 

#include "buzzerdvrinc.h"

void _initBuzzer(void) {
	DDRB |= _BV(5);
	PORTB &= ~_BV(5); 
}

void _toggleBuzzer(void) {
	if (buzzer_state == 0){
		PORTB |= _BV(5);
		buzzer_state = 1;
	}
	else{
		PORTB &= ~_BV(5);
		buzzer_state = 0;
	}
}