'''
Carson Harbin
Programming Exercise 13
This program propts the user to choose one of 10 cities and then displays the population growth for the city chosen.
'''

import sqlite3
import matplotlib.pyplot as plt


#Function 1: Create the database, table, and insert 2023 data
def create_database():
    conn = sqlite3.connect('population_CH.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    #10 Florida cities with sample populations (2023 estimates)
    cities = {
        'Miami': 449514,
        'Orlando': 316081,
        'Tampa': 407599,
        'Jacksonville': 971319,
        'Tallahassee': 201731,
        'St. Petersburg': 261256,
        'Fort Lauderdale': 183445,
        'Hialeah': 221673,
        'Port St. Lucie': 236400,
        'Cape Coral': 222343
    }
    #Insert 2023 data
    for city, population in cities.items():
        c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)',
                  (city, 2023, population))
    conn.commit()
    conn.close()


#Function 2: Simulate 20 years of 2% population growth
def simulate_population_growth():
    conn = sqlite3.connect('population_CH.db')
    c = conn.cursor()

    #Get 2023 data
    c.execute('SELECT city, population FROM population WHERE year = 2023')
    rows = c.fetchall()

    #For each city, simulate 20 years
    for city, pop in rows:
        current_pop = pop
        for year in range(2024, 2024 + 20):
            current_pop = int(current_pop * 1.02)  # 2% increase
            c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)',
                      (city, year, current_pop))

    conn.commit()
    conn.close()


#Function 3: Let user pick a city and plot its population growth
def plot_population_growth():
    conn = sqlite3.connect('population_CH.db')
    c = conn.cursor()

    #Get list of cities
    c.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in c.fetchall()]

    print("Choose a city from the following list:")
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city}")

    choice = int(input("Enter the number corresponding to your choice: "))
    if choice < 1 or choice > len(cities):
        print("Invalid choice.")
        return
    selected_city = cities[choice - 1]

    #Get population data for the selected city
    c.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
    data = c.fetchall()
    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    #Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth of {selected_city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

    conn.close()

if __name__ == "__main__":
    create_database()
    simulate_population_growth()
    plot_population_growth()
