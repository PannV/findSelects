import os
import Tkinter, tkFileDialog


ch_out = []

def choose():
    
    root = Tkinter.Tk()
    root.withdraw()
    
    print('Hi Katie, please pick a folder/directory')
    
    _folder = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
   
    print('Your folder path is '+ _folder)
    
    print('Now pick your selects , a .txt file')
    
    _file = tkFileDialog.askopenfilename(parent=root,initialdir="/",title='Pick a file')
    print('This is the file you picked: ' + _file)
    
    
    ch_out.append(_folder)
    ch_out.append(_file)
    
    
    return ch_out


#print(ch_out[0])


def rename_files():

    curDir = os.getcwd()
    
    #rootDir = r'/Volumes/kt5tb/ONIA/'
    rootDir = ch_out[0]
    
    fileList = os.listdir(rootDir)
    
    #Selects = r'/Users/pv/Desktop/presets/extra_selects.txt'
    Selects = ch_out[1]
    
    
    select_list = open(Selects).read().splitlines()
    
    #print(file_list)
    
    
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        for file_name in fileList:
            for sel in select_list:
                if sel == file_name:
                    #print(file_name)
                    #print (os.path.join(dirName, file_name))   # print the current path of the matched file
                    os.rename( os.path.join(dirName, file_name), os.path.join(dirName, 'select_' + file_name) )
                
                else:
                    pass
   

 
 
choose()
rename_files()

print('All DONE!')
