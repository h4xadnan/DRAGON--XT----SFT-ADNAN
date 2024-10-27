import getpass
import os
import time
from binance.client import Client
from random import choice
from colorama import Fore, Style, init
from datetime import datetime, timedelta
import urllib3
import warnings

# Suppress only the InsecureRequestWarning from urllib3
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# User's Gmail and Password
correct_email = "h4xadnanlr@1secmail.com"
correct_password = "h4x_dr@gon"

# Binance API setup
api_key = '54i4y3jK3wqnRlZ6n2t4isgcHrhSTAjHFOHk7zZLvqU8DpvbpND3yR6YkAVjmFKe'
api_secret = '20A8irk55nARO9FKiPxXpmYAfp9riEZLlV6ZeutaATy8AJ6ZtaGHnSZRt27OYFTH'

# Initialize Binance client with API keys
client = Client(api_key, api_secret, {"timeout": 60})

# Disable SSL verification by modifying the session after client initialization
client.session.verify = False

# Expanded trading pairs including USDNGN
pairs = [
    'EURUSD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDZAR', 'Pfizer inc', 'Microsoft', 'USDIDR', 'USDCAD', 'USDPHP', 'GBPUSD', 'USDPKR', 'USDTRY', 'USDDZD', 'USDMXN', 'USDEGP',
    'USDINR', 'USCrude', 'UKBrent', 'Silver', 'Gold', 'USDCOP', 'EURJPY', 'EURGBP', 'AUDUSD', 'CADJPY', 'USDARS',
    'Bitcoin', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF', 'EURNZD', 'EURSGD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'USDBDT', 'FACEBOOK-INC', 'Johnson', 'AEXP', 'INTEL', 'USDCHF', 'USDBRL', 'CADCHF', 'USDCAD', 'McDonalds', 'AUDUSD', 'BNBBTC',
    'ETHBTC', 'USDJPY', 'USDNGN'
]

# Step 1: User Login
def login():
    print(Style.BRIGHT + Fore.GREEN + "Welcome..! Please log in DRAGON..!")
    email = input(Style.BRIGHT + Fore.YELLOW + "Enter your Token ID: ")
    password = getpass.getpass(Style.BRIGHT + Fore.YELLOW + "Enter Your Password: ")

    # Check for correct email and password
    if email == correct_email and password == correct_password:
        print(Style.BRIGHT + Fore.GREEN + "Login successful!")
        time.sleep(1)
    else:
        print(Style.BRIGHT + Fore.RED + "Login failed! Exiting...")
        exit()

# Step 2: Clear screen after login
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Step 3: Banner Design and Input Prompt
def show_banner():
    print(Fore.RED + """

       ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗
       ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║
       ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║
       ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║
       ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║
       ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝
    """)
    print(Fore.CYAN + Style.BRIGHT + "﴾◀═══════>> DRAGON 𖤍 IS MOST POWERFUL 𖤍 SOFTWARE <<═══════➤﴿")
    print(Fore.CYAN + Style.BRIGHT + "﴾◀═════════════════>> DRAGON - XT v4.05 <<════════════════➤﴿")
    print(Fore.CYAN + Style.BRIGHT + "﴾◀══════════════>> TELEGRAM: @Ittzsowmick <<═════════════➤﴿")
    print(Fore.CYAN + Style.BRIGHT + "﴾◀═══════════════>> DEVELOPER ―‣ ADNAN'〆 <<══════════════➤﴿")


from datetime import datetime, timedelta
from random import choice
from colorama import Fore, Style

# Sample pairs, replace this with your actual pairs
pairs = ['EURUSD', 'USDJPY', 'Bitcoin', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'AUDUSD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURCAD', 'EURCHF', 'EURSGD', 'GBPAUD', 'GBPCHF', 'GBPNZD', 'GBPCAD', 'NZDCAD', 'NZDJPY', 'NZDCHF', 'NZDUSD', 'USDZAR', 'Pfizer inc', 'Microsoft', 'McDonalds', 'Bitcoin', 'GBPJPY', 'EURNZD', 'EURGBP', 'USDIDR', 'USDCAD', 'USDPHP',  'USDMXN', 'USDNGN', 'USDTRY', 'FACEBOOK-INC', 'INTEL', 'Johnson', 'AEXP', 'UKBrent', 'USCrude', 'Silver', 'USDPKR', 'USDBRL', 'USDBDT', 'USDINR', 'USDEGP', 'USDDZD', 'USDCOP', 'USDARS']

def get_user_input():
    print("\n\n")

    selected_pairs = input(Style.BRIGHT + Fore.BLUE + "[•] TYPE YOUR CURRENCY NAME: ").split(",")
    selected_pairs = [pair.strip() for pair in selected_pairs if pair.strip() in pairs]

    if not selected_pairs:
        print(Style.BRIGHT + Fore.RED + f"Invalid pair selected. Please choose from {pairs}")
        exit()

    martingale_count = input(Style.BRIGHT + Fore.CYAN + "[•] HOW MANY MARTINGALE DO YOU NEED?: ")
    day_analysis = input(Style.BRIGHT + Fore.WHITE + "[•] DAY ANALYSIS: ")
    min_percentage = input(Style.BRIGHT + Fore.RED + "[•] MINIMUM PERCENTAGE: ")
    max_percentage = input(Style.BRIGHT + Fore.GREEN + "[•] MAXIMUM PERCENTAGE: ")

    # Get signal type from user
    signal_type = input(Style.BRIGHT + Fore.YELLOW + "[•] SELECT SIGNAL TYPE (CALL/PUT/BOTH): ").strip().upper()
    while signal_type not in ['CALL', 'PUT', 'BOTH']:
        print(Style.BRIGHT + Fore.RED + "Invalid selection. Please choose CALL, PUT, or BOTH.")
        signal_type = input(Style.BRIGHT + Fore.CYAN + "[•] SELECT SIGNAL TYPE (CALL/PUT/BOTH): ").strip().upper()

    start_time = input(Style.BRIGHT + Fore.GREEN + "[•] START OF THE LIST (HH:MM): ")
    end_time = input(Style.BRIGHT + Fore.RED + "[•] END OF THE LIST (HH:MM): ")

    # Return all values including signal type
    return (selected_pairs, martingale_count, day_analysis, min_percentage, max_percentage, signal_type, start_time, end_time)

# Step 4: Signal Generation
from random import choice
from datetime import datetime, timedelta

def generate_signal(selected_pairs, start_time, end_time, signal_type='BOTH'):
    signals = {pair: [] for pair in selected_pairs}  # Dictionary to hold signals for each pair
    current_time = datetime.now() + timedelta(minutes=1)  # Start generating signals from 1 minute in the future

    # Convert start and end times to datetime objects
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    start_time_dt = current_time.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    end_time_dt = current_time.replace(hour=end_hour, minute=end_minute, second=59, microsecond=999999)

    # Ensure start time is before end time
    if start_time_dt >= end_time_dt:
        print("Start time must be before end time.")
        return []
    # Define the pairs that should be in OTC format
    otc_pairs = ['USDBDT', 'EURUSD', 'USDJPY', 'GBPUSD', 'USDCAD', 'USDCHF', 'EURGBP', 'EURJPY', 'USDBRL', 'USDNGN', 'USDMXN', 'USDPKR',
                 'USDTRY', 'UKBrent', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD',
                 'EURCAD', 'EURCHF', 'EURSGD', 'EURNZD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'NZDCAD',
                 'NZDUSD', 'NZDCHF', 'NZDJPY', 'USDZAR', 'McDonalds', 'Microsoft', 'Pfizer inc', 'USDIDR', 'USCrude',
                 'Silver', 'Gold', 'FACEBOOK-INC', 'Bitcoin', 'INTEL', 'AEXP', 'Johnson', 'USDCOP', 'USDDZD',
                 'USDPHP', 'USDEGP', 'USDARS', 'USDINR']

    # Define time intervals in minutes
    time_intervals = [5, 9, 13, 24, 32, 43, 57]  # in minutes

    # Initialize a different signal time for each pair
    signal_times = {pair: start_time_dt for pair in selected_pairs}

    # Determine actions based on user selection
    actions = []
    if signal_type == 'CALL':
        actions = ['CALL']  # Only generate CALL signals
    elif signal_type == 'PUT':
        actions = ['PUT']  # Only generate PUT signals
    elif signal_type == 'BOTH':
        actions = ['CALL', 'PUT']  # Generate both CALL and PUT signals

    # Start generating signals for each pair
    while any(signal_time <= end_time_dt for signal_time in signal_times.values()):
        for pair in selected_pairs:
            signal_time = signal_times[pair]

            if signal_time > end_time_dt:
                continue  # Skip this pair if its signal time exceeds the end time

            # Generate action based on signal_type (CALL, PUT, or BOTH)
            action = actions[0] if len(actions) == 1 else choice(actions)  # Only one action if CALL or PUT, random if BOTH

            # Format signal with color based on whether it's a call or put
            if action == 'CALL':
                color = "\033[92m"  # Green for call signals
            else:
                color = "\033[91m"  # Red for put signals

            # Format signal based on whether the pair is OTC or not
            if pair in otc_pairs:
                signals[pair].append(f"{color}{signal_time.strftime('%H:%M')} /~ {pair}-OTC - {action}\033[0m")
            else:
                signals[pair].append(f"{color}{signal_time.strftime('%H:%M')} /~ {pair} - {action}\033[0m")

            # Add a random interval for the next signal for this specific pair
            interval = choice(time_intervals)  # Choose a random interval
            signal_times[pair] += timedelta(minutes=interval)

    # Create a flat list of signals
    output_signals = []
    for pair in selected_pairs:
        output_signals.append(f"\033[1;37m=========================\033[0m")  # Bold and white line before each pair
        output_signals.extend(signals[pair])  # Add signals for each pair to the output list
        output_signals.append(f"\033[1;37m=========================\033[0m")  # Bold and white line after each pair
        output_signals.append("")  # Add an empty line after each pair's signals for better readability

    return output_signals  # Return the generated signals

# Step 5: Signal Filtering (removed for no filtering)
def filter_signals(signals):
    return signals  # Return all signals without filtering
# Step 6: Display Signals                       
from colorama import Fore, Style

# Define the function to display signals
def display_signals(signals):
    print(" " + Fore.GREEN + Style.BRIGHT + "GENERATED   DRAGON   SIGNAL'S...")
    print("=" * 50)
    print("\n")

    for signal in signals:
        print("        " + Fore.LIGHTRED_EX + signal)  # Align signals to the right

    print("=" * 50)
    print("\n")  # Space after signals

    finished_message = Fore.LIGHTYELLOW_EX + Style.BRIGHT + " {====== FINISHED SINAI'S ======}"
    print(finished_message)  # Print the finished message

    print("\n")
    print("             " + Style.BRIGHT + Fore.CYAN + "𖤍 DRAGON 𖤍 v4.05")  # Ensure this line is consistently indented

# Example function for your main logic
def main():
    # Assuming signals are generated somewhere in your code
    signals = ["signal1", "signal2", "signal3"]  # Example signals
    filtered_signals = signals  # Replace with your actual filtering logic

    # Call the display_signals function to show the signals
    display_signals(filtered_signals)

# Call the main function to run the program
if __name__ == "__main__":
    main()
  
# Step 7: Copying Signals
def copy_signals(signals):
    # Join all signals into a single string separated by new lines
    signal_text = "\n".join(signals)
    # Copying to clipboard (you may need to install 'pyperclip')
    try:
        import pyperclip
        pyperclip.copy(signal_text)
        print(Style.BRIGHT + Fore.GREEN + "Signals copied to clipboard!")
    except ImportError:
        print(Style.BRIGHT + Fore.RED + "pyperclip is not installed. Please install it to use this feature.")

# Step 8: Main Program Flow
def main():
    login()
    clear_screen()
    show_banner()

    # Get user input for selected pairs and other parameters
    selected_pairs, martingale_count, day_analysis, min_percentage, max_percentage, detection, start_time, end_time = get_user_input()

    print("\n")
    print(" " + Style.BRIGHT + Fore.GREEN + "GENERATING 𖤍 DRAGON 𖤍 SIGNAL'S...")
    signals = generate_signal(selected_pairs, start_time, end_time)  # Pass start and end time
    filtered_signals = filter_signals(signals)  # No filtering applied now

    if not filtered_signals:
        print(Style.BRIGHT + Fore.RED + "No signals generated.")
    else:
        display_signals(filtered_signals)

    print("        " + Style.BRIGHT + Fore.BLUE + "Type { C } For Copy SIGNAL'S")
    print("=" * 50)
    print("            " + Style.BRIGHT + Fore.RED + "Press " + Style.BRIGHT + Fore.YELLOW + "( q )" + Style.BRIGHT + Fore.RED + " For Quit...!")
    print("=" * 50)

    while True:
        choice = input().strip().lower()
        if choice == 'c':
            copy_signals(filtered_signals)
        elif choice == 'q':
            print(Style.BRIGHT + Fore.GREEN + "Exiting the DRAGON..Good Bye...")
            break

if __name__ == "__main__":
    main()