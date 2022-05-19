#include <FastLED.h>
#include "Fretboard.h"

#define STR1    2
#define STR2    3
#define STR3    4
#define STR4    5
#define STR5    6
#define STR6    7
#define N_FRET  22

#define TFT_SDA     20
#define TFT_CLK     21
#define TFT_RS      22
#define TFT_RST     23
#define TFT_CS      24
#define N_STRING 6
//Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,      TFT_RS,  TFT_SDA, TFT_CLK,    TFT_RST);
void setup() {
  fretboard.clear();
  delay(500);
  fretboard.red();
  delay(500);
  fretboard.clear();
}

void loop() {
//  float val1 = 64 + (float)64*sin(t*2*PI/1000);
//  float val2 = 64 - 64*sin(t*2*PI/1000);
//  for(int i=0; i < N_STRING; i++) {
//    for(int j=0; j < N_FRET+1; j++) {
//      if((i+j)%2){
//        leds[i][j] = CRGB(0, (int)(128-val2), 0);
//      } else {
//        leds[i][j] = CRGB(0,(int)val2,0);
//      }
//    }
//  }
//  FastLED.show();
//  delay(1);
//  t = (t+1)%1000;
  // put your main code here, to run repeatedly:
}
