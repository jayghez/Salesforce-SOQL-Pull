import tkinter as tk
from tkinter import filedialog
from salesforce_api import Salesforce
import pandas as pd
client = Salesforce(
    username='USERNAME',
    password='PASSWORD',
    security_token='TOKEN')

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        
        root.title("Salesforce Widget")
        
        #Close window fx
        def quit(event = None):
            root.destroy()  

        #File Picker Fx
        def file_picker():
            selected_files =filedialog.askopenfilenames()
            file_count.set('{} file(s)'.format(len(self.selected_files)))   
    
        # Print new excel to Desktop
        def print_new():
            global dframe
            outputpath = filedialog.asksaveasfile(defaultextension= '.csv')
            dframe.to_csv(outputpath, encoding = 'utf-8')

            
        global dframe, source_name, col_statement, where_statement, limit_statement, payload
        source_name_label = tk.Label(root, text = "Source").grid(row = 12)
        col_statement_label = tk.Label(root, text = "Column Statement").grid(row = 13 )
        where_statement_label = tk.Label(root, text = "Where Statement").grid(row = 14 )
        limit_statement_label = tk.Label(root, text = "Limit Statement").grid(row = 15 )
        
        
        source_name = tk.Entry(root)
        source_name.grid(row = 12, column =1 )
        col_statement = tk.Entry(root)
        col_statement.grid(row= 13,column =1)
        where_statement = tk.Entry(root)
        where_statement.grid(row= 14,column =1)
        limit_statement = tk.Entry(root)
        limit_statement.grid(row= 15,column =1)
        
        
        label_use=tk.Label(root, text = "IF USING WHERE/LIMIT STATEMENT, INCLUDE WHERE/LIMIT in line").grid(row = 18, column =1)
        
        #Kill Button
        button =tk.Button(text = "Kill", command= quit)
        button.grid(row = 16 )

        # Download  Button
        display_fp1_button = tk.Button(text="Download", command = print_new)
        display_fp1_button.grid(row = 16, column =3)
        
       
       

        


                    
        def payloade():
            global dframe, source_name, col_statement, where_statement, limit_statement, payload
            col = col_statement.get()
            source = source_name.get()
            if len(str(where_statement))== 0:
                wheres = ''
            else:
                wheres = where_statement.get()
            if len(str(limit_statement))==0:
                limit = ''
            else:
                limit=limit_statement.get()
            limit = limit_statement.get()
            payload= client.sobjects.query(  ' SELECT ' + col 
                                           + ' FROM '+ source + ' '+
                                           wheres  + ' '+  limit)
            #FROM USERS
            #WHERE SOMETHING
            #LIMIT SOMETHING
            dframe = pd.DataFrame(data=[x for x in payload])
            print(len(dframe.index))

         # Payload Button
        test_button = tk.Button(text="Payload Run", command =payloade)
        test_button.grid(row = 16, column =1)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x400+250+200")
    MainApplication(root)
    root.mainloop()