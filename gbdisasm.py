"""
GB Disassembler
"""
##### Libraries #####
import mmap # Used for reading the ROM
#import os.path # Used to find if file exists
import sys # Used to log disassembled output
from tkinter import filedialog # File dialog to load ROM

##### Variables #####
seekPos = 0x00 # Starting position of romMap's seek, obviously at the start of the rom

##### Functions #####


##### Initialisation #####
# Load rom file with filedialog and into a memorymap using mmap
#romPath = filedialog.askopenfilename(title = "Select ROM File", filetypes = (("GameBoy Files", "*.gb*"), ("All Files", "*.*")))
romPath = "Z:\ROMs\GB\[BIOS] Nintendo Game Boy Boot ROM (World) (Rev 1).gb" # Hardcoded rom for quick testing rn
print(romPath)
romOpen = open(romPath, "rb")
#
romMap = mmap.mmap(romOpen.fileno(), 0, access=mmap.ACCESS_READ)
print(romMap)
# Set the seek position of the romMap to seekPos, which is 0x00 currently
romMap.seek(seekPos)
# Set up sys.stdout to log the disassembled code
sys.stdout = open("disasmLog.txt", "w")

##### Main Loop #####
# While loop that 
while seekPos < romMap.size():
    print(hex(seekPos), end=" ") # Debug: Prints position of current byte disassembler is on
    # Convert current read byte to integer, compares correctly with Python hex format
    currentByte = int.from_bytes(romMap.read(1), byteorder="little")
    print(hex(currentByte), end=" ") # Debug: Prints current byte disassembler is on
    # Opcode decoder if statements
    if currentByte == 0x00:
        print("NOP")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x01:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD BC," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0x02:
        print("LD (BC),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x03:
        print("INC BC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x04:
        print("INC B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x05:
        print("DEC B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x06:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD B," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x07:
        print("RLCA")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x08:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD (" + hex(currentByte) + "),SP")
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0x09:
        print("ADD HL,BC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0A:
        print("LD A,(BC)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0B:
        print("DEC BC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0C:
        print("INC C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0D:
        print("DEC C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0E:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD C," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x0F:
        print("RRCA")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x10:
        print("STOP")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x11:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD DE," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0x12:
        print("LD (DE),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x13:
        print("INC DE")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x14:
        print("INC D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x15:
        print("DEC D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x16:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD D," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x17:
        print("RLA")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x18:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("JR " + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x19:
        print("ADD HL,DE")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1A:
        print("LD A,(DE)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1B:
        print("DEC DE")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1C:
        print("INC E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1D:
        print("DEC E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1E:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD E," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x1F:
        print("RRA")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x20:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("JR NZ," + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x21:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD HL," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0x22:
        print("LD (HL+),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x23:
        print("INC HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x24:
        print("INC H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x25:
        print("DEC H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x26:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD H," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x27:
        print("DAA")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x28:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("JR Z," + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x29:
        print("ADD HL,HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2A:
        print("LD A,(HL+)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2B:
        print("DEC HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2C:
        print("INC L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2D:
        print("DEC L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2E:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD L," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x2F:
        print("CPL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x30:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("JR NC," + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x31:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD SP," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0x32:
        print("LD (HL-),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x33:
        print("INC SP")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x34:
        print("INC (HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x35:
        print("DEC (HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x36:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD (HL)," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x37:
        print("SCF")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x38:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("JR C," + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x39:
        print("ADD HL,SP")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3A:
        print("LD A,(HL-)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3B:
        print("DEC SP")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3C:
        print("INC A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3D:
        print("DEC A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3E:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x3F:
        print("CCF")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x40:
        print("LD B,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x41:
        print("LD B,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x42:
        print("LD B,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x43:
        print("LD B,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x44:
        print("LD B,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x45:
        print("LD B,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x46:
        print("LD B,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x47:
        print("LD B,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x48:
        print("LD C,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x49:
        print("LD C,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4A:
        print("LD C,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4B:
        print("LD C,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4C:
        print("LD C,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4D:
        print("LD C,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4E:
        print("LD C,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x4F:
        print("LD C,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x50:
        print("LD D,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x51:
        print("LD D,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x52:
        print("LD D,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x53:
        print("LD D,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x54:
        print("LD D,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x55:
        print("LD D,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x56:
        print("LD D,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x57:
        print("LD D,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x58:
        print("LD E,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x59:
        print("LD E,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5A:
        print("LD E,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5B:
        print("LD E,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5C:
        print("LD E,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5D:
        print("LD E,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5E:
        print("LD E,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x5F:
        print("LD E,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x60:
        print("LD H,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x61:
        print("LD H,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x62:
        print("LD H,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x63:
        print("LD H,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x64:
        print("LD H,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x65:
        print("LD H,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x66:
        print("LD H,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x67:
        print("LD H,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x68:
        print("LD L,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x69:
        print("LD L,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6A:
        print("LD L,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6B:
        print("LD L,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6C:
        print("LD L,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6D:
        print("LD L,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6E:
        print("LD L,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x6F:
        print("LD L,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x70:
        print("LD (HL),B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x71:
        print("LD (HL),C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x72:
        print("LD (HL),D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x73:
        print("LD (HL),E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x74:
        print("LD (HL),H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x75:
        print("LD (HL),L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x76:
        print("HALT")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x77:
        print("LD (HL),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x78:
        print("LD A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x79:
        print("LD A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7A:
        print("LD A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7B:
        print("LD A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7C:
        print("LD A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7D:
        print("LD A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7E:
        print("LD A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x7F:
        print("LD A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x80:
        print("ADD A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x81:
        print("ADD A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x82:
        print("ADD A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x83:
        print("ADD A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x84:
        print("ADD A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x85:
        print("ADD A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x86:
        print("ADD A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x87:
        print("ADD A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x88:
        print("ADC A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x89:
        print("ADC A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8A:
        print("ADC A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8B:
        print("ADC A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8C:
        print("ADC A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8D:
        print("ADC A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8E:
        print("ADC A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x8F:
        print("ADC A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x90:
        print("SUB A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x91:
        print("SUB A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x92:
        print("SUB A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x93:
        print("SUB A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x94:
        print("SUB A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x95:
        print("SUB A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x96:
        print("SUB A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x97:
        print("SUB A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x98:
        print("SBC A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x99:
        print("SBC A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9A:
        print("SBC A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9B:
        print("SBC A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9C:
        print("SBC A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9D:
        print("SBC A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9E:
        print("SBC A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0x9F:
        print("SBC A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA0:
        print("AND A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA1:
        print("AND A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA2:
        print("AND A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA3:
        print("AND A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA4:
        print("AND A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA5:
        print("AND A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA6:
        print("AND A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA7:
        print("AND A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA8:
        print("XOR A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xA9:
        print("XOR A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAA:
        print("XOR A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAB:
        print("XOR A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAC:
        print("XOR A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAD:
        print("XOR A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAE:
        print("XOR A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xAF:
        print("XOR A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB0:
        print("OR A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB1:
        print("OR A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB2:
        print("OR A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB3:
        print("OR A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB4:
        print("OR A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB5:
        print("OR A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB6:
        print("OR A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB7:
        print("OR A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB8:
        print("CP A,B")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xB9:
        print("CP A,C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBA:
        print("CP A,D")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBB:
        print("CP A,E")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBC:
        print("CP A,H")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBD:
        print("CP A,L")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBE:
        print("CP A,(HL)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xBF:
        print("CP A,A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC0:
        print("RET NZ")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC1:
        print("POP BC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC2:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("JP NZ," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xC3:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("JP," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xC4:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("CALL NZ," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xC5:
        print("PUSH BC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC6:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("ADD A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC7:
        print("RST 00h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC8:
        print("RET Z")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xC9:
        print("RET")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xCA:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("JP Z," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    # Wonder why 0xCB missing? It is a trigger to go to the other 256 opcodes
    elif currentByte == 0xCC:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("CALL Z," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xCD:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("CALL " + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xCE:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("ADC A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xCF:
        print("RST 08h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD0:
        print("RET NC")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD1:
        print("POP DE")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD2:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("JP NC," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    # 0xD3 has no opcode
    elif currentByte == 0xD4:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("CALL NC," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xD5:
        print("PUSH DE")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD6:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("SUB A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD7:
        print("RST 10h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD8:
        print("RET C")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xD9:
        print("RETI")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xDA:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("JP C," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    # 0xDB has no opcode
    elif currentByte == 0xDC:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("CALL C," + hex(currentByte))
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    # 0xDD has no opcode
    elif currentByte == 0xDE:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("SBC A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xDF:
        print("RST 18h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE0:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD (FF00+" + hex(currentByte) + "),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE1:
        print("POP HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE2:
        print("LD (FF00+C),A")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    # 0xE3 has no opcode
    # 0xE4 has no opcode
    elif currentByte == 0xE5:
        print("PUSH HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE6:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("AND A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE7:
        print("RST 20h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE8:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("ADD SP," + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xE9:
        print("JP HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xEA:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")        
        print("LD (" + hex(currentByte) + "),A")
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    # 0xEB has no opcode
    # 0xEC has no opcode
    # 0xED has no opcode
    elif currentByte == 0xEE:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("XOR A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xEF:
        print("RST 28h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF0:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD A,(FF00+" + hex(currentByte) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF1:
        print("POP AF")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF2:
        print("LD A,(FF00+C)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF3:
        print("DI")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    # 0xF4 has no opcode
    elif currentByte == 0xF5:
        print("PUSH AF")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF6:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("OR A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF7:
        print("RST 30h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF8:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("LD HL,SP+" + hex(currentByte), end=" ")
        if currentByte >= 0x80: currentByteSigned = -(currentByte & 0x80) | (currentByte & 0x7f)
        print("(Signed int: " + str(currentByteSigned) + ")")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xF9:
        print("LD SP,HL")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xFA:
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        currentByte = int.from_bytes(romMap.read(2), byteorder="little")
        print("LD A,(" + hex(currentByte) + ")")
        seekPos = seekPos + 2
        romMap.seek(seekPos)
    elif currentByte == 0xFB:
        print("EI")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    # 0xEB has no opcode
    # 0xEC has no opcode
    # 0xED has no opcode
    elif currentByte == 0xFE:
        seekPos = seekPos + 1
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print("CP A," + hex(currentByte))
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    elif currentByte == 0xFF:
        print("RST 38h")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
    # 0xCB prefix opcodes
    elif currentByte == 0xCB:
        print("PREFIX 0xCB (Go to other 256 opcodes)")
        seekPos = seekPos + 1
        romMap.seek(seekPos)
        print(hex(seekPos), end=" ") # Debug: Prints position of current byte disassembler is on
        # Convert current read byte to integer, compares correctly with Python hex format
        currentByte = int.from_bytes(romMap.read(1), byteorder="little")
        print(hex(currentByte), end=" ") # Debug: Prints current byte disassembler is on
        # Opcode decoder if statements for 0xCB prefix opcodes
        if currentByte == 0x00:
            print("RLC B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x01:
            print("RLC C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x02:
            print("RLC D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x03:
            print("RLC E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x04:
            print("RLC H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x05:
            print("RLC L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x06:
            print("RLC (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x07:
            print("RLC A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x08:
            print("RRC B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x09:
            print("RRC C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0A:
            print("RRC D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0B:
            print("RRC E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0C:
            print("RRC H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0D:
            print("RRC L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0E:
            print("RRC (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x0F:
            print("RRC A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x10:
            print("RL B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x11:
            print("RL C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x12:
            print("RL D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x13:
            print("RL E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x14:
            print("RL H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x15:
            print("RL L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x16:
            print("RL (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x17:
            print("RL A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x18:
            print("RR B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x19:
            print("RR C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1A:
            print("RR D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1B:
            print("RR E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1C:
            print("RR H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1D:
            print("RR L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1E:
            print("RR (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x1F:
            print("RR A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x20:
            print("SLA B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x21:
            print("SLA C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x22:
            print("SLA D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x23:
            print("SLA E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x24:
            print("SLA H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x25:
            print("SLA L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x26:
            print("SLA (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x27:
            print("SLA A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x28:
            print("SRA B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x29:
            print("SRA C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2A:
            print("SRA D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2B:
            print("SRA E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2C:
            print("SRA H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2D:
            print("SRA L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2E:
            print("SRA (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x2F:
            print("SRA A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x30:
            print("SWAP B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x31:
            print("SWAP C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x32:
            print("SWAP D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x33:
            print("SWAP E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x34:
            print("SWAP H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x35:
            print("SWAP L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x36:
            print("SWAP (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x37:
            print("SWAP A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x38:
            print("SRL B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x39:
            print("SRL C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3A:
            print("SRL D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3B:
            print("SRL E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3C:
            print("SRL H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3D:
            print("SRL L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3E:
            print("SRL (HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x3F:
            print("SRL A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x40:
            print("BIT 0,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x41:
            print("BIT 0,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x42:
            print("BIT 0,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x43:
            print("BIT 0,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x44:
            print("BIT 0,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x45:
            print("BIT 0,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x46:
            print("BIT 0,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x47:
            print("BIT 0,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x48:
            print("BIT 1,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x49:
            print("BIT 1,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4A:
            print("BIT 1,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4B:
            print("BIT 1,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4C:
            print("BIT 1,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4D:
            print("BIT 1,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4E:
            print("BIT 1,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x4F:
            print("BIT 1,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x50:
            print("BIT 2,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x51:
            print("BIT 2,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x52:
            print("BIT 2,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x53:
            print("BIT 2,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x54:
            print("BIT 2,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x55:
            print("BIT 2,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x56:
            print("BIT 2,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x57:
            print("BIT 2,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x58:
            print("BIT 3,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x59:
            print("BIT 3,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5A:
            print("BIT 3,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5B:
            print("BIT 3,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5C:
            print("BIT 3,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5D:
            print("BIT 3,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5E:
            print("BIT 3,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x5F:
            print("BIT 3,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x60:
            print("BIT 4,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x61:
            print("BIT 4,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x62:
            print("BIT 4,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x63:
            print("BIT 4,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x64:
            print("BIT 4,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x65:
            print("BIT 4,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x66:
            print("BIT 4,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x67:
            print("BIT 4,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x68:
            print("BIT 5,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x69:
            print("BIT 5,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6A:
            print("BIT 5,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6B:
            print("BIT 5,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6C:
            print("BIT 5,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6D:
            print("BIT 5,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6E:
            print("BIT 5,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x6F:
            print("BIT 5,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x70:
            print("BIT 6,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x71:
            print("BIT 6,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x72:
            print("BIT 6,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x73:
            print("BIT 6,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x74:
            print("BIT 6,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x75:
            print("BIT 6,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x76:
            print("BIT 6,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x77:
            print("BIT 6,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x78:
            print("BIT 7,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x79:
            print("BIT 7,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7A:
            print("BIT 7,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7B:
            print("BIT 7,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7C:
            print("BIT 7,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7D:
            print("BIT 7,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7E:
            print("BIT 7,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x7F:
            print("BIT 7,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x80:
            print("RES 0,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x81:
            print("RES 0,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x82:
            print("RES 0,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x83:
            print("RES 0,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x84:
            print("RES 0,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x85:
            print("RES 0,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x86:
            print("RES 0,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x87:
            print("RES 0,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x88:
            print("RES 1,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x89:
            print("RES 1,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8A:
            print("RES 1,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8B:
            print("RES 1,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8C:
            print("RES 1,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8D:
            print("RES 1,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8E:
            print("RES 1,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x8F:
            print("RES 1,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x90:
            print("RES 2,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x91:
            print("RES 2,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x92:
            print("RES 2,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x93:
            print("RES 2,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x94:
            print("RES 2,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x95:
            print("RES 2,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x96:
            print("RES 2,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x97:
            print("RES 2,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x98:
            print("RES 3,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x99:
            print("RES 3,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9A:
            print("RES 3,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9B:
            print("RES 3,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9C:
            print("RES 3,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9D:
            print("RES 3,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9E:
            print("RES 3,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0x9F:
            print("RES 3,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA0:
            print("RES 4,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA1:
            print("RES 4,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA2:
            print("RES 4,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA3:
            print("RES 4,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA4:
            print("RES 4,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA5:
            print("RES 4,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA6:
            print("RES 4,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA7:
            print("RES 4,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA8:
            print("RES 5,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xA9:
            print("RES 5,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAA:
            print("RES 5,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAB:
            print("RES 5,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAC:
            print("RES 5,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAD:
            print("RES 5,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAE:
            print("RES 5,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xAF:
            print("RES 5,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB0:
            print("RES 6,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB1:
            print("RES 6,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB2:
            print("RES 6,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB3:
            print("RES 6,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB4:
            print("RES 6,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB5:
            print("RES 6,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB6:
            print("RES 6,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB7:
            print("RES 6,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB8:
            print("RES 7,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xB9:
            print("RES 7,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBA:
            print("RES 7,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBB:
            print("RES 7,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBC:
            print("RES 7,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBD:
            print("RES 7,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBE:
            print("RES 7,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xBF:
            print("RES 7,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC0:
            print("SET 0,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC1:
            print("SET 0,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC2:
            print("SET 0,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC3:
            print("SET 0,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC4:
            print("SET 0,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC5:
            print("SET 0,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC6:
            print("SET 0,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC7:
            print("SET 0,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC8:
            print("SET 1,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xC9:
            print("SET 1,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCA:
            print("SET 1,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCB:
            print("SET 1,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCC:
            print("SET 1,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCD:
            print("SET 1,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCE:
            print("SET 1,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xCF:
            print("SET 1,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD0:
            print("SET 2,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD1:
            print("SET 2,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD2:
            print("SET 2,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD3:
            print("SET 2,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD4:
            print("SET 2,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD5:
            print("SET 2,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD6:
            print("SET 2,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD7:
            print("SET 2,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD8:
            print("SET 3,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xD9:
            print("SET 3,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDA:
            print("SET 3,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDB:
            print("SET 3,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDC:
            print("SET 3,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDD:
            print("SET 3,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDE:
            print("SET 3,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xDF:
            print("SET 3,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE0:
            print("SET 4,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE1:
            print("SET 4,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE2:
            print("SET 4,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE3:
            print("SET 4,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE4:
            print("SET 4,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE5:
            print("SET 4,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE6:
            print("SET 4,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE7:
            print("SET 4,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE8:
            print("SET 5,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xE9:
            print("SET 5,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xEA:
            print("SET 5,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xEB:
            print("SET 5,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xEC:
            print("SET 5,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xED:
            print("SET 5,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xEE:
            print("SET 5,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xEF:
            print("SET 5,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF0:
            print("SET 6,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF1:
            print("SET 6,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF2:
            print("SET 6,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF3:
            print("SET 6,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF4:
            print("SET 6,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF5:
            print("SET 6,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF6:
            print("SET 6,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF7:
            print("SET 6,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF8:
            print("SET 7,B")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xF9:
            print("SET 7,C")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFA:
            print("SET 7,D")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFB:
            print("SET 7,E")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFC:
            print("SET 7,H")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFD:
            print("SET 7,L")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFE:
            print("SET 7,(HL)")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
        elif currentByte == 0xFF:
            print("SET 7,A")
            seekPos = seekPos + 1
            romMap.seek(seekPos)
    else:
        print("Opcode doesn't exist, must be part of data")