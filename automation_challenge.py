import os

def proccess_folder(folder_name):

  files = os.listdir(folder_name)
  years = []
  months = []
  dates = []
  for i in files:
    split_files = i.split(".")
    
    year_1 = split_files[1][4:6]
    month_1 = split_files[1][2:4]
    date_1 = split_files[1][0:2]
    
    if (year_1 not in years):
      years.append(year_1)
    if (month_1 not in months):
      months.append(month_1)
    if (date_1 not in dates):
      dates.append(date_1)
#  print("years:",years)
#  print("months:",months)
#  print("dates:",years)
  
  return(files,years,months,dates)


def create_dir_mov_files(src_folder,dst_folder,files,years,months,dates):
  
  for i in years:
   for j in months:
    for k in dates:
      os.system("mkdir -p {dst_folder_name}/{year_name}/{month_name}/{date_name}".format(dst_folder_name = dst_folder,year_name = i,month_name= j,date_name = k))

  

  for n in files:
    split_files = n.split(".")
    
    f_year_1 = split_files[1][4:6]
    f_month_1 = split_files[1][2:4]
    f_date_1 = split_files[1][0:2]

    os.system("mv {src_folder_name}/{file_name} {dst_folder_name}/{year_name}/{month_name}/{date_name}".format(src_folder_name = src_folder, dst_folder_name = dst_folder, year_name = f_year_1,month_name= f_month_1,date_name = f_date_1,file_name = n))
    

src_folder = "drive/MyDrive/src_folder"
dst_folder = "drive/MyDrive/dst_folder"

obj = proccess_folder(src_folder)

create_dir_mov_files(src_folder,dst_folder,obj[0],obj[1],obj[2],obj[3])


