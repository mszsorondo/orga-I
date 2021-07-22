SET R3, 0x00
STR [0xF1], 0x02
LOAD R4, [0xF1]

max:
STR [0XF0], 0x0F
CMP R3, 0x10
JZ incremBocina
JMP max

incremBocina:
INC R4
STR [0xF1], R4
SET R3, 0x00
JMP max

interrupcionCurva:
SET R0, 0x00
confirmacionCurva:
CMP R0, 0x00
JNZ writeVelC
INC R3
writeVelC: STR [0XF0], 0x0C
INC R0
JMP confirmacionCurva
