/*
 * uartdvrsrc.c
 *
 * Source file for UART Interface driver code.
 *
 * Created: 3/17/2021 
 *
 *  Author: Alexander Alexandrov
 */ 

#include "uartdvrinc.h"

void UART_enable(void){
	UBRR0L = UBRRL_VALUE;
	UBRR0H = UBRRH_VALUE;
	
	UCSR0B = (1 << TXEN0) | (1 << RXEN0);
}

void UART_disable(void){
	UCSR0B = 0;
}

void UART_double_speed(int flag){
	if (flag)
		UCSR0A |= (1 << U2X0);
	else
		UCSR0A &= ~(1 << U2X0);
}

void UART_write_byte(uint8_t data){
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

uint8_t UART_read_byte(void){
	uint8_t data = 0;
	
	while (!(UCSR0A & (1 << RXC0)));
	data = UDR0;
	
	return data;
}
