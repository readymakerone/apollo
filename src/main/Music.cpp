#include "Music.h"
#define NOTES_PER_OCTAVE 12

Note noteByName(char noteLetter, Modifier mod) {
  Note returnNote;
  switch(noteLetter) {
    case 'A':
      returnNote = Note::A;
      break;
    case 'B':
      returnNote = Note::B;
      break;
    case 'C':
      returnNote = Note::C;
      break;
    case 'D':
      returnNote = Note::D;
      break;
    case 'E':
      returnNote = Note::E;
      break;
    case 'F':
      returnNote = Note::F;
      break;
    case 'G':
      returnNote = Note::G;
      break;
    default:
      return Note::undefined;
  }
  int returnInt = static_cast<int>(returnNote) + static_cast<int>(mod);
  returnInt = ((returnInt%NOTES_PER_OCTAVE) + NOTES_PER_OCTAVE)%NOTES_PER_OCTAVE;
  returnNote = static_cast<Note>(returnInt);
  return returnNote;
}

Note noteByVal(int noteValue) {
  switch(noteValue) {
    case 0:
      return Note::A;
    case 1:
      return Note::AsBf;
    case 2:
      return Note::B;
    case 3:
      return Note::C;
    case 4:
      return Note::CsDf;
    case 5:
      return Note::D;
    case 6:
      return Note::DsEf;
    case 7:
      return Note::E;
    case 8:
      return Note::F;
    case 9:
      return Note::FsGf;
    case 10:
      return Note::G;
    case 11:
      return Note::GsAf;
    default:
      return Note::undefined;
  }
}

int noteValFromName(char noteLetter, Modifier mod) {
  Note returnNote = noteByName(noteLetter, mod);
  return static_cast<int>(returnNote);
}

Scale::Scale(const char* nameArray, uint8_t nameLength, const uint8_t* notesArray, uint8_t numOfNotes) {
  scaleName = new char[nameLength];
  notes = new uint8_t[numOfNotes];
  numNotes = numOfNotes;

  memcpy(scaleName, nameArray, nameLength);
  memcpy(notes, notesArray, numOfNotes);
}

Tuning::Tuning(const char* nameArray, uint8_t nameLength, const Note* notesArray, uint8_t numOfStrings) {
  tuningName = new char[nameLength];
  notes = new Note[numOfStrings];

  memcpy(tuningName, nameArray, nameLength);
  for(int string_index = 0; string_index < numOfStrings; string_index++) {
    notes[string_index] = notesArray[string_index];
  }
}
