def gui_output():
    try:
        with open('rms_log.txt') as log:
            lines = log.readlines()
            if lines:
                print("Latest Output for GUI:")
                print(lines[-1])
            else:
                print("No logs to display.")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == '__main__':
    gui_output()