SET R1, 0x03
SET R2, 0x00
SET R3, rai ; DIRECCION DE LA INTERRUPCION
STR [0x00], R3; GUARDAR EN 0X00 LA DIRECCIONDE LA INTERRUPCION

loop: CMP R1, R2
JZ fin
JMP loop

fin: CLI ; deshabilitar atencion de interrupciones

halt: JMP halt

rai: DEC R1
IRET
