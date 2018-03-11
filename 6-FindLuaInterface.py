#!/usr/bin/python
"""
Tree of Savior IDAPython Script
Find LuaInterface getters
"""
import idaapi
import idautils
import idc

"""
Getter example:
.text:00496080                 push    offset aFast    ; "FAST"
.text:00496085                 mov     ecx, offset unk_12F5614
.text:0049608A                 call    LuaInterface::getInstance
"""

LuaInterface__getInstance = 0xD22720

MakeNameEx (LuaInterface__getInstance, "LuaInterface::getInstance", SN_NOWARN);

def MakeNameForce (address, name):
    x = 2;
    newName = name;
    while (MakeNameEx (address, newName, SN_NOWARN) == 0):
        newName = "%s_%d" % (name, x);
        x = x + 1;
        if x > 300:
            break;
    return newName;

occ = RfirstB (LuaInterface__getInstance);
while occ != BADADDR:
    movAddress = PrevHead (occ);
    pushAddress = PrevHead (movAddress);

    if (GetMnem (pushAddress) == "push" 
    and GetMnem (movAddress) == "mov" ):
        sidAddress = GetOperandValue (movAddress, 1); #the second operand
        strAddress = GetOperandValue (pushAddress, 0);
        if GetString (strAddress) != None:
            MakeData (sidAddress, FF_DWRD, 4, 0);
            MakeNameForce (sidAddress, "SID_" + GetString (strAddress));
        else: 
            print "Another Exception " + hex(occ)
    else:
        print "Exception " + hex(occ)

    occ = RnextB (LuaInterface__getInstance, occ);
