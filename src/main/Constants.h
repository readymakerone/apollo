#ifndef CONSTANTS_H
#define CONSTANTS_H

#if (ARDUINO >= 100)
  #include "Arduino.h"
#else
  #include "WProgram.h"
#endif

#include "Music.h"
#include <FastLED.h>
#include <Wire.h>
//#include <SSD1306Ascii.h>
//#include <SSD1306AsciiWire.h>

#define NUM_STRINGS       6
#define NUM_FRETS         21
#define NUM_LEDS          NUM_STRINGS * (NUM_FRETS + 1)
#define DATA_PIN          2
#define NOTES_PER_OCTAVE  12
#define NUMBER_OF_SCALES  12
#define NUMBER_OF_TUNINGS 4
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET 4
#define DISPLAY_ADDRESS 0x3C
#define TUNING_BUTTON_PIN 22
#define NOTE_BUTTON_PIN 24
#define SCALE_BUTTON_PIN 25
#define LED_PIN 51
#define DEFAULT_DEBOUNCE_DELAY 50

extern const CRGB RGB_BLACK;
extern const CRGB RGB_RED;
extern const CRGB RGB_GREEN;
extern const CRGB RGB_BLUE;
//extern const CRGB RGB_YELLOW;
//extern const CRGB RGB_CYAN;
//extern const CRGB RGB_MAGENTA;
extern const CRGB RGB_WHITE;
extern const CRGB RGB_ORANGE;

extern Scale hminor;
extern Scale majorblues;
extern Scale minorblues;
extern Scale majorpent;
extern Scale minorpent;
extern Scale locrian;
extern Scale minor;
extern Scale mixolydian;
extern Scale lydian;
extern Scale phrygian;
extern Scale dorian;
extern Scale major;

extern Tuning standard;
extern Tuning flatstandard;
extern Tuning dropd;
extern Tuning openc;

extern const char noteNames[NOTES_PER_OCTAVE][6];
extern Scale* pScalesTable[1];
extern Tuning* pTuningsTable[NUMBER_OF_TUNINGS];
//extern SSD1306AsciiWire oled;

#endif
