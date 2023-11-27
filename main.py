"""
GB Emu
"""
##### Libraries #####
import mmap
from tkinter import filedialog

##### Variables #####
seekPos = 0

##### Functions #####


##### Initialisation #####
# Load bios file with filedialog and into a memorymap using mmap
#biosPath = filedialog.askopenfilename(title = "Select BIOS File", filetypes = (("GameBoy Files", "*.gb*"), ("All Files", "*.*")))
#biosPath = "Z:\ROMs\GB\[BIOS] Nintendo Game Boy Boot ROM (World) (Rev 1).gb" # Hardcoded bios for quick testing rn
#print(biosPath)
#biosOpen = open(biosPath, "rb")
#
#bios = mmap.mmap(biosOpen.fileno(), 0, access=mmap.ACCESS_READ)
#print(bios)

# Load rom file with filedialog and into a memorymap using mmap
#romPath = filedialog.askopenfilename(title = "Select ROM File", filetypes = (("GameBoy Files", "*.gb*"), ("All Files", "*.*")))
romPath = "Z:\ROMs\GB\[BIOS] Nintendo Game Boy Boot ROM (World) (Rev 1).gb" # Hardcoded rom for quick testing rn
print(romPath)
romOpen = open(romPath, "rb")
#
romMap = mmap.mmap(romOpen.fileno(), 0, access=mmap.ACCESS_READ)
print(romMap)

# 
#memMap = memoryview(bios)
#print(memMap)
#memMap = mmap.mmap(rom.fileno(), length=0xffff, access=mmap.ACCESS_COPY)
#print(memMap)

##### Main Loop #####
