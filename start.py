from os import system, environ

class lavalinkserver:

    def __init__(self):
        self.download_command = "curl -s https://api.github.com/repos/Frederikam/Lavalink/releases/24847811| grep browser_download_url | cut -d '\"' -f 4 | wget -qi -"
        self.change_port = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'
        self.change_password = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
        self.additional = environ.get("ADDITIONAL_JAVA_OPTIONS")
        self.run_command = f"java -jar Lavalink.jar {self.additional}"

    def password_and_port(self):
        try:
            system(self.change_port)
            if not environ.get("PASSWORD"):
               print("[INFO] No password provided...")
               return system(self.no_password)
            system(self.change_password)
        except BaseException as exc:
            print(f"[ERROR] Error when setup port & password... Info: {exc}")
        else:
            print("[INFO] Setup port & password...")

    def download(self):
        print("[INFO] Downloading lavalink...")
        try:
            system(self.download_command)
        except BaseException as exc:
            print(f"[ERROR] Failed when downloading lavalink server. Info: {exc}")

        else:
            print("[INFO] Lavalink server has been downloaded")
    
    def run(self):
        self.download()
        self.password_and_port()
        print("[INFO] Iniciando o lavalink.")
        try:
            system(self.run_command)
        except BaseException as exc:
            print(f"[ERROR] Failed to run lavalink server. Info: {exc}")

if __name__ == "__main__":
   lavalinkserver().run()
