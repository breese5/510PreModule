# Generals Performance Tool

This tool processes a CSV file containing generals' battle performance data and elimintate some generals based on under 4 battles then sorts the generals by their aWAR (Adjusted Wins Above Replacement).

## Tool Features

- **Process Generals Data**: Load a CSV file, filter out generals with less than 4 battles, and sort the remaining generals by aWAR in descending order.
- **Run Unit Tests**: Verifies the Task is running correctly

## Requirements

- Python 3.6 or higher
- pandas

## Installation
1) Navigate in terminal to the directory you want this tool (eg. cd ~/Desktop)
2) Clone the GitHub repo locally (git clone https://github.com/breese5/510PreModule.git)
3) If using your own generals data it should be in this format:<br>
General,number_of_battles,WAR,aWAR<br>
General name1,#.#,#<br>
General name2,#,#,#<br>
General name3,#,##,#<br>
General name4,#,#,#<br>
General name5,#,#,#<br>
-**Note: name is a place holder for each generals name and each # is a placeholder for the numeric value corresponding to number of battles, WAR and aWAR of each general specifically
-You may add a csv file with your own data in the required format if desired and name in "Generals_Performance", replacing the provided data

##Each Column

General: The name of the general.<br>
number_of_battles: The number of battles the general participated in.<br>
WAR: Wins Above Replacement, a measure of the general's overall contribution.<br>
aWAR: Adjusted Wins Above Replacement, a measure of the general's contribution per battle

##Running Tool
1) In your terminal, navigate to your cloned local repo: cd /path/to/your/repository
2) Run the following command: pip install . to install the tool locally
3) To process the data, run: process_generals Generals_Performance.csv
4) To run the unit test, run: test_generals

##Ending
That's all! I hope you enjoy using this simple processing tool.
