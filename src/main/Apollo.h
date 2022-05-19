#ifndef APOLLO_H
#define APOLLO_H

#if (ARDUINO >= 100)
  #include "Arduino.h"
#else
  #include "WProgram.h"
#endif

#include "Fretboard.h"

class Apollo {
  public:
    //Constructor
    Apollo();

    //Attributes
    
    Fretboard board;
  
    //Methods
    void upRoot();
    void downRoot();
    void nextScale();
    void lastScale();
    void nextTuning();
    void lastTuning();

  private:
    //Atributes
    Note root;
    Scale* pScale;
    Tuning* pTuning;

    //Methods
};
extern Apollo apollo;

#endif
