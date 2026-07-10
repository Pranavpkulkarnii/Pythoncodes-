import math
import time

def surf_the_wave():
    print("Starting the wave... Press Ctrl+C to stop!\n")
    
    try:
        step = 0
        while True:
            # Calculate the sine of our current step. 
            # Multiply by 20 for the width, add 20 so it doesn't go negative.
            position = int(math.sin(step) * 20 + 20)
            
            # Create the wave string using spaces to push the emoji to the right position
            wave_line = (" " * position) + "🌊"
            
            print(wave_line)
            
            # Move the wave forward and pause briefly to create smooth animation
            step += 0.15
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        # Gracefully handle the user stopping the script
        print("\nWave surfing completed! Back to dry land.")

if __name__ == "__main__":
    surf_the_wave()