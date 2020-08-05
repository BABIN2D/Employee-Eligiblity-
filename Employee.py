# ask user to provide input for age gender and physical disability.
# if anyone is above the age of 45 the work in urban areas, all female workers 
# work in urban areas, any disabled person work in urban areas rest 
# will work any location
# ask for qualification, the following are the criteria and accordingly
# the post offered to those criterias.
# 12 pass = peon
# graduate = clerk 
# pg- in MSC = R&D, M.COM = FINANCE, MCA = IT , MBA = Marketing / HR / FINANCE
# There are only the above posts available 
age = int(input('Enter Age\t'))
if 18 <= age <= 60:
    print('The following are the qualification and the post\noffered on those qualifications\nMSC\tR&D\nM.COM\tFINANCE\nMCA\tIT\nMBA\tMARKETING/FINANCE/HR\nGraduation\tClarical\n12 Pass\tPeon')
    qualification = input('Please enter your qualification\t')  
    if qualification in('MSC','M.COM','MCA','MBA','12 Pass','Graduate'):
        print('you are eligible for work ')
        if qualification == "MSC":
            print('Work available in R&D Department')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('Wrok in Urban Area')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working in Urban .\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
        if qualification == "M.COM":
            print('Work available in FINANCE Department')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('Wrok in Urban Area')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working for Urban location.\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
        if qualification == "MCA":
            print('Work available in IT Department')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('Wrok in Urban Area')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working for Urban location.\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
        if qualification == "MBA":
            print('Work available in FINANCE/MARKETING/HR Department')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('You are eligible for working for Urban location.\nCome down to our nearest branch of an interview session')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working for Urban location.\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
        if qualification == "Graduate":
            print('Work available in Clarical Department')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('Wrok in Urban Area')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working in Urban .\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
        if qualification == "12 Pass":
            print('Work available for Peon ')
            gender = input('Enter Gender\t')
            choice = input('Do you have any disability?\t')
            if choice in ('YES',"Yes",'y','yes','Y'):
                 print('Wrok in Urban Area')
            elif gender in('Female','FEMALE','F','f') or age >= 45:
                print('You are eligible for working in Urban .\nCome down to our nearest branch of an interview session')
            else:
                print('You are eligible for working in any location.\nCome down to our nearest branch of an interview session')
    else:
        print('No Work Available for"%s"qualification'%qualification)
else:
    print('You are not elligable for work')
