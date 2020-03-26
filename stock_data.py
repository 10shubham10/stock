import datetime
import requests
import os
import pandas as pd

class Stock_data:
    def __init__(self):
        pass
    # this method will return the list of last thirty days excluding weekends.
    def data_of_the_input_days(self,days):
        days_array = []
        self.days = days
        # find the list of days from today to the input days
        for i in range(0,self.days):
            start_date = datetime.datetime.now() - datetime.timedelta(i)
            # weekday module will return 5, 6 for saturdays and sunday which will be excluded from the code in the below line.
            if (((start_date.weekday()) == 5) or ((start_date.weekday()) == 6)):
                continue
            else:
                days_array.append(str(start_date.strftime("%d""%b""%Y").upper()))
        return days_array

    # this method will get the connection and look for the files from the same link.
    def link_for_download(self,link,date,connection):
        self.connection = connection
        self.link = link
        self.date = date
        # try except is used for the connection exceptions of internet, data not available, holiday date of stock, data not generated for the specific date.
        try:
            connection = requests.get(self.link, allow_redirects=True, timeout=200)
            open(str(datetime.datetime.now().date()) + "/cm" + date + "bhav.csv.zip", 'wb').write(connection.content)
        except:
            print(
                "There can be multiple reason for no data generation for the date " + date + "\n1. website is not responding.\n2. Internet connection has problem\n3. This day was holiday.\n4. Data for this day is not generated yet.")

    def download_zip_files(self,days):
        self.days = days
        # if the directory is not present the code will create the directory
        try:
            os.makedirs(str(datetime.datetime.now().date()))
        except:
            print("Directory already exist, application will replace the same data in the date folder:- " + str(datetime.datetime.now().date()))


        for date in self.data_of_the_input_days(days=days):
            # get the particulars for the link(date, month, year)
            month = date[2:5]
            year = date[5:]
            link = "https://archives.nseindia.com/content/historical/EQUITIES/"+year+"/"+ month+"/cm"+ date+"bhav.csv.zip"
            print (link)
            self.link_for_download(link= link,date= date,connection="stock_url")


    # get the specific collumns of the downloaded files
    def merge_data(self,*args):
        dir_name = (datetime.datetime.now().date())
        # print (dir_name)
        self.data_directory = (os.getcwd() + "/" + str(dir_name))
        # print (self.data_directory)
        os.chdir(self.data_directory)  # change directory from working dir to dir with files
        # print (os.getcwd())
        df1 = []
        for item in os.listdir(str(self.data_directory)):  # loop through items in dir
            # taking the zip files only
            if ".zip" in item:
                df = pd.read_csv(item, index_col=None, header=0)
                df1.append(df)
        # merge all the data of the zipped files
        df2 = pd.concat(df1,axis=0, ignore_index=True)
        # getting the specific columns from all the zipped files into final_df
        final_df = df2[[*args]]
        # print(final_df)
        # writing the final data into the excel
        final_df.to_excel("final_data.xlsx", index = False)

days = Stock_data()
print (days.data_of_the_input_days(days=30))
days.download_zip_files(days = 30)
days.merge_data('SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TIMESTAMP')