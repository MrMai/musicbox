#include <Adafruit_SSD1306.h>
#include <MIDI.h>
#include <Wire.h>
#include <Adafruit_MPR121.h>

MIDI_CREATE_DEFAULT_INSTANCE();

Adafruit_SSD1306 display(4);

Adafruit_MPR121 bank0 = Adafruit_MPR121();
Adafruit_MPR121 bank1 = Adafruit_MPR121();

uint16_t bank0_t_c = 0; // bank 0 current touched
uint16_t bank1_t_c = 0; // bank 1 current touched

uint16_t bank0_t_l = 0; // bank 0 last touched
uint16_t bank1_t_l = 0; // bank 1 last touched

uint8_t button_l = 0;   // last buttons touched


// status varibles
int octave_c = 4;
int note_ref_c = (octave_c + 2) * 12;
int velocity_c = 72;
int channel_c = 1;

void setup() {
  // begin touch sensors
  bank0.begin(0x5A);
  bank1.begin(0x5B);
  // display stuff
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.display();
  // midi stuff?
}

void loop() {
  // get touch sensor data
  bank0_t_c = bank0.touched();
  bank1_t_c = bank1.touched();

  // create delta things
  bool bank_a[24] = {}; // activated
  bool bank_d[24] = {}; // deactivated

  bool button_a[5] = {0,0,0,0,0};

  // check bank0
  for(uint8_t i=0; i<12; i++) {
    if ((bank0_t_c & _BV(i)) && !(bank0_t_l & _BV(i)) ) {
      bank_a[i] = 1;
    }
    if (!(bank0_t_c & _BV(i)) && (bank0_t_l & _BV(i)) ) {
      bank_d[i] = 1;
    }
  }

  // check bank1 (bank1 is wired up inverted so it has to do some abs math. if this is wrong CORRECT IT)
  for(uint8_t i=0; i<12; i++) {
    if ((bank1_t_c & _BV(i)) && !(bank1_t_l & _BV(i)) ) {
      bank_a[(abs(i-23))] = 1;
    }
    if (!(bank1_t_c & _BV(i)) && (bank1_t_l & _BV(i)) ) {
      bank_d[(abs(i-23))] = 1;
    }
  }

  // check buttons for changes, and write those changes to button_a[ctivated]
  if (button_l != PINB) {
    for (int i=0; i<5; i++) {
      button_a[i] = digitalRead(i+8);
    }
    button_l = PINB;
  }
  // octave swtiching with buttons
  if (button_a[0]) {
    octave_c ++;
    note_ref_c = (octave_c + 2) * 12;
  }
  if (button_a[1]) {
    octave_c --;
    note_ref_c = (octave_c + 2) * 12;
  }

  // send notes over midi connection
  for (int i=0; i<sizeof(bank_a); i++) {
    if(bank_a[i]) {
      int note_on = i + note_ref_c;
      MIDI.sendNoteOn(note_on, velocity_c, channel_c);
    }
  }

  for (int i=0; i<sizeof(bank_d); i++) {
    if(bank_a[i]) {
      int note_off = i + note_ref_c;
      MIDI.sendNoteOn(note_off, velocity_c, channel_c);
    }
  }
}

// section is for scale playing mode
/*
int sum_semi(int scale[]) {
  for(int i=0; i<sizeof(scale); i++) {
    if(i != 0) {
      scale[i] += scale[i-1];
    }
  }
}

int shift_semi(int scale[], int shift) {
  int new_scale[] = scale;
  for(int i=0; i<sizeof(scale)); i++) {
    new_scale[i] = scale[i] + shift;
  }
  return new_scale;
}
*/
