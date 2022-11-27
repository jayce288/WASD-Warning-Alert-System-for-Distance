#include <SoftwareSerial.h>
#include <TinyGPS.h>
#define RXPIN 6
#define TXPIN 5
#define xRX 12
#define xTX 13
#define GPSBAUD 9600

SoftwareSerial xbee(xRX,xTX);
TinyGPS gps;
SoftwareSerial uart_gps(RXPIN,TXPIN);

void setup(){
  xbee.begin(9600);
  Serial.begin(9600);
  uart_gps.begin(GPSBAUD);
}

void getgps(TinyGPS &gps){

  float latitude, longitude, altitude;
  gps.f_get_position(&latitude, &longitude);
  altitude = gps.f_altitude();

  String str_latitude = String(latitude,5);
  String str_longitude = String(longitude,5);
  String str_altitude = String(altitude,5);
}

void loop(){
  while(uart_gps.available()){

    int c = uart_gps.read();

    if(gps.encode(c)){
      getgps(gps);
    }
  }
}
