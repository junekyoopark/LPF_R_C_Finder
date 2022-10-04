import math

capacitor_list = [
    2,3,5,10,15,22,30,33,47,68,
    75,82,100,150,220,330,470,
    680,1000,1500,2200,3300,4700,6800,
    10000, 15000, 22000, 47000, 68000, 100000
    ]

capacitor_multiplier = 10**-12

resistor_list = [
    10, 100, 150, 220, 330, 470, 510,
    1000, 2000, 4700, 10000, 100000, 1000000, 10000000
]

f_cutoff_result_list = []

# f_cutoff_equation = 1/(2* math.pi * capacitance * resistance)
for capacitance in capacitor_list:
    for resistance in resistor_list:
        f_cutoff_result = 1/(2* math.pi * capacitance * capacitor_multiplier * resistance)
        f_cutoff_result_list.append(f_cutoff_result)

f_cutoff_goal = 250
f_cutoff_result_list.sort()

f_cutoff_best = min([i for i in f_cutoff_result_list if f_cutoff_goal < i])
print("Lowest possible cut-off frequency above cut-off frequency goal of " + str(f_cutoff_goal) + "Hz: " + str(f_cutoff_best) + "Hz")

for capacitance in capacitor_list:
    for resistance in resistor_list:
        if (1/(2* math.pi * capacitance * capacitor_multiplier * resistance)) == f_cutoff_best:
            print("Capacitance: " + str(capacitance) + "PF" + ", Resistance: " + str(resistance) + "Ohms")





