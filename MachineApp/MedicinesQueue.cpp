/*
 * MedicinesQueue.cpp
 *
 * Created: 4/14/2021 8:39:12 PM
 *  Author: Alexander Alexandrov
 */ 

#include "MedicinesQueue.h"

MedicineQueue::MedicineQueue(){
	head = 0;
	tail = 0;
	full = false;
	empty = true;
}

void MedicineQueue::enqueue(int slot_id){
	if (isFull() == true)
		return;
		
	container[head] = slot_id;
	head = (head + 1) % SIZE;
	empty = false;
	
	if (head == tail)
		full = true;	
}

int MedicineQueue::dequeue(void){
	if (isEmpty() == true)
		return -1;
	
	int res = container[tail];
	tail = (tail + 1) % SIZE;
	full = false;
	
	if (tail == head)
		empty = true;
		
	return res;
}

bool MedicineQueue::isEmpty(void){
	return empty;
}

bool MedicineQueue::isFull(void){
	return full;
}