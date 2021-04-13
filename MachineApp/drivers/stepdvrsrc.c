/*
 * stepdvrsrc.c
 *
 * Source file for step motor driver code.
 *
 * Created: 3/17/2021
 *
 *  Author: Alexander Alexandrov
 */ 

#include "stepdvrinc.h"

void _initDriver(struct stepdvr_t* driver, unsigned int ppr, unsigned int ena, unsigned int dir, unsigned int pul){
	driver -> PULSE_PER_REV = ppr;
	
	driver -> ENA_PIN = ena;
	driver -> DIR_PIN = dir;
	driver -> PUL_PIN = pul;
	
	driver -> PUL_T = 2 * MIN_PUL_T_US;
	
	PORTB = 0;
	DDRB = 0;
	DDRB |= _BV(ena) | _BV(dir) | _BV(pul);
}

void _setSpeed(struct stepdvr_t* driver, unsigned int speed){
	driver -> PUL_T = ((100 - speed) * MIN_PUL_T_US) / 100 + MIN_PUL_T_US;
}

int _rotate(struct stepdvr_t* driver, unsigned int revs, unsigned int dir){
	PORTB |= _BV(driver -> ENA_PIN);
	
	if (driver -> PULSE_PER_REV == 0 || driver -> PUL_T == 0)
		return -1; 

	if (dir)
		PORTB |= _BV(driver -> DIR_PIN);
	else
		PORTB &= ~_BV(driver -> DIR_PIN);

	for (unsigned int pulse = 0; pulse < (driver -> PULSE_PER_REV) * revs; pulse ++){
		PORTB |= _BV(driver -> PUL_PIN);
		
		for (unsigned int t = 0; t < driver -> PUL_T; t ++)
			_delay_us(1);
		
		PORTB &= ~_BV(driver -> PUL_PIN);
		
		for (unsigned int t = 0; t < driver -> PUL_T; t ++)
			_delay_us(1);
	}

	PORTB &= ~_BV(driver -> ENA_PIN);
	return 0;
}
