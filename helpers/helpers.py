import serial

def decide_color(input_data, Arduino_Serial):        
    if (input_data == 'red'):
        Arduino_Serial.write('#00001\n')

    if (input_data == 'blue'):
        Arduino_Serial.write('#00003\n')

    if (input_data == 'teal'):
        Arduino_Serial.write('#00006\n')
    
    if (input_data == 'lightblue'):
        Arduino_Serial.write('#00005\n')

    if (input_data == 'lightred'):
        Arduino_Serial.write('#00010\n')

    if (input_data == 'minty'):
        Arduino_Serial.write('#00007\n')

    if (input_data == 'purple'):
        Arduino_Serial.write('#00008\n')
    
    if (input_data == 'lightpurple'):
        Arduino_Serial.write('#00009\n')

    if (input_data == 'orange'):
        Arduino_Serial.write('#00010\n')

    if (input_data == 'green'):
        Arduino_Serial.write('#00002\n')

    if (input_data == 'lightgreen'):
        Arduino_Serial.write('#00012\n')
    
    if (input_data == 'seafoam'):
        Arduino_Serial.write('#00005\n')

def decide_palette(input_data, Arduino_Serial):        
    if (input_data == 'All'):
        Arduino_Serial.write('#PALLC\n')

    if (input_data == 'Aqua'):
        Arduino_Serial.write('#PAQUA\n')

    if (input_data == 'Reds'):
        Arduino_Serial.write('#PREDS\n')
    
    if (input_data == 'Blues'):
        Arduino_Serial.write('#PBLUS\n')
        
    if (input_data == 'White'):
        Arduino_Serial.write('#PWHNB\n')

def stop_color(Arduino_Serial):
    Arduino_Serial.write('#MSTOP\n')
