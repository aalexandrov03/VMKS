/*
 * serleddvrsrc.c
 *
 * Created: 4/13/2021 8:02:12 PM
 * Author: Alexander Alexandrov
 */ 

#include "serleddvrinc.h"

void _initSerialLED(void){
	DDRC |= _BV(1);
	PORTC &= ~_BV(1);
}

int _checkSerialConnected(void) {
	if (bit_is_set(PINC, 0))
		return 1;
	else
		return 0;
}

void _serialReady(void){
	PORTC &= ~_BV(1);
}

void _serialBusy(void){
	PORTC |= _BV(1);
}

