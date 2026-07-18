import os

def delete_everything(folders):
 new_folders = []

 for folder in folders:
  for directory in os.listdir(folder):
   if os.path.isfile(folder + '/' + directory): 
    os.remove(folder + '/' + directory)
    
   
   else:
    new_folders.append(folder + '/' + directory)
 
 if new_folders:
  return delete_everything(new_folders)


delete_everything(['/home/yash/.java'])
