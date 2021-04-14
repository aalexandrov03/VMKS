/*
 * MedicinesQueue.h
 *
 * Created: 4/14/2021 8:38:52 PM
 *  Author: Alexander Alexandrov
 */ 


#ifndef MEDICINESQUEUE_H_
#define MEDICINESQUEUE_H_

#define SIZE 30

class MedicineQueue{
	private:
		int container[SIZE];
		int head, tail;
		bool full, empty;
		
	public:
		MedicineQueue(void);
		void enqueue(int);
		int dequeue(void);
		bool isEmpty(void);
		bool isFull(void);
};

#endif 