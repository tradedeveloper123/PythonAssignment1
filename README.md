

````md
# Password Strength Checker

## Overview
This Python script checks whether a user-entered password is **strong or weak** based on common security rules.  
It helps ensure that passwords follow best practices to improve security.

The script uses **regular expressions (regex)** to validate different password conditions.

---

## Features
The password is considered **strong** only if it meets **all** of the following criteria:

- Minimum **8 characters** in length
- Contains **at least one uppercase letter (A–Z)**
- Contains **at least one lowercase letter (a–z)**
- Contains **at least one digit (0–9)**
- Contains **at least one special character**  
  (`! @ # $ % ^ & * ( ) , . ? " : { } | < >`)

---

## Code Explanation

### 1. Import Required Module
```python
import re
````

* The `re` module is used for **regular expression matching**.
* It helps search for specific character patterns in the password.

---

### 2. Function: `check_password_strength`

```python
def check_password_strength(password: str) -> bool:
```

* Accepts a password as a string.
* Returns `True` if the password is strong.
* Returns `False` if any rule is not satisfied.

---

### 3. Validation Rules

#### a. Minimum Length Check

```python
if len(password) < 8:
    return False
```

* Ensures the password has **at least 8 characters**.

---

#### b. Uppercase Letter Check

```python
if not re.search(r"[A-Z]", password):
    return False
```

* Verifies at least **one uppercase letter** exists.

---

#### c. Lowercase Letter Check

```python
if not re.search(r"[a-z]", password):
    return False
```

* Ensures at least **one lowercase letter** is present.

---

#### d. Digit Check

```python
if not re.search(r"[0-9]", password):
    return False
```

* Confirms at least **one numeric digit** is included.

---

#### e. Special Character Check

```python
if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    return False
```

* Checks for at least **one special character**.
* Improves password complexity and security.

---

### 4. Successful Validation

```python
return True
```

* If all conditions pass, the password is declared **strong**.

---

## Main Script Execution

```python
if __name__ == "__main__":
```

* Ensures the script runs only when executed directly (not imported).

---

### User Input

```python
user_password = input("Enter a password to check its strength: ")
```

* Prompts the user to enter a password.

---

### Output Result

```python
if check_password_strength(user_password):
    print("Your password is strong!")
else:
    print("Your password is weak. Make sure it meets the following criteria")
```

* Displays a success message if the password is strong.
* Otherwise, prints clear guidelines for improvement.

---

## Sample Output

### Strong Password

```
Enter a password to check its strength: Strong@123
Your password is strong!
```

### Weak Password

```
Enter a password to check its strength: test123
Your password is weak. Make sure it meets the following criteria
At least 8 characters long
Contains uppercase and lowercase letters
Contains at least one number (0-9)
Contains at least one special character (!, @, #, $, %, etc.)
```
<img width="1863" height="921" alt="image" src="https://github.com/user-attachments/assets/6df6309a-23db-4f02-82ff-0d0a5c516169" />






````md
# CPU Usage Monitoring Script

## Overview
This Python script continuously monitors the system’s **CPU usage** and triggers an alert when usage exceeds a defined threshold.  
It is useful for detecting high CPU consumption in real time and can be used in **server monitoring**, **performance testing**, or **system health checks**.

The script uses the `psutil` library to retrieve CPU usage statistics.

---

## Features
- Real-time CPU usage monitoring
- Configurable CPU threshold
- Alerts when CPU usage exceeds the limit
- Graceful shutdown using keyboard interrupt (`Ctrl + C`)
- Basic error handling

---

## Prerequisites
Ensure Python 3 is installed, then install the required library:

```bash
pip install psutil
````

---

## Code Explanation

### 1. Import Required Modules

```python
import psutil
import time
```

* `psutil`: Fetches system and CPU usage information.
* `time`: Controls execution timing and prevents excessive CPU polling.

---

### 2. Function: `monitor_cpu`

```python
def monitor_cpu(threshold=80):
```

* Accepts a CPU usage **threshold percentage**.
* Default threshold is set to **80%**.

---

### 3. Start Monitoring

```python
print("Monitoring CPU usage...")
```

* Informs the user that CPU monitoring has started.

---

### 4. Infinite Monitoring Loop

```python
while True:
```

* Keeps the script running continuously until interrupted.

---

### 5. Fetch CPU Usage

```python
cpu_usage = psutil.cpu_percent(interval=1)
```

* Measures CPU usage over **1 second**.
* Returns the CPU usage percentage.

---

### 6. Threshold Check

```python
if cpu_usage > threshold:
    print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
```

* Displays an alert if CPU usage crosses the defined limit.

---

### 7. Sleep Interval

```python
time.sleep(0.5)
```

* Adds a short delay to prevent a tight loop.
* Reduces unnecessary CPU load caused by the script itself.

---

### 8. Graceful Exit Handling

```python
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
```

* Allows the user to stop the script safely using `Ctrl + C`.

---

### 9. Error Handling

```python
except Exception as e:
    print(f"An error occurred during CPU monitoring: {e}")
```

* Catches and displays unexpected runtime errors.

---

## Main Execution Block

```python
if __name__ == "__main__":
    monitor_cpu(threshold=80)
```

* Ensures the script runs only when executed directly.
* Starts monitoring with an **80% CPU usage threshold**.

---

## Sample Output

### Normal CPU Usage

```
Monitoring CPU usage...
```

### High CPU Usage Alert

```
Alert! CPU usage exceeds threshold: 81.2%
```

### Script Termination

```
Monitoring stopped by user.
```

---

## Use Cases

* Monitoring CPU usage on servers
* Detecting performance bottlenecks
* Running background system health checks
* Learning system monitoring with Python

---
<img width="1253" height="818" alt="image" src="https://github.com/user-attachments/assets/40215b8d-b12a-4264-a79a-91d532a9c49c" />


## Flask Configuration Management Application
## Overview 
This Flask application reads a configuration file from the local system, parses its contents, stores the data in MongoDB, and exposes an API endpoint to fetch the latest configuration in JSON format
<img width="1779" height="918" alt="image" src="https://github.com/user-attachments/assets/99105009-ca5c-41cd-9d09-da4c1fcb60c3" />
<img width="1852" height="868" alt="image" src="https://github.com/user-attachments/assets/693074e5-2efc-460d-8b7d-02bb8dfb21f8" />
<img width="1813" height="883" alt="image" src="https://github.com/user-attachments/assets/2ec9cb9a-d833-499f-bc26-679e971c29da" />





