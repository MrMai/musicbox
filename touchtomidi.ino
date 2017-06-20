#include <MIDI.h>
#include <Wire.h>
#include "Adafruit_MPR121.h"

MIDI_CREATE_DEFAULT_INSTANCE();

Adafruit_SSD1306 display(OLED_RESET);

Adafruit_MPR121 bank0 = Adafruit_MPR121();
Adafruit_MPR121 bank1 = Adafruit_MPR121();

unit8_t bank0_t_c = 0; // bank 0 current touched
unit8_t bank1_t_c = 0; // bank 1 current touched

unit8_t bank0_t_l = 0; // bank 0 last touched
unit8_t bank1_t_l = 0; // bank 1 last touched

void setup() {
  // begin touch sensors
  bank0.begin(0x5A);
  bank1.begin(0x5B);
  // display stuff
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.display();
}

void loop() {
  // get touch sensor data
  bank0_t_c = bank0.touched();
  bank1_t_c = bank1.touched();

  // create delta vars
  activated[24] = {};
  deactivated[24] = {};

  // check bank0
  for(unit8_t i=0; i<12; i++) {
    if ((bank0_t_c & _BV(i)) && !(bank0_t_l & _BV(i)) ) {
      activated.append(i);
    }
    if (!(bank0_t_c & _BV(i)) && (bank0_t_l & _BV(i)) ) {
      deactivated.append(i);
    }
  }

  // check bank1 (bank1 is wired up inverted so it has to do some abs math. if this is wrong CORRECT IT)
  for(unit8_t i=0; i<12; i++) {
    if ((bank1_t_c & _BV(i)) && !(bank1_t_l & _BV(i)) ) {
      activated.append(abs(i-23));
    }
    if (!(bank1_t_c & _BV(i)) && (bank1_t_l & _BV(i)) ) {
      deactivated.append(abs(i-23));
    }
  }
}

int sum_semi(int scale[]) {
  for(int i=0; i<sizeof(scale); i++) {
    if(i != 0) {
      scale[i] += scale[i-1];
    }
  }
}

int shift_semi(int scale[], int shift) {
  new_scale[] = scale;
  for(int i=0; i<sizeof(scale)); i++) {
    new_scale[i] = scale[i] + shift;
  }
  return new_scale;
}
