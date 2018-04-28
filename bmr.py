'''This is a BMR (Basic Metabolism Rate) calculator from Mifflin St Jeor'''
                   #''' coded by Screw '''
def get_info():
    try:
        mass = float(input('What\'s your weight in kg?: '))
        height = float(input('What\'s your height in cm?: '))
        age = int(input('How old are you?: '))
        individual = input('Are you Male of Female?: ')
        return {'mass':mass,'height':height,'age':age,'sex':individual}
    except ValueError:
        print('Can\'t take letters as input,Only numbers are accepted!')
        return False

def calculate_bmr(person_info):
        if person_info:
            mass = person_info['mass']
            height = person_info['height']
            age = person_info['age']
            individual = person_info['sex']
            if individual.lower() == 'male':
                bmr = (float(10)*float(mass) + float(6.25)*float(height) - int(5.0)*int(age) + 5)
                print('Your daily calorie expenditure is '+str(round(bmr)) + ' kcal per day')
                return bmr
            if individual.lower() == 'female':
                bmr = (float(10)*float(mass) + float(6.25)*float(height) - int(5.0)*int(age) - 161)
                print('Your daily calorie expenditure is ' +str(round(bmr)) + ' kcal per day')
                return bmr


person = get_info()
persons_bmr = calculate_bmr(person)
