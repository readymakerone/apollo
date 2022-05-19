#ifndef FRETBOARD_H
#define FRETBOARD_H

#if (ARDUINO >= 100)
  #include "Arduino.h"
#else
  #include "WProgram.h"
#endif

#define STR1 2
#define STR2 3
#define STR3 4
#define STR4 5
#define STR5 6
#define STR6 7
#define NUM_STRINGS 6
#define NUM_FRETS 22

#include "Music.h"
#include <FastLED.h>

class Fretboard {
  public:
    //Constructor
    Fretboard();

    //Methods
    void clear();
    void show(const Note& rootNote, Scale* pScale, Tuning* pTuning);
    void red();
    CRGB leds[NUM_STRINGS][NUM_FRETS + 1];

  private:
    //Atributes
    Note boardNotes[NUM_STRINGS][NUM_FRETS + 1];

    //Methods
    bool isInScale(Note note);
    CRGB ledColor(Note note);
};
extern Fretboard fretboard;

#endif
