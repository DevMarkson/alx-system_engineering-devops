# Processes and Signals

This repository contains a set of Bash scripts that demonstrate various operations related to processes and signals. Each script focuses on a specific task and provides a solution using Bash scripting.

## List of Scripts

1. **0-what-is-my-pid**: Displays the PID (Process ID) of the script itself.
2. **1-list_your_processes**: Lists all currently running processes, including those without a TTY, in a user-oriented format, showing process hierarchy.
3. **2-show_your_bash_pid**: Displays lines containing the word "bash" to obtain the PID of the Bash process. Ignoring shellcheck error SC2009 is required.
4. **3-show_your_bash_pid_made_easy**: Displays the PID and process name of processes containing the word "bash". ps command is not used.
5. **4-to_infinity_and_beyond**: Displays the message "To infinity and beyond" indefinitely, with a 2-second sleep between iterations.
6. **5-dont_stop_me_now**: Stops the "4-to_infinity_and_beyond" process using the kill command.
7. **6-stop_me_if_you_can**: Stops the process with a specific PID using the kill command.

## Requirements

To run these scripts, you need a Unix-like environment with Bash installed. The scripts have been tested on Ubuntu, but they should work on other Linux distributions or macOS.

## Usage

1. Clone the repository:

```
git clone https://github.com/your_username/alx-system_engineering-devops.git
```

2. Change into the "0x05-processes_and_signals" directory:

```
cd alx-system_engineering-devops/0x05-processes_and_signals
```

3. Run any of the scripts using the Bash interpreter:

```
./script_name
```

Make sure to replace "script_name" with the actual name of the script you want to run.



