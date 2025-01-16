import sys
from tabulate import tabulate
import matplotlib.pyplot as plt

def read_file(file_path):
    #Reads and returns lines from a file or prints an error if not found
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1) 

def parse_driver_info(lines):
    #Parses driver details into a dictionary.
    driver_details = {}
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 4:
            car_id, driver_code, driver_name, team_name = parts
            driver_details[driver_code] = {
                'car_id': car_id,
                'name': driver_name,
                'team': team_name
            }
        else:
            print(f"Warning: Invalid driver data in line: {line.strip()}")
    return driver_details

def parse_lap_data(lines):
    #Parses lap data and returns race venue and lap records
    race_venue = lines[0].strip()
    lap_records = {}
    for line in lines[1:]:
        driver_code = line[:3]
        try:
            lap_time = float(line[3:])
            lap_records.setdefault(driver_code, []).append(lap_time)
        except ValueError:
            print(f"Warning: Invalid lap time format in line: {line.strip()}")
    return race_venue, lap_records

def compute_average(times):
    """Computes the average of a list of times."""
    return sum(times) / len(times) if times else 0

def generate_report(driver_details, race_venue, lap_records):
    #Generates and displays the race performance report
    print(f"\nTrack Name: {race_venue}\n")

    # Find the fastest lap overall
    fastest_lap_data = min(
        [(code, min(laps)) for code, laps in lap_records.items()], key=lambda x: x[1]
    )
    best_driver_code, quickest_lap = fastest_lap_data
    best_driver_name = driver_details.get(best_driver_code, {}).get('name', best_driver_code)
    print(f"Fastest Lap Time: {quickest_lap:.3f} by {best_driver_name} ({best_driver_code})\n")

    # Compute overall average lap time
    all_lap_times = [time for laps in lap_records.values() for time in laps]
    overall_avg_time = compute_average(all_lap_times)
    print(f"Average Lap Time Overall: {overall_avg_time:.3f}\n")

    # Generate and display the driver Lap Time Analysis (Fastest & Average)
    table = [
        [
            idx + 1,
            driver_details.get(code, {}).get('name', code),
            code,
            driver_details.get(code, {}).get('team', 'Unknown'),
            f"{min(laps):.3f}",
            f"{compute_average(laps):.3f}"
        ]
        for idx, (code, laps) in enumerate(lap_records.items())
    ]
    print("Driver Lap Time Analysis (Fastest & Average):")
    print(tabulate(table, headers=["SN", "Driver", "Code", "Team", "Fastest Lap Time", "Average Lap Time"], tablefmt="heavy_grid"))
    print("\n")

    # Fastest lap times in descending order
    sorted_table = sorted(
        [(code, min(laps)) for code, laps in lap_records.items()], key=lambda x: x[1]
    )
    sorted_display = [
        [idx + 1, driver_details.get(code, {}).get('name', code), code, f"{time:.3f}"]
        for idx, (code, time) in enumerate(sorted_table)
    ]
    print("Fastest Lap Times in Descending Order:")
    print(tabulate(sorted_display, headers=["SN", "Driver", "Code", "Fastest Lap Time"], tablefmt="heavy_grid"))
    print("\n")

    # Plot lap times
    plot_lap_times(race_venue, lap_records)

# Bar chart
def plot_lap_times(race_venue, lap_records):
    #Plots the fastest and average lap times for each driver.
    driver_codes = list(lap_records.keys())
    fastest_times = [min(laps) for laps in lap_records.values()]
    average_times = [compute_average(laps) for laps in lap_records.values()]

    x = range(len(driver_codes))
    width = 0.35

    plt.bar([pos - width / 2 for pos in x], fastest_times, width=width, color='blue', label='Fastest Lap Time')
    plt.bar([pos + width / 2 for pos in x], average_times, width=width, color='deepskyblue', label='Average Lap Time')

    plt.xlabel('Driver Codes')
    plt.ylabel('Lap Time (s)')
    plt.title(f'Lap Time Analysis for {race_venue}')
    plt.xticks(x, driver_codes)
    plt.ylim(80, max(max(fastest_times), max(average_times)) + 10)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    if len(sys.argv) < 3:
        print("Usage: python f1.py <driver_info_file> <lap_times_file(s)>")
        sys.exit(1)  

    driver_info_file = sys.argv[1]
    lap_time_files = sys.argv[2:]

    driver_lines = read_file(driver_info_file)
    if not driver_lines:
        sys.exit(1)  

    driver_details = parse_driver_info(driver_lines)

    for lap_file in lap_time_files:
        print(f"Processing file: {lap_file}\n")
        lap_lines = read_file(lap_file)
        if not lap_lines:
            continue  

        race_venue, lap_records = parse_lap_data(lap_lines)
        if not lap_records:
            print(f"Warning: No lap records found in {lap_file}\n")
            continue  

        generate_report(driver_details, race_venue, lap_records)

if __name__ == "__main__":
    main()