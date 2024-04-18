w = float( input('Enter weight in kg:') )
h = float( input('Enter height in cm:') )
hm = h/100

bmi = w / hm**2
bmi =round(bmi, 2)

print(f'BMI={bmi}') 
 

if bmi<16.0:
    print ('Underweight (Severe thinness)')

if 16.0<=bmi<=16.9:
    print ('Underweight (Moderate thinness)')

if 17.0<=bmi<=18.4:
    print ('Underweight (Mild thinness)')

if 18.5<=bmi<=24.9:
    print ('Normal range')

if 25.0<=bmi<=29.9:
    print ('Overweight (Pre-obese)')

if 30.0<=bmi<=34.9:
    print ('Obese (Class I)')

if 35.0<=bmi<=39.9:
    print ('Obese (Class II)')

if bmi>=40.0:
    print ('Obese (Class III)')