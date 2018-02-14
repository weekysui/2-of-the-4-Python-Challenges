import os, csv
employee_ID=[]
first_name = []
last_name = []
DOB=[]
SSN=[]
state=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
numbers = ['1','2']
for number in numbers:
    csvpath = os.path.join("raw_data","employee_data{}.csv".format(number))
    with open(csvpath,mode='r',newline='')as csvfile:
        next(csvfile, None)  # skip header
        csvreader=csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            employee_ID.append(row[0])
            name = row[1].split(' ')
            first_name.append(name[0])
            last_name.append(name[1])
            date = row[2].split('-')
            birthday = date[1]+"/"+date[2]+"/"+date[0]
            DOB.append(birthday)
            SSN.append('***-**-' + row[3].split('-')[2])
            for key in us_state_abbrev:
                if row[4]==key:
                    us_state = us_state_abbrev[key]
                    state.append(us_state)
        zipper = zip(employee_ID,first_name,last_name,DOB,SSN,state)
    output_path = os.path.join('raw_data','{}.csv'.format(number))
    with open(output_path,'w',newline="")as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        csvwriter.writerow(["Employee ID","First Name", "Last Name", "DOB","SSN", "State"])
        csvwriter.writerows(zipper)





