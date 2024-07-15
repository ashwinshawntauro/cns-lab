import ftplib
import os
def ftp_client():
    server=input("Enter the server name: ")
    username=input("Enter username: ")
    password=input("Enter password: ")
    try:
        ftp=ftplib.FTP(server)
        ftp.login(user=username,passwd=password)
        print("Connect to ",server)
        print("Directory List:")
        ftp.retrlines('LIST')

        def upload_file():
            file_path=input("Enter file path: ")
            file_name=os.path.basename(file_path)
            with open(file_path,'rb') as file:
                ftp.storbinary(f'STOR {file_path}',file)
            print("File uploaded")

        def download_file():
            file_name=input("Enter the file name: ")
            local_path=input("Enter the local path: ")
            with open(local_path+'/'+file_name,'wb') as file:
                ftp.retrbinary('RETR '+file_name,file.write)
            print("File downoaded")
        while True:
            print("\nOptions:")
            print("1. List Directory")
            print("2. Upload File")
            print("3. Download File")
            print("4. Quit")
            choice=int(input("Enter your choice: "))
            if choice=='1':
                print("Directory List")
                ftp.retrlines('LIST')
            elif choice=='2':
                upload_file()
            elif choice=='3':
                download_file()
            elif choice=='4':
                break
            else:
                print("Invalid input")
        ftp.quit()
        print("Disconnected from server")
    except ftplib.all_errors as e:
        print(f'FTP error: ',e)
    
if __name__=="__main__":
    ftp_client()

