import serial                                                                                                         
import sys
                                                                                                                        
def main():
    port = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyUSB0"                                                       
                                                                                                                        
    try:
        ser = serial.Serial(                                                                                          
            port=port,
            baudrate=4800,                                                                                            
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,                                                                                
            stopbits=serial.STOPBITS_ONE,                                                                             
            timeout=1                                                                                                 
        )                                                                                                             
        print(f"Listening on {port} at 4800 baud... (Ctrl+C to quit)")                                                
                                                                                                                        
        while True:
            data = ser.readline()                                                                                     
            if data:
                print(data.decode("utf-8", errors="replace"), end="")
                                                                                                                        
    except serial.SerialException as e:
        print(f"Error: {e}", file=sys.stderr)                                                                         
        sys.exit(1)                                                                                                   
    except KeyboardInterrupt:
        print("\nStopped.")                                                                                           
    finally:    
        if "ser" in locals() and ser.is_open:                                                                         
            ser.close()                                                                                               
   
if __name__ == "__main__":                                                                                            
    main()      
