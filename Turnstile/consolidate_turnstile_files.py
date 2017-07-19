'''
    Script that takes in turnstile files and consolidates them into one file located at output_file. 
    
    All turnstile files have the columns: 
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', 
    
    There will be one row with the column headers, located at the top of the file. 
    The input files do not have column header rows of their own.
    
    For example, if file_1 has:
    line 1 ...
    line 2 ...
    
    and another file, file_2 has:
    line 3 ...
    line 4 ...
    line 5 ...
    
    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
'''

## Function
def create_master_turnstile_file(filenames, output_file):
    # Consolidates rows from multiple files
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
            file_in = open(filename, 'r')
            for row in f_in:
                master_file.write(row)