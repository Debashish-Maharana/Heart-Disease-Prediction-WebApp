import pyrebase
from datetime import datetime

firebase_config = {
    "apiKey": "AIzaSyBDqIy22JtJjMH-pFE2xKan60Sn59VFwzs",
    "authDomain": "myblogsite-a2800.firebaseapp.com",
    "projectId": "myblogsite-a2800",
    "storageBucket": "myblogsite-a2800.appspot.com",
    "messagingSenderId": "450379329014",
    "appId": "1:450379329014:web:544da56f3a3b4de86cabd7",
    "databaseURL": "https://myblogsite-a2800-default-rtdb.asia-southeast1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()

def sanitize_email(email: str) -> str:
    """
    Sanitize email to be used as Firebase Realtime Database key/path
    by replacing '@' with '_at_' and '.' with '_dot_'.
    """
    return email.replace('@', '_at_').replace('.', '_dot_')

def login_user(email, password):
    """
    Login user with email and password.
    Returns user dict containing idToken, email, etc.
    """
    return auth.sign_in_with_email_and_password(email, password)

def register_user(email, password):
    """
    Register new user with email and password.
    Returns user dict.
    """
    return auth.create_user_with_email_and_password(email, password)

def upload_to_storage(local_path, remote_path, user):
    """
    Upload a local file to Firebase Storage under remote_path.
    Requires 'user' dict obtained from login_user for authentication.
    Logs upload info in Realtime Database.
    """
    if not isinstance(user, dict):
        raise ValueError("Expected user dict with idToken and email, got: {}".format(type(user)))
    if 'idToken' not in user or 'email' not in user:
        raise KeyError("User dict must contain 'idToken' and 'email' keys.")

    id_token = user['idToken']
    
    # Upload file with authentication token
    storage.child(remote_path).put(local_path, id_token)
    
    # Get download URL with token
    url = storage.child(remote_path).get_url(id_token)
    
    uid = sanitize_email(user['email'])
    
    # Log upload metadata with timestamp in Realtime Database
    db.child("reports").child(uid).push({
        "path": remote_path,
        "timestamp": datetime.now().strftime('%d-%m-%Y %H:%M')
    })
    
    return url

def get_user_reports(uid):
    """
    Fetch reports metadata from Realtime Database for user ID (sanitized).
    """
    return db.child("reports").child(uid).get()

def list_reports(user_email):
    """
    Return a list of report info dicts (name, url, timestamp) for a user email.
    """
    uid = sanitize_email(user_email)
    reports = db.child("reports").child(uid).get()
    report_files = []

    if reports.each():
        for report in reports.each():
            data = report.val()
            path = data.get("path")
            timestamp = data.get("timestamp", "")
            # Use no token for public URL; adjust if your storage rules require auth token
            url = storage.child(path).get_url(None) if path else None
            
            report_files.append({
                "name": path or "Unknown",
                "url": url,
                "timestamp": timestamp
            })

    return report_files


# Example usage:
if __name__ == "__main__":
    try:
        user = login_user("test@example.com", "yourpassword")
        print(f"Logged in as: {user['email']}")

        local_file = "path/to/local/file.pdf"
        remote_file = "reports/user_uploads/file.pdf"
        
        download_url = upload_to_storage(local_file, remote_file, user)
        print("File uploaded. Download URL:", download_url)
        
        reports = list_reports(user['email'])
        print("User reports:")
        for r in reports:
            print(r)

    except Exception as e:
        print("Error:", e)
