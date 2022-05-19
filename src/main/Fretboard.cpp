#include "Fretboard.h"

Fretboard fretboard = Fretboard::Fretboard();

Fretboard::Fretboard()
{
  FastLED.addLeds<WS2812B, STR1, GRB>(leds[0], NUM_FRETS+1);
  FastLED.addLeds<WS2812B, STR2, GRB>(leds[1], NUM_FRETS+1);
  FastLED.addLeds<WS2812B, STR3, GRB>(leds[2], NUM_FRETS+1);
  FastLED.addLeds<WS2812B, STR4, GRB>(leds[3], NUM_FRETS+1);
  FastLED.addLeds<WS2812B, STR5, GRB>(leds[4], NUM_FRETS+1);
  FastLED.addLeds<WS2812B, STR6, GRB>(leds[5], NUM_FRETS+1);
}

void Fretboard::clear() {
  for(int i=0; i<NUM_STRINGS; i++) {
    for(int j=0; j<NUM_FRETS+1; j++) {
      leds[i][j] = CRGB(0,0,0);
    }
  }
  FastLED.show();
}

void Fretboard::red() {
  for(int j=0; j<NUM_FRETS+1; j++) {
    leds[0][j] = CRGB(255,0,0);
  }
  FastLED.show();
}
