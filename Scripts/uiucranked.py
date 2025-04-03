import time
import random
import sys
import pyautogui
import threading
import os

# Define your identifiers
MY_SCHOOL = "University of Illinois Urbana-Champaign"
MY_MAJOR = "Computer Science"
MY_HIGH_SCHOOL = "Waubonsie Valley High School"

# Global variables
RUNNING = False

def start_automation():
    """Function to start the automation"""
    global RUNNING
    RUNNING = True
    print("\n🟢 Automation STARTED! Press Ctrl+C to stop.")
    # Run the automation in the main thread
    auto_clicker()

def auto_clicker():
    """Function that automatically checks profiles and clicks accordingly"""
    global RUNNING
    
    try:
        print("\n📋 INSTRUCTIONS:")
        print("For each pair of profiles:")
        print("- Type 'l' or 'left' if your profile is on the left")
        print("- Type 'r' or 'right' if your profile is on the right")
        print("- Type 'e' or 'equal' if neither profile is yours")
        print("- Type 'q' or 'quit' to exit")
        print("\nMake sure your browser window with uiucranked.com is visible!")
        
        # Get the screen dimensions once
        screen_width, screen_height = pyautogui.size()
        
        while RUNNING:
            # Ask for input
            choice = input("\nWhich profile is yours? (l/r/e/q): ").lower().strip()
            
            if choice in ['q', 'quit', 'exit']:
                print("\n👋 Exiting automation.")
                RUNNING = False
                break
                
            if choice in ['l', 'left']:
                print("Clicking left profile")
                pyautogui.click(x=screen_width * 0.25, y=screen_height * 0.5)
            elif choice in ['r', 'right']:
                print("Clicking right profile")
                pyautogui.click(x=screen_width * 0.75, y=screen_height * 0.5)
            elif choice in ['e', 'equal']:
                print("Clicking equal")
                pyautogui.click(x=screen_width * 0.5, y=screen_height * 0.7)
            else:
                print("Invalid input. Please try again.")
                continue
            
            # Wait a moment for the next pair to load
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\n👋 Script terminated by user.")
        RUNNING = False
    except Exception as e:
        print(f"\n❌ Error in auto_clicker: {e}")
        RUNNING = False



def main():
    """Main function to set up and run the script"""
    print("\n🔄 UIUC Ranked Automation Tool 🔄")
    print("=================================")
    print("This tool will help you automate clicking on uiucranked.com")
    print("\n1. Open your browser and navigate to https://uiucranked.com/")
    print("2. Position the browser window so it's visible")
    print("3. Come back to this terminal to control the automation")
    
    # Ask if user is ready to start
    input("\nPress Enter when you're ready to start...")
    
    # Start the automation
    start_automation()


if __name__ == "__main__":
    main()
