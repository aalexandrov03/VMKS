/*
 * uartdvrinc.h
 *
 * Header file for UART interface driver code.
 *
 * Created: 3/17/2021 
 *
 *  Author: Alexander Alexandrov
 */ 

#ifndef UARTDVRINC_H_
#define UARTDVRINC_H_

#define BAUD 9600 
#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/setbaud.h>

void UART_enable(void);
void UART_disable(void);

void UART_double_speed(int);

void UART_write_byte(uint8_t);
uint8_t UART_read_byte(void);

#endif