/*
 * stepdvrinc.h
 *
 * Header file for step motor driver code.
 *
 * Created: 3/17/2021
 *
 * Author: Alexander Alexandrov
 */ 

#ifndef STEPDVRINC_H_
#define STEPDVRINC_H_

#define F_CPU 16000000UL
#define MIN_PUL_T_US 300

#include <avr/io.h>
#include <util/delay.h>

struct stepdvr_t {
	unsigned int PULSE_PER_REV, ENA_PIN, DIR_PIN, PUL_PIN;
	unsigned int PUL_T;
};

void _init(struct stepdvr_t*, unsigned int, unsigned int, unsigned int, unsigned int);
void _setSpeed(struct stepdvr_t*, unsigned int);
int _rotate(struct stepdvr_t*, unsigned int, unsigned int);

#endif 