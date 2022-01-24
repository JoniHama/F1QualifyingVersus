import requests
import sys
import statistics
import SortingData
from datetime import date


#Sorry for the lack of functions. It's my first project with Python and I learned as I went on.

startseason = 2003
season = 0
drivername = ""
driverposition = 0
driverQ3 = ""
driverQ2 = ""
driverQ1 = ""
teammate = []
teammateposition = 0
mateQ1 = ""
mateQ2 = ""
mateQ3 = ""
constructor = ""
qualitimes_ignored = {1: {'driver': '', 'teammate': '', 'teammatename': ''}}
qualitimes = {'driver': '0', "teammate": "0"}
qualitimestable = {1: {'driver': '', 'teammate': '', 'teammatename': ''}}
twothousandfive_quali = {'driver': '0', "teammate": "0", "driver2": "0", "teammate2": "0"}
qualidifference = {1: {'time': '', 'teammate': ''}}
qualitimeswithoutdata = {1: {'time': '', 'teammate': ''}}
endoftheseasondata = {0: {'year': '', 'time': '', 'teammate': ''}}
missedraces = 0
positionadd = 0
races = 0
checkraces = False

def ergast_retrieve(api_endpoint: str):
    url = f'https://ergast.com/api/f1/{api_endpoint}.json'
    response = requests.get(url).json()

    return response['MRData']
print("Staring season:")
startseason = int(input())
season = startseason
current_round = 1
print("Current round:")
current_round = int(input())

race = ergast_retrieve(f'{season}/{current_round}/qualifying')
results = race['RaceTable']['Races'][0]['QualifyingResults']


drivers = []

for c in range(len(results)):
    driver = results[c]['Driver']['driverId']
    drivers.append(driver)
print("Selectable drivers: ", drivers)

drivername = input(drivername)


while True:

    driverQ3 = ""
    driverQ2 = ""
    driverQ1 = ""
    mateQ1 = ""
    mateQ2 = ""
    mateQ3 = ""

    print("Current round ", current_round)
    print("Races ", races)
    print("Missed races ", missedraces)
    print("Season ", season)
    print("Start season ", startseason)

    qualitimes = {'driver': '0', "teammate": '0'}
    #race = ergast_retrieve(f'{season}/drivers/{drivername}/qualifying')
    race = ergast_retrieve(f'{season}/{current_round}/qualifying')
    driverseason = ergast_retrieve(f'{season}/drivers/{drivername}/qualifying')
    print("Total races this season", int(driverseason['total']))
    '''with open('output.json', 'w') as jsonFile:
        json.dump(int(driverseason['total']), jsonFile)'''

    if not checkraces:
        races = int(ergast_retrieve(f'{season}/races')['total'])
        checkraces = True

    print("Current round ", current_round)
    if not current_round > races:
        try:
            constructor = driverseason['RaceTable']['Races'][current_round-1-missedraces]['QualifyingResults'][0]['Constructor']['constructorId'] # result index starts at 0
        except IndexError:
            print(IndexError)

        results = race['RaceTable']['Races'][0]['QualifyingResults']

        if len(results) != 20:  # check the number of the drivers only season by season basis
            positionadd = len(results) - 20
            #print("positionadd ", positionadd)
        else:
            positionadd = 0

    print("Constructor ", constructor)




    #if not teammaterace['RaceTable']['Races']:
        #break
   #print(current_round)

    if not race['RaceTable']['Races']:
        print("Preparing next season")
        listofdrivers = []
        listoftimes = []
        listoftimes2 = []
        listoftimes3 = []

        for x, k in qualidifference.items(): # to-do: cleanup?
            #print(qualidifference[x])
            #print("listofdrivers ", listofdrivers)

            if qualidifference[x]['teammate'] not in listofdrivers:
                if (qualidifference[x]['teammate'] != ''):
                    listofdrivers.append(qualidifference[x]['teammate'])
                    if len(listofdrivers) == 1:
                        listoftimes.insert(0, qualidifference[x]['time'])
                    elif len(listofdrivers) == 2:
                        listoftimes2.insert(0, qualidifference[x]['time'])
                    elif len(listofdrivers) == 3:
                        listoftimes3.insert(0, qualidifference[x]['time'])
            else:
                if qualidifference[x]['teammate'] == listofdrivers[0]:
                    listoftimes.append(qualidifference[x]['time'])
                elif qualidifference[x]['teammate'] == listofdrivers[1]:
                    listoftimes2.append(qualidifference[x]['time'])
                elif qualidifference[x]['teammate'] == listofdrivers[2]:
                    listoftimes3.append(qualidifference[x]['time'])

        #print("Listoftimes after loop ", listoftimes)
        #print("listoftimes2", listoftimes2)
        #print("listoftimes3", listoftimes3)
        average = round(statistics.mean(float(n) for n in listoftimes if n), 3) # maybe exclude some results if they are clearly outliers
        #print(average)

        endoftheseasondata[0] = {}
        endoftheseasondata[0]['year'] = season
        endoftheseasondata[0]['time'] = average
        endoftheseasondata[0]['teammate'] = listofdrivers[0]


        if listoftimes2:
            endoftheseasondata[1] = {}

            average1 = round(statistics.mean(float(n) for n in listoftimes2 if n), 3)

            endoftheseasondata[1]['year'] = season
            endoftheseasondata[1]['time'] = average1
            endoftheseasondata[1]['teammate'] = listofdrivers[1]
        if listoftimes3:
            endoftheseasondata[2] = {}

            average2 = round(statistics.mean(float(n) for n in listoftimes3 if n), 3)

            endoftheseasondata[2]['year'] = season
            endoftheseasondata[2]['time'] = average2
            endoftheseasondata[2]['teammate'] = listofdrivers[2]

        season += 1
        SortingData.create_column(season, races, qualitimestable, qualidifference, endoftheseasondata,drivername, missedraces, qualitimes_ignored)
        current_round = 1
        try:
            print("Trying next season")
            qualitimes_ignored = {1: {'driver': '', 'teammate': '', 'teammatename': ''}}
            qualitimes = {'driver': '0', "teammate": "0"}
            qualitimestable = {1: {'driver': '', 'teammate': '', 'teammatename': ''}}
            twothousandfive_quali = {'driver': '0', "teammate": "0", "driver2": "0", "teammate2": "0"}
            qualidifference = {1: {'time': '', 'teammate': ''}}
            qualitimeswithoutdata = {
                1: {'time': '', 'teammate': ''}}
            endoftheseasondata = {0: {'year': '', 'time': '', 'teammate': ''}}
            qualidifference = {1: {'time': '', 'teammate': ''}}
            teammateposition = 0
            missedraces = 0
            positionadd = 0
            races = 0

            if not checkraces:
                races = int(ergast_retrieve(f'{season}/races')['total'])
                checkraces = True

            driverseason = ergast_retrieve(f'{season}/drivers/{drivername}/qualifying')

            if int(driverseason['total']) == 0:
                retired = True
                print("Driver not driving next season!")
                print("Let's check if he hasn't retired from F1 yet")
                for k in range((date.today().year - season)):
                    a = ergast_retrieve(f'{season+k}/drivers/{drivername}/qualifying')
                    print("k loop")
                    if(int(a['total']) != 0):
                        season = season+k
                        print(season)
                        checkraces = False
                        if len(results) != 20:  # check the number of the drivers only season by season basis
                            positionadd = len(results) - 20

                            if positionadd < 0:
                                positionadd = 0
                        else:
                            positionadd = 0
                        race = ergast_retrieve(f'{season}/{current_round}/qualifying')
                        results = race['RaceTable']['Races'][0]['QualifyingResults']
                        driverseason = ergast_retrieve(f'{season}/drivers/{drivername}/qualifying')
                        constructor = driverseason['RaceTable']['Races'][current_round - missedraces - 1]['QualifyingResults'][0]['Constructor']['constructorId']
                        current_round = 1
                        missedraces = 0
                        teammate = []
                        retired = False
                        break
                if retired:
                    sys.exit()
            else:
                checkraces = False
                if len(results) != 20:  # check the number of the drivers only season by season basis
                    positionadd = len(results) - 20

                    if positionadd < 0:
                        positionadd = 0
                else:
                    positionadd = 0
                current_round = 1
                race = ergast_retrieve(f'{season}/{current_round}/qualifying')
                results = race['RaceTable']['Races'][0]['QualifyingResults']
                constructor = driverseason['RaceTable']['Races'][current_round - missedraces - 1]['QualifyingResults'][0]['Constructor']['constructorId']
                missedraces = 0
                teammate = []
                print("Season ", season)
        except IndexError:
            print("Next season not possible")
            sys.exit
    #teammateresults = teammaterace['RaceTable']['Races'][0]['QualifyingResults']

    results = race['RaceTable']['Races'][0]['QualifyingResults']

    for j in range(len(results)):
        driver = results[j]['Driver']['driverId']
        position = int(results[j]['position'])
        team = results[j]['Constructor']['constructorId']
        #print("teammateposition ", teammateposition)
        #print("MateQ3 ", mateQ3)
        if team == constructor:
            print(position)
            if driver == drivername:
                if season == 2003 or season == 2004 or season == 2005 and current_round >= 7:
                    #print("Season ", season, " säännöt")
                    qualitimes['driver'] = results[j]['Q1']
                    driverposition = int(results[j]['position'])
                    if (qualitimes['teammate'] != '0'):
                        break
                    else:
                        continue
                elif season == 2005 and current_round < 7:
                    twothousandfive_quali['driver'] = results[j]['Q1']
                    twothousandfive_quali['driver2'] = results[j]['Q2']
                else:
                    if position <= 10 and position != 0:
                        try:
                            qualitimes['driver'] = results[j]['Q3']
                            driverQ3 = results[j]['Q3']
                        except KeyError:
                            driverQ3 = results[j]['Q2']
                            qualitimes['driver'] = results[j]['Q2']

                        driverQ2 = results[j]['Q2']
                        driverQ1 = results[j]['Q1']
                        driverposition = int(results[j]['position'])
                        if (qualitimes['teammate'] != '0'):
                            if (15 + (positionadd/2)) >= teammateposition >= 10 or not mateQ3:
                                qualitimes['driver'] = driverQ2

                            if teammateposition >= (15 + (positionadd/2)):
                                qualitimes['driver'] = driverQ1

                            break
                        else:
                            continue
                    if (15 + (positionadd/2)) >= position >= 10:
                        try:
                            qualitimes['driver'] = results[j]['Q2']
                            driverQ2 = results[j]['Q2']
                        except KeyError:
                            qualitimes['driver'] = results[j]['Q1']
                        driverQ1 = results[j]['Q1']
                        driverposition = int(results[j]['position'])
                        if qualitimes['teammate'] != '0':

                            #Q2
                            if (15 + (positionadd/2)) >= driverposition >= 10 and driverQ2:
                                qualitimes['teammate'] = mateQ2

                            #Q1
                            if driverposition > (15 + (positionadd/2)) or not driverQ2 and not driverQ3:
                                qualitimes['teammate'] = mateQ1

                            if teammateposition >= (15 + (positionadd/2)):
                                qualitimes['driver'] = driverQ1

                            break
                        else:
                            continue
                    if position > (15 + (positionadd/2)):
                        #print("over 15")
                        driverQ1 = results[j]['Q1']
                        qualitimes['driver'] = results[j]['Q1']
                        driverposition = int(results[j]['position'])
                        if (qualitimes['teammate'] != '0'):
                            #Q2
                            if (15 + (positionadd/2)) >= driverposition >= 10:
                                qualitimes['teammate'] = mateQ2
                            #Q1
                            if driverposition > (15 + (positionadd/2)):
                                qualitimes['teammate'] = mateQ1

                            break
                        else:
                            print("continue")
                            continue
            else:
                teammate = driver
                teammateposition = int(results[j]['position'])
                print("Teammmate ", teammate)
                if season == 2003 or season == 2004 or season == 2005 and current_round >= 7:
                    qualitimes['teammate'] = results[j]['Q1']
                    teammateposition = int(results[j]['position'])
                    if (qualitimes['driver'] != '0'):
                        break
                    else:
                        continue
                elif season == 2005 and current_round < 7:
                    twothousandfive_quali['teammate'] = results[j]['Q1']
                    try:
                        twothousandfive_quali['teammate2'] = results[j]['Q2']
                    except Exception as ex:
                        twothousandfive_quali['teammate2'] = "0"
                else:
                    if position <= 10 and position != 0:
                        try:
                            qualitimes['teammate'] = results[j]['Q3']
                            mateQ3 = results[j]['Q3']
                        except KeyError:
                            mateQ3 = results[j]['Q2']
                            qualitimes['teammate'] = mateQ3

                        mateQ2 = results[j]['Q2']
                        mateQ1 = results[j]['Q1']
                        teammateposition = int(results[j]['position'])
                        if (qualitimes['driver'] != '0'):

                            if (15 + (positionadd/2)) >= driverposition >= 10:
                                qualitimes['teammate'] = mateQ2

                            if driverposition > (15 + (positionadd/2)):
                                qualitimes['teammate'] = mateQ1

                            if mateQ3 == mateQ2:
                                qualitimes['driver'] = driverQ2

                            break
                        else:
                            continue
                    if (15 + (positionadd/2)) >= position > 10:
                        try:
                            qualitimes['teammate'] = results[j]['Q2']
                            mateQ2 = results[j]['Q2']
                        except Exception:
                            qualitimes['teammate'] = results[j]['Q1']
                        mateQ1 = results[j]['Q1']
                        teammateposition = int(results[j]['position'])
                        if (qualitimes['driver'] != '0'):
                            #Q2
                            if 15 + (positionadd/2) >= teammateposition >= 10 or mateQ3:
                                if mateQ2 == "":
                                    qualitimes['driver'] = driverQ1
                                else:
                                    qualitimes['driver'] = driverQ2

                            #Q1
                            if driverposition > (15 + (positionadd/2)):
                                qualitimes['teammate'] = mateQ1

                            if teammateposition > (15 + (positionadd/2)):
                                qualitimes['driver'] = driverQ1

                            break
                        else:
                            continue
                    if position > (15+(positionadd/2)):
                        qualitimes['teammate'] = results[j]['Q1']
                        mateQ1 = results[j]['Q1']
                        teammateposition = int(results[j]['position'])
                        if (qualitimes['driver'] != '0'):

                            if (15 + (positionadd/2)) >= teammateposition >= 10:
                                qualitimes['driver'] = driverQ2
                            #Q1
                            if driverposition > (15 + (positionadd/2)):
                                qualitimes['teammate'] = mateQ1

                            if teammateposition > (15 + (positionadd/2)):
                                qualitimes['driver'] = driverQ1
                            break
                        else:
                            continue

    #if not qualitimes['teammate'] or qualitimes['teammate'] == 0 or qualitimes['teammate'] == "0":
        #if mateQ2:
            #qualitimes['teammate'] = mateQ2
        #elif mateQ1:
           #qualitimes['teammate'] = mateQ1

    print(qualitimes['driver'])
    print(qualitimes['teammate'])

    if qualitimes['driver'] != "" and qualitimes['teammate'] != "" and qualitimes['driver'] != '0' and qualitimes['teammate'] != '0' and qualitimes['teammate'] != 0 or season == 2005 and current_round < 7 and twothousandfive_quali['teammate'] != "0" and twothousandfive_quali['teammate2'] != "0":
        #print("2005 ", twothousandfive_quali)
        if season != 2005:
            a = qualitimes['driver'].split(':')
            b = qualitimes['teammate'].split(':')
        elif current_round < 7:
            a = twothousandfive_quali['driver'].split(':')
            b = twothousandfive_quali['teammate'].split(':')
            o = twothousandfive_quali['driver2'].split(':')
            p = twothousandfive_quali['teammate2'].split(':')
        else:
            a = qualitimes['driver'].split(':')
            b = qualitimes['teammate'].split(':')

        c = int(a[0]) * 60
        d = float(a[1])
        e = (c + d)

        f = int(b[0]) * 60
        g = float(b[1])
        h = (f + g)

        if season == 2005 and current_round < 7:
            q = int(o[0]) * 60
            r = float(o[1])
            s = (q + r)

            t = int(p[0]) * 60
            u = float(p[1])
            v = (t + u)

        #print(qualitimes['driver'] < qualitimes['teammate'])

        if season != 2005 or season == 2005 and current_round >= 7:
            if 5 > e-h > -5: # remove the results where the gap isn't most likely dictated by speed
                if current_round != 1:
                    qualitimestable[current_round] = {}

                qualitimestable[current_round]['driver'] = qualitimes['driver']
                qualitimestable[current_round]['teammate'] = qualitimes['teammate']
                qualitimestable[current_round]['teammatename'] = teammate

                if current_round != 1:
                    qualidifference[current_round] = {}

                qualidifference[current_round]['time'] = round(e - h, 3)
                qualidifference[current_round]['teammate'] = teammate
            else:
                if current_round != 1:
                    qualitimes_ignored[current_round] = {}

                qualitimes_ignored[current_round]['driver'] = qualitimes['driver']
                qualitimes_ignored[current_round]['teammate'] = qualitimes['teammate']
                qualitimes_ignored[current_round]['teammatename'] = teammate

                if qualitimes['driver'] == "":
                    qualitimes_ignored[current_round]['driver'] = "no time"

                if qualitimes['teammate'] == "":
                    qualitimes_ignored[current_round]['teammate'] = "no time"
        else:
            if 5 > ((e - h) + (s - v)) > -5:
                if current_round != 1:
                    qualitimestable[current_round] = {}

                qualitimestable[current_round]['driver'] = qualitimes['driver']
                qualitimestable[current_round]['teammate'] = qualitimes['teammate']
                qualitimestable[current_round]['teammatename'] = teammate

                if current_round != 1:
                    qualidifference[current_round] = {}

                qualidifference[current_round]['time'] = round((e - h) + (s - v), 3)
                qualidifference[current_round]['teammate'] = teammate
            else:
                if current_round != 1:
                    qualitimes_ignored[current_round] = {}

                qualitimes_ignored[current_round]['driver'] = qualitimes['driver']
                qualitimes_ignored[current_round]['teammate'] = qualitimes['teammate']
                qualitimes_ignored[current_round]['teammatename'] = teammate

                if qualitimes['driver'] == "":
                    qualitimes_ignored[current_round]['driver'] = "no time"

                if qualitimes['teammate'] == "":
                    qualitimes_ignored[current_round]['teammate'] = "no time"

        #qualidifference.append(round(e - h, 3))
        #print(qualidifference)
    elif qualitimes['driver'] == '0' or not qualitimes['driver'] and season != 2005:
        missedraces += 1 # only if selected driver didn't enter the qualifying

        if current_round != 1:
            qualitimes_ignored[current_round] = {}

        qualitimes_ignored[current_round]['driver'] = qualitimes['driver']
        qualitimes_ignored[current_round]['teammate'] = qualitimes['teammate']
        qualitimes_ignored[current_round]['teammatename'] = teammate

        if qualitimes['driver'] == "":
            qualitimes_ignored[current_round]['driver'] = "no time"

        if qualitimes['teammate'] == "":
            qualitimes_ignored[current_round]['teammate'] = "no time"
    else:
        if current_round != 1:
            qualitimes_ignored[current_round] = {}

        qualitimes_ignored[current_round]['driver'] = qualitimes['driver']
        qualitimes_ignored[current_round]['teammate'] = qualitimes['teammate']
        qualitimes_ignored[current_round]['teammatename'] = teammate

        if qualitimes['driver'] == "":
            qualitimes_ignored[current_round]['driver'] = "no time"

        if qualitimes['teammate'] == "":
            qualitimes_ignored[current_round]['teammate'] = "no time"

    qualitimes.clear()
    twothousandfive_quali.clear()

    current_round += 1