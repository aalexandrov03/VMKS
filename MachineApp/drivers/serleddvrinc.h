/*
 * serleddvrinc.h
 *
 * Created: 4/13/2021 8:01:55 PM
 * Author: Alexander Alexandrov
 */ 


#ifndef SERLEDDVRINC_H_
#define SERLEDDVRINC_H_

#include <avr/io.h>
#include <avr/sfr_defs.h>

void _initSerialLED(void);
int _checkSerialConnected(void);
void _serialReady(void);
void _serialBusy(void);

#endif