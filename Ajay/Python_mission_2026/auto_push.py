import os
import time
import subprocess
from datetime import datetime

# Is directory ko monitor karna hai
REPO_PATH = r"C:\Users\squad\Desktop\Ajay\Ajay\DSA"

def check_for_changes():
    try:
        # Check karte hain ki koi changes hue hain ya nahi
        status_output = subprocess.check_output(['git', 'status', '--porcelain'], cwd=REPO_PATH, text=True)
        if status_output.strip():
            return True
        return False
    except subprocess.CalledProcessError as e:
        print(f"Git status check karne me error aaya: {e}")
        return False

def git_commit_and_push():
    try:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 1. Sabhi changes ko add karo
        subprocess.check_call(['git', 'add', '.'], cwd=REPO_PATH)
        
        # 2. Commit karo
        commit_message = f"Auto-commit: {current_time}"
        subprocess.check_call(['git', 'commit', '-m', commit_message], cwd=REPO_PATH)
        
        # 3. GitHub par push karo
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Changes detect hue. GitHub par push kar rahe hain...")
        subprocess.check_call(['git', 'push'], cwd=REPO_PATH)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Successfully push ho gaya!\n")
        
    except subprocess.CalledProcessError as e:
        print(f"Git operation ke dauran error aaya: {e}")

if __name__ == "__main__":
    print("=====================================================")
    print(f"Auto-push script start ho gaya hai.")
    print(f"Monitoring folder: {REPO_PATH}")
    print("Har 10 second me changes check honge.")
    print("Script rokne ke liye 'Ctrl + C' dabayein.")
    print("=====================================================\n")
    
    try:
        while True:
            if check_for_changes():
                git_commit_and_push()
            
            # Har 10 seconds me check karega
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nAuto-push script stop ho gaya hai.")
