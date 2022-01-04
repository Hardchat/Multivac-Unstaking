<img src="https://e.mtv.ac/logo_color.png">

# Multivac Unstaking Tool 
A script to track the total amount of Multivac tokens being unstaked from the pool.

## Details
Firstly, it pulls all active staking addresses from the explorer api, then proceeds to check each address for the value in `withdrawPending` and outputs progress. After each address has been checked we save the data into the directory `mtv_logs` with each file being time-stamped and output it in a more human readable format.

# Linux Requirements
```
git
python3
```
# Windows Requirements
```
python3
windows terminal
```
# Installation
## Linux:
```
git clone https://github.com/Hardchat/Multivac-Unstaking/
```
## Windows:
Download the repository from <a href="https://github.com/Hardchat/Multivac-Unstaking/archive/refs/heads/main.zip">Here</a>

Then, open powershell and install urllib3 with `pip3 install urllib3`

# Usage
## Linux:
```
cd Multivac-Unstaking
python3 unstake.py
```

## Windows:
Using powershell/windows terminal, navigate to the folder the files were downloaded to and enter the project folder:
```
cd Multivac-Unstaking
```

Then you can run the script using:
```
python3 unstake.py
```
