
#include "Constants.h"

const CRGB RGB_BLACK = CRGB(0,0,0);
const CRGB RGB_RED = CRGB(255,0,0);
const CRGB RGB_GREEN = CRGB(0,255,0);
const CRGB RGB_BLUE = CRGB(0,0,255);
//const CRGB RGB_YELLOW = CRGB(255,255,0);
//const CRGB RGB_CYAN = CRGB(0,255,255);
//const CRGB RGB_MAGENTA = CRGB(255,0,255);
const CRGB RGB_WHITE = CRGB(255,255,255);
const CRGB RGB_ORANGE = CRGB(255,100,0);

//Init all desired scale shapes
//Scale hminor("Harmonic Minor", 14, new uint8_t[7]{0,2,3,5,7,8,11}, 7);
//Scale majorblues("Major Blues", 11, new uint8_t[6]{0,2,3,4,6,9}, 6);
//Scale minorblues("Minor Blues", 11, new uint8_t[6]{0,3,5,6,7,10}, 6);
//Scale majorpent("Major Pentatonic", 16, new uint8_t[5]{0,2,4,7,9}, 5);
//Scale minorpent("Minor Pentatonic", 16, new uint8_t[5]{0,3,5,7,10}, 5);
//Scale locrian("Locrian", 7, new uint8_t[7]{0,1,3,5,6,8,10}, 7);
//Scale minor("Minor", 5, new uint8_t[7]{0,2,3,5,7,8,10}, 7);
//Scale mixolydian("Mixolydian", 10, new uint8_t[7]{0,2,4,5,7,9,10}, 7);
//Scale lydian("Lydian", 6, new uint8_t[7]{0,2,4,6,7,9,11}, 7);
//Scale phrygian("Phrygian", 8, new uint8_t[7]{0,1,3,5,7,8,10}, 7);
//Scale dorian("Dorian", 6, new uint8_t[7]{0,2,3,5,7,9,10}, 7);
Scale major("Major", 5, new uint8_t[7]{0,2,4,5,7,9,11}, 7);

//Init all desired tunings
Tuning standard("Standard", 8, new Note[NUM_STRINGS] {Note::E, Note::A, Note::D, Note::G, Note::B, Note::E}, NUM_STRINGS);
Tuning flatstandard("Eb Standard", 11, new Note[NUM_STRINGS] {Note::DsEf, Note::GsAf, Note::CsDf, Note::FsGf, Note::AsBf, Note::DsEf}, NUM_STRINGS);
Tuning dropd("Drop D", 6, new Note[NUM_STRINGS] {Note::D, Note::A, Note::D, Note::G, Note::B, Note::E}, NUM_STRINGS);
Tuning openc("C Open", 6, new Note[NUM_STRINGS] {Note::C, Note::G, Note::C, Note::G, Note::C, Note::E}, NUM_STRINGS);

const char noteNames[NOTES_PER_OCTAVE][6] = { "A",
                                              "A#/Bb",
                                              "B",
                                              "C",
                                              "C#/Db",
                                              "D",
                                              "D#/Eb",
                                              "E",
                                              "F",
                                              "F#/Gb",
                                              "G",
                                              "G#/Ab" };

Scale* pScalesTable[1] = {&major};
//                                        { &major,
//                                          &minor,
//                                          &minorpent,
//                                          &majorpent,
//                                          &minorblues,
//                                          &majorblues,
//                                          &hminor,
//                                          &dorian,
//                                          &phrygian,
//                                          &lydian,
//                                          &mixolydian,
//                                          &locrian };

Tuning* pTuningsTable[NUMBER_OF_TUNINGS] = {  &standard,
                                              &flatstandard,
                                              &dropd,
                                              &openc };

//SSD1306AsciiWire oled;
