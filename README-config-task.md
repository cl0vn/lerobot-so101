# Config Files with Python

## 🎯 **Task **
Complete the template files to create a working Python script that uses YAML config files to execute complex commands.

## 📁 **Files You Have**
- `lerobot-config-template.yaml` - Basic config template (needs expansion)
- `lerobot-execute-command-template.py` - Python script with pseudo code (needs completion)

## ✅ **Step-by-Step Instructions**

### **Step 1: Install Requirements**
Install any missing libraries in your machine, such as:
```bash
pip install PyYAML
```

### **Step 2: Complete the Python Script**
Fill in the missing code in `lerobot-execute-command-template.py`:

#### 🔧 **Function 1: `load_config()`**
**Research:** How to read YAML files in Python
**Complete:** The function to load and parse a YAML file

#### 🔧 **Function 2: `build_command_args()`**
**Current:** Only handles a mockup example `teleop` section
**Complete:** Support any additional parameters needed for your command, calibrate, or record, or train, etc

#### 🔧 **Function 3: `execute_command()`**
**Research:** How to use `subprocess.run()` in Python
**Complete:** Execute the command and handle errors

#### 🔧 **Function 4: `main()`**
**Research:** How to use `argparse` in Python
**Complete:** Parse command line arguments to get the config file path
**Expected usage:** `python script.py config.yaml`

### **Step 3: Expand the YAML Config**
Add any sections or paramters to your config file as needed for your command. For example

```yaml
# Robot configuration
robot:
  type: "so101_follower"
  port: "/dev/ttyACM1"
  id: "my_awesome_follower_arm"
  cameras:
    front:
      type: "opencv"
      index_or_path: "/dev/video2"
      width: 640
      height: 480
      fps: 30
```

### **Step 4: Test Your Work**

#### **Basic Test:**
For example:
```bash
python lerobot-execute-command-template.py lerobot-config-template.yaml
```

#### **Expected Output:**
```
📁 Loading configuration from: lerobot-config-template.yaml
🔧 Building command arguments...
Command to execute:
lerobot-calibrate --teleop.type=so101_leader --teleop.port=/dev/ttyACM0 --teleop.id=my_awesome_leader_arm --robot.type=so101_follower --robot.port=/dev/ttyACM1 --robot.id=my_awesome_follower_arm --robot.cameras={"front":{"type":"opencv","index_or_path":"/dev/video2","width":640,"height":480,"fps":30}} --display_data=true --dataset.repo_id=my_user/my_dataset --dataset.num_episodes=1 --dataset.single_task="Grab the lego and put in the box" --resume=true

🚀 Executing command...
❌ Command failed with return code 127
Error: /bin/sh: 1: lerobot-calibrate: command not found
```

**✅ This error is EXPECTED!** The `lerobot-calibrate` command doesn't exist on your system if you don't have lerebot install, but your script successfully built the command from the config file.

## 🔍 **What You're Learning**

### **Python Concepts:**
- File I/O operations (`open()`, `with` statements)
- Dictionary manipulation and nested data structures
- String formatting (`f-strings`)
- Error handling (`try/except`)
- Command-line argument parsing (`argparse`)
- Process execution (`subprocess`)

### **Configuration Management:**
- YAML file structure and syntax
- Separating configuration from code
- Making complex commands manageable
- Reusable and maintainable code


## 💡 **Tips**

**YAML files** Search: "python yaml safe_load example"
**argparse functionality** Search: "python argparse tutorial"
**Subprocess functionality** Search: "python subprocess run example"
