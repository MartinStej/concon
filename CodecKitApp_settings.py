#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @file
# @brief Python script for communication with LN_AC-00
#
# This script is written for AT90USB1287, but it can be modified
#
# @author Martin Stejskal

# Universal protocol for embedded systems
from CodecKitApp_lib.HW_bridge_uniprot import *

# Time operations
from time import sleep

# Keyboard events (only debug for now)
#from msvcrt import kbhit



##
# @brief Main function
if __name__ == '__main__':
    global const_UNI_CHAR_HEADER
    global const_UNI_CHAR_DATA
    global const_UNI_CHAR_TAIL
    
    print("[LNAC settings] Alive!")
    
    """
    try:
        #Uniprot_USB_tx_command(ord('N'))
        Uniprot_USB_tx_data( 5)
    except UniException as e:
        print(e)
        print("Exception")
        exit()
    print("ALL OK :=)")
    exit()
    """
    
    try:
        bridge_init()
    except BridgeException_Device_not_found as e:
        print("[Bridge init] " + str(e))
        exit()
    except:
        print("Unknown error during initialization -> exit")
        exit()
        
    
    """
    try:
        print("Max dev index: " + str(bridge_get_number_of_devices()))
    except:
        print("Exception :(")
        exit() 
        """
    try:
        metadata = BRIDGE_METADATA()
        metadata = bridge_get_metadata(0)
    except:
        print("Get metadata fail!")
        exit()
    
    print("Desc: " + str(metadata.s_descriptor))
    print("DID: " + str(metadata.i_Device_ID))
    print("MAX CMD: " + str(metadata.i_MAX_CMD_ID))
    print("Serial number: " + str(metadata.i_serial))
    print("_________________________________________")
    
#    for i in i_buffer_rx:
#        print("RXD {0} | {1} | {2}".format(hex(i), str(unichr(i)), i ))
    
    
    
    
    bridge_close()
    print("[LNAC settings] Bye")
    
    exit()

