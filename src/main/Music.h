#ifndef MUSIC_H
#define MUSIC_H

#if (ARDUINO >= 100)
  #include "Arduino.h"
#else
  #include "WProgram.h"
#endif

enum class Note {
  undefined = -1,
  A = 0,
  AsBf = 1,
  B = 2,
  C = 3,
  CsDf = 4,
  D = 5,
  DsEf = 6,
  E = 7,
  F = 8,
  FsGf = 9,
  G = 10,
  GsAf = 11
};

enum class Modifier {
  sharp = 1,
  flat = -1
};

class Scale {
  public:
  // Constructor
    Scale(const char* nameArray, uint8_t nameLength, const uint8_t* notesArray, uint8_t numOfNotes);

    char* scaleName;
    uint8_t* notes;
    uint8_t numNotes;
  // Methods


  private:
};

class Tuning {
  public:
  // Constructor
    Tuning(const char* nameArray, uint8_t nameLength, const Note* notesArray, uint8_t numOfStrings);

    char* tuningName;
    Note* notes;
  // Methods


  private:
};

Note noteByName(char noteLetter, int8_t mod);
Note noteByVal(int noteValue);
int noteValFromName(char noteLetter);

#endif
