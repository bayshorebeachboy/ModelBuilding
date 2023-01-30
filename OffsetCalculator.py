import PySimpleGUI as sg

sg.theme('LightBlue3')   # Add a touch of color
layout = [  [sg.Text('Enter Station (Y)'), sg.InputText(size=(10, 10))],
            [sg.Text('Enter W.L./HT. (Z) '), sg.InputText(size=(10, 10))],
            [sg.Text('Enter Feet   '), sg.InputText(size=(10, 10)),],
            [sg.Text('Enter Inches'), sg.InputText(size=(10, 10)),],
            [sg.Text('Enter Eights'), sg.InputText(size=(10, 10))],
            [sg.Radio('Half Breaths', "RADIO1", default=True, key="-IN1-")],
            [sg.Radio('Heights', "RADIO1", default=False, key="-IN3-")],
            [[sg.Button('Add Record'),sg.Button('Cancel')]]
            
            ]
    
# Create the Window
window = sg.Window('Station by Offsets', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0], values[1],values[2], values[3],values[4])
    feet = float(values[2])
    inches = float(values[3])
    eights = float(values[4])
    print(feet, inches, eights) 
    inches8 = float(inches)*8 # number of 1/8's in Inches column
    print(inches8)
    eights = float(eights)
    print(eights)
    dec_ft = 8/(inches8 + eights)
    print(dec_ft)  
    print(feet+dec_ft)
    print('Populate Station')
    # populate record function
    print('X = ', feet+dec_ft)
    print('Y = ', values[0])
    print('Z = ', values[1])      


window.close()