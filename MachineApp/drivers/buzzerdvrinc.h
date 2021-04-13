/*
 * buzzerdvrinc.h
 *
 * Created: 4/13/2021 5:21:51 PM
 * Author: Alexander Alexandrov
 */ 

#ifndef BUZZERDVRINC_H_
#define BUZZERDVRINC_H_

#include <avr/io.h>
#include <avr/sfr_defs.h>

static int buzzer_state = 0;

void _initBuzzer(void);
void _toggleBuzzer(void);

#endif