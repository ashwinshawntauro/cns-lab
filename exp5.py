def ftp_client():
    print("FTP Server: ")
    server=input("Enter server: ")
    username=input("Enter username: ")
    password=input("Enter password: ")
    try:
        ftp=ftplib.FTP(server)
        ftp.login(user=username,passwd=password)
        print(f"Connected to {server}")
        print("Directory List")
        ftp.retrlines("LIST")
        def upload():
            file_path=input("Enter file name: ")
            file_name=os.path.basename(file_path)
            with open(file_path,'rb') as file:
                ftp.storbinary(f"STOR {file_name}",file)
            print("File uploaded")
        def download():
            file_name=input("Enter file to download: ")
            local_path=input("Enter local path to save: ")
            with open(local_path+'/'+file_name,'wb') as file:
                ftp.retrbinary('RETR'+file_name,file.write)
            print("Downloaded file")
        while True:
            print("\nOptions")
            print("1.DirectoryList")
            print("2.Upload")
            print("3.Download")
            print("4.Quit")
            choice=int(input("Enter your choice"))
            if choice=='1':
                print("Directory List: ")
                ftp.retrlines("LIST")
            elif choice=='2':
                upload_file()
            elif choice == '3':
                download_file()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        ftp.quit()
        print("Disconnected from server")
    except ftplib.all_errors as e:
        print("FTP SErvere error ",e)

if __name__=="__main__":
    ftp_client()