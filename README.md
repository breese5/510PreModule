# Generals Performance Tool

This tool processes a CSV file containing generals' battle performance data and elimintate some generals based on under 4 battles then sorts the generals by their aWAR (Adjusted Wins Above Replacement).

## Tool Features

- **Process Generals Data**: Load a CSV file, filter out generals with less than 4 battles, and sort the remaining generals by aWAR in descending order.
- **Run Unit Tests**: Verifies the Task is running correctly

## Requirements

- Python 3.6 or higher
- pandas

## Installation

1) Clone or Fork the repository so you have access to the dataset and tool
2) If using your own generals data it should be in this format:
General,number_of_battles,WAR,aWAR
General name1,#.#,#
General name2,#,#,#
General name3,#,##,#
General name4,#,#,#
General name5,#,#,#
**Note: name is a place holder for each generals name and each # is a placeholder for the numeric value corresponding to number of battles, WAR and aWAR of each general specifically

##Each Column

General: The name of the general.
number_of_battles: The number of battles the general participated in.
WAR: Wins Above Replacement, a measure of the general's overall contribution.
aWAR: Adjusted Wins Above Replacement, a measure of the general's contribution per battle

##Running Tool
1) In your terminal, navigate to your github repo or local repo: cd /path/to/your/repository
