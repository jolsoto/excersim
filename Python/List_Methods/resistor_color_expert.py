'''
Introduction
If you want to build something using a Raspberry Pi, you'll probably use resistors. Like the previous Resistor Color Duo and Resistor Color Trio exercises, you will be translating resistor color bands to human-readable labels.

Each resistor has a resistance value.
Resistors are small - so small in fact that if you printed the resistance value on them, it would be hard to read. To get around this problem, manufacturers print color-coded bands onto the resistors to denote their resistance values.
Each band acts as a digit of a number. For example, if they printed a brown band (value 1) followed by a green band (value 5), it would translate to the number 15.
Instructions
In this exercise, you are going to create a helpful program so that you don't have to remember the values of the bands. The program will take 1, 4, or 5 colors as input, and outputs the correct value, in ohms. The color bands are encoded as follows:

Black: 0
Brown: 1
Red: 2
Orange: 3
Yellow: 4
Green: 5
Blue: 6
Violet: 7
Grey: 8
White: 9
In resistor-color trio you decoded the first three colors. For instance: orange-orange-brown translated to the main value 330. In this exercise you will need to add tolerance to the mix. Tolerance is the maximum amount that a value can be above or below the main value. For example, if the last band is green, the maximum tolerance will be ±0.5%.

The tolerance band will have one of these values:

Grey - 0.05%
Violet - 0.1%
Blue - 0.25%
Green - 0.5%
Brown - 1%
Red - 2%
Gold - 5%
Silver - 10%
The four-band resistor is built up like this:

Band_1	Band_2	Band_3	band_4
Value_1	Value_2	Multiplier	Tolerance
Meaning

orange-orange-brown-green would be 330 ohms with a ±0.5% tolerance.
orange-orange-red-grey would be 3300 ohms with ±0.05% tolerance.
The difference between a four and five-band resistor is that the five-band resistor has an extra band to indicate a more precise value.

Band_1	Band_2	Band_3	Band_4	band_5
Value_1	Value_2	Value_3	Multiplier	Tolerance
Meaning

orange-orange-orange-black-green would be 333 ohms with a ±0.5% tolerance.
orange-red-orange-blue-violet would be 323M ohms with a ±0.10 tolerance.
There are also one band resistors. One band resistors only have the color black with a value of 0.

This exercise is about translating the resistor band colors into a label:

"... ohms ...%"

So an input of "orange", "orange", "black", "green" should return:

"33 ohms ±0.5%"

When there are more than a thousand ohms, we say "kiloohms". That's similar to saying "kilometer" for 1000 meters, and "kilograms" for 1000 grams.

So an input of "orange", "orange", "orange", "grey" should return:

"33 kiloohms ±0.05%"

When there are more than a million ohms, we say "megaohms".

So an input of "orange", "orange", "blue", "red" should return:

"33 megaohms ±2%"
'''

color_list={'black':0,'brown':1,'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6,'violet': 7,'grey': 8,'white': 9}
tolerances={'grey':0.05,'violet':0.1,'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5,'silver': 10}
def resistor_label(colors):
    if len(colors)==1:
            return '0 ohms'
    else:
        values = [color_list[color] for color in colors[:-2]]
    
        multiplier_color=colors[-2]
        tolerance_color=colors[-1]
    
        main_value=int(''.join(map(str,values)))
        multiplier=10**color_list[multiplier_color]
    
        total=main_value*multiplier
    
        if total < 1000:
            unit = 'ohms'
        elif total < 1000000:
            total /= 1000
            unit = 'kiloohms'
        elif total < 1000000000:
            total /= 1000000
            unit = 'megaohms'
        else:
            total /= 1000000000
        
        tolerance=tolerances[tolerance_color]
        
        if total%1==0:
            return f'{int(total)} {unit} ±{tolerance}%'
        else:
            return f'{total} {unit} ±{tolerance}%'
