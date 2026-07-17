import subprocess
import time
import datetime
import os

def push_to_github():
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-commit: {current_time}"
        
        # Files add karo
        subprocess.run(["git", "add", "."], capture_output=True)
        
        # Check karo ki kya kuch "staged" (add hui) files hain commit karne ke liye
        # Agar error aaye (returncode != 0), matlab commit karne ke liye kuch naya nahi hai
        commit_process = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
        
        if commit_process.returncode != 0:
            print(f"[{current_time}] Koi naye changes nahi hain push karne ke liye.")
            return

        # Agar commit success ho gaya toh Push karo
        push_process = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        
        if push_process.returncode == 0:
            print(f"[{current_time}] ✅ Code GitHub par successfully push ho gaya!")
        else:
            print(f"[{current_time}] ❌ Push fail ho gaya: {push_process.stderr}")
            
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ Error aaya: {str(e)}")

#=======================================================
# SETTINGS: 
#=======================================================
# Kitne seconds baad push karna hai? (Default: 10 minutes = 600 seconds)
# Abhi ke liye 60 seconds (1 minute) rakha hai taaki aap test kar sakein
INTERVAL_SECONDS = 60 

if __name__ == "__main__":
    print("🚀 Auto-pusher start ho gaya hai!")
    print(f"⏳ Ye script har {INTERVAL_SECONDS // 60} minute mein check karegi aur push karegi.")
    print("🛑 Isko rokne ke liye terminal par 'Ctrl + C' dabayein.\n")
    
    while True:
        push_to_github()
        time.sleep(INTERVAL_SECONDS)
