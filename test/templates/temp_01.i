<< ----- Test template ----- >>
CLOBBER
JSON
GETXS 0
GETDECAY 0
FISPACT
* Test template for template
{material}
<< -----irradiation phase----- >>
FLUX 2.0000e+10
TIME 2 YEARS SPEC
FLUX 1.0000e+11
TIME 10 YEARS SPEC
FLUX  0
TIME 0.667 YEARS SPEC
FLUX 1.0000e+09
TIME 1.330 YEARS SPEC
PULSE 17
  FLUX 0
  TIME 3920 SPEC
  FLUX 1.0000e+10
  TIME 400 SPEC
ENDPULSE
<< ----- cooling phase ---- >>
FLUX 0
ZERO
TIME 1 ATOMS
TIME 299 ATOMS
TIME 25 MINS ATOMS
TIME 30 MINS ATOMS
TIME 2 HOURS ATOMS
TIME 2 HOURS ATOMS
TIME 5 HOURS ATOMS
TIME 14 HOURS ATOMS
TIME 2 DAYS ATOMS
TIME 4 DAYS ATOMS
TIME 23 DAYS ATOMS
TIME 60 DAYS ATOMS
END
* END