<< -----set initial switches and get nuclear data----- >>
CLOBBER
GETXS 0
GETDECAY 0
FISPACT
* FNS 5 Minutes Inconel-600
{material}
MIND 1E3
HALF
HAZARDS
<< -----irradiation phase----- >>
FLUX    0.05
TIME 1 YEARS ATOMS
FLUX  1
TIME 10 MINS ATOMS
<< ----- cooling phase ---- >>
FLUX 0
ZERO
TIME 1 HOURS ATOMS
TIME 23 HOURS ATOMS
TIME 9 DAYS ATOMS
TIME 355 DAYS ATOMS
END
* END