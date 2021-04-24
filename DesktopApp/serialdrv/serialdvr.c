#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>
#include <string.h>

#define DEV_NAME 1
#define BAUD 2
#define MEDICS_START 3

int conftermstruct(int, struct termios*);

int main(int argc, char* argv[]){
	char dev_name[20] = "/dev/";
	strcat(dev_name, argv[DEV_NAME]);
	
	int serial_file = open(dev_name, O_RDWR | O_NOCTTY | O_NDELAY);
	if (serial_file == -1){
		perror("open");
		return -1;
	}

	struct termios config;
	conftermstruct(serial_file, &config);
	cfsetospeed(&config, atoi(argv[BAUD]));
	
	
	for (int idx = MEDICS_START; idx < argc; idx ++){
		write(serial_file, argv[idx], 1);	
		sleep(1);
	}

	if (close(serial_file) != 0)
		perror("close");
     
	return 0;
}

int conftermstruct(int fd, struct termios* conf){
	if (tcgetattr(fd, conf) == -1){
		perror("tcgetattr");
		return -1;
	}

	conf->c_cflag &= ~PARENB;
	conf->c_cflag &= ~CSTOPB;
	conf->c_cflag &= ~CSIZE;
	conf->c_cflag |= CS8;
	conf->c_cflag &= ~CRTSCTS;

	conf->c_lflag &= ~ICANON;
	conf->c_lflag &= ~ECHO; 
	conf->c_lflag &= ~ECHOE; 
	conf->c_lflag &= ~ECHONL; 
	conf->c_lflag &= ~ISIG;

	conf->c_oflag &= ~OPOST;
        conf->c_oflag &= ~ONLCR;

	if (tcsetattr(fd, TCSANOW, conf) != 0){
		perror("tcsettattr");
		return -1;
	}
	
	return 0;
}
