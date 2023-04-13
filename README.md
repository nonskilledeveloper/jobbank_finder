# jobbank_finder

This is a web scraping tool designed to find job postings on the Canadian website Job Bank that meet specific criteria that are not configurable on the website itself. The software ranks the job postings and generates a file with easy-to-read results.

# Instalation

To use this script, you must have Python installed on your computer. Additionally, you need to install the following packages using pip:

* requests
* lxml
* markdown

You can install these packages by running the following command:

`pip install requests lxml markdown`

# Usage

To run the script, execute the following command:

`python offer_analyzer.py`

![](http://assets.nonskilledeveloper.com/16675314895783.jpg)

When prompted, input the number of pages you want to analyze. The software will automatically analyze each job posting and output a summary of the findings in the console. The most important part of the summary is the "Stars Rank" section, which indicates how closely each job posting matches the specified criteria. These criteria can be customized in the code and the software will support customizable criteria during runtime in the future.

The script will generate a folder named with the current date containing all the information found.

![](http://assets.nonskilledeveloper.com/16675319232825.jpg)

# Notes

* The script ranks job postings according to the criteria specified in the code.
* The script generates an HTML file with all the results found.

# Legal Compliance

The usage of this web scraping tool does not violate the user agreement, "robots.txt" section of the website, or any Canadian laws prohibiting web scraping on this website.

# License

This project is licensed under the GNU General Public License v3.0 - see the [<u>LICENSE</u>](https://github.com/nonskilledeveloper/jobbank_finder/blob/main/LICENSE) file for details.
