# tasks.py
from _celery import app
import subprocess

# Define tasks

@app.task(name='run_ScriptTracker')
def run_ScriptTracker():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\ScriptTracker.bat'])
    print('Script Tracker Executed.')

@app.task(name='run_diskSpaceManagement')
def run_diskSpaceManagement(): 
    subprocess.Popen([r'\\sf-data\data\_PyScripts\Disk Space Monitoring\usageAlert.bat'])
    print('Disk Space Management Executed.')

@app.task(name='run_DashesInDB3')
def run_DashesInDB3():
    subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\DashesInDb3.bat'])
    print('Dashes Check Executed.')

@app.task(name='run_DailyPubLog')
def run_DailyPubLog():
    subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\DailyPubLog.bat'])
    print('Daily Pub Log Executed.')

@app.task(name='run_JapanETL')
def run_JapanETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Japan_ETL.bat'])
    print('Japan ETL Executed.')

@app.task(name='run_ITC_Availability')
def run_ITC_Availability():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\itc_Availability.bat'])
    print('ITC Availability Executed.')

@app.task(name='run_JetroAvailability')
def run_JetroAvailability():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\jetro_Availability.bat'])
    print('Jetro Availability Executed.')

@app.task(name='run_UN_Comtrade_ETL')
def run_UN_Comtrade_ETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\UNcomtradeAutomation_ETL.bat'])
    print('UN Comtrade ETL Executed.')

@app.task(name='run_FinlandScrape')
def run_FinlandScrape():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\finlandAutomation.bat'])
    print('Finland Scrape Executed.')

@app.task(name='run_ArgentinaETL')
def run_ArgentinaETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Aregentina_ETL.bat'])
    print('Aregentina Executed.')

@app.task(name='run_FranceCustomsETL')
def run_FranceCustomsETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\France_Customs_ETL.bat'])
    print('France Customs ETL Executed.')

@app.task(name='run_ItalyIstatETL')
def run_ItalyIstatETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\italyAutomation.bat'])
    print('Italy ISTAT Scrape Executed.')

@app.task(name='run_CzechRepublicETL')
def run_CzechRepublicETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Czech_Republic_ETL.bat'])
    print('Czech Republic ETL Executed.')

@app.task(name='run_IndonesiaETL')
def run_IndonesiaETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Indonesia_ETL.bat'])
    print('Czech Republic ETL Executed.')

@app.task(name='run_IsraelETL')
def run_IsraelETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Israel_ETL.bat'])
    print('Israel ETL Executed.')

@app.task(name='run_MacaoETL')
def run_MacaoETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Macao_ETL.bat'])
    print('Macao ETL Executed.')

@app.task(name='run_MauritiusETL')
def run_MauritiusETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Mauritius_ETL.bat'])
    print('Mauritius ETL Executed.')

@app.task(name='run_ThailandETL')
def run_ThailandETL():
    process = subprocess.Popen([r'\\sf-data\data\_PyScripts\Damon\Tasks\Thailand_ETL.bat'])
    print('Thailand ETL Executed.')



