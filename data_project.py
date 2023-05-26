from sqlalchemy import create_engine
import sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker
from create_table import Person
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


Base = sqlalchemy.orm.declarative_base()

# <editor-fold desc="Login details">
url = 'mysql+mysqlconnector://root:password@localhost:3317/duomenu_baze' #  password changed
engine = create_engine(url, echo=True)
# </editor-fold>
connection = engine.connect()
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
pasirinkimas = 0
while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti asmenis \n2 - įvesti naują asmenį \n3 - atnaujinti asmenį \n4 - ištrinti asmenį \n5 - atvaizduoti grafiku \n6 - išeiti iš aplikacijos     "))
    if pasirinkimas == 1:
        all_data = session.query(Person).all()
        # print(all_data)
        columns1 = ['id', 'first_name', 'last_name', 'race', 'age', 'Creation_date']
        data = [(i.id, i.first_name, i.last_name, i.race, i.age, i.created_date) for i in all_data]
        df = pd.DataFrame(data=data, columns=columns1)
        print(df)


    elif pasirinkimas == 2:
        first_name = input('Įveskite žmogaus vardą: ')
        last_name = input('Įveskite žmogaus pavardę: ')
        race = input('Įveskite žmogaus rasę: ')
        age = input('Įveskite žmogaus amžių: ')
        person1 = Person(first_name, last_name, race, age)
        session.add(person1)
        session.commit()

    elif pasirinkimas == 3:
        while True:
            zmones = session.query(Person).all()
            print("-------------------")
            for i in zmones:
                print(i," \n ")
            print("-------------------")
            try:
                keiciamo_id = int(input("enter id of row You want to change: "))
                print(keiciamo_id)
                keitimas = int(input("Enter changeable column: 1 - first_name ; 2 - last_name; 3 - race; 4- age:"))
                if keitimas == 1:
                    print("all good")
                    new_name = input("Enter a new first name: ")
                    session.query(Person).filter_by(id=keiciamo_id).update({Person.first_name: new_name})
                    session.commit()
                    break
                elif keitimas == 2:
                    print("all good")
                    new_name = input("Enter a new last name: ")
                    session.query(Person).filter_by(id=keiciamo_id).update({Person.last_name: new_name})
                    session.commit()
                    break
                elif keitimas == 3:
                    print("all good")
                    new_race = input("Enter a new race: ")
                    session.query(Person).filter_by(id=keiciamo_id).update({Person.last_name: new_race})
                    session.commit()
                    break
                elif keitimas == 4:
                    print("all good")
                    new_age = input("Enter a new age: ")
                    session.query(Person).filter_by(id=keiciamo_id).update({Person.last_name: new_age})
                    session.commit()
                    break
            except:
                print("You entered wrong values, try again ")

    elif pasirinkimas == 4:
        zmones = session.query(Person).all()
        print("                       ")
        for i in zmones:
            print(i, " \n ")
        #print("                       ")
        deleted_row=int(input("enter id of row You want to delete: "))
        person1 = session.query(Person).filter(Person.id == deleted_row).delete()


    elif pasirinkimas == 5:

        all_data = session.query(Person).all()
        # print(all_data)
        columns1 = ['id', 'first_name', 'last_name', 'race', 'age', 'Creation_date']
        data = [(i.id, i.first_name, i.last_name, i.race, i.age, i.created_date) for i in all_data]
        df = pd.DataFrame(data=data, columns=columns1)
        # print(df)

        ########## dalyviu amziaus grafikai #######3

        while True:
            try:
                print('grafiką darom su matplotlib ar seaborn?')
                kuris_grafikas = int(input('1 = matplotlib, o 2 =  seaborn'))
                if kuris_grafikas==1:
                    plt.plot(df.first_name, df.age)
                    plt.legend(['Dalyvių amžius'])
                    plt.xlabel('Dalyviai')
                    plt.ylabel('Amžius')
                    plt.grid(True, color='green', linewidth=0.5, linestyle='--')
                    plt.show()
                    break

                elif kuris_grafikas==2:
                    sns.set_style('white')
                    sns.barplot(x='age', y='first_name', data=df)
                    sns.despine()
                    plt.show()
                    break

            except:
                print('grafiką darom su matplotlib ar seaborn?')
                kuris_grafikas = int(input('1 = matplotlib, o 2 =  seaborn'))



    elif pasirinkimas == 6:
        break





