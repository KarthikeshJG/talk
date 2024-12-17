# Basic ROS2 Talker and Listener Program

This repository contains a simple ROS2 publisher (talker) and subscriber (listener) program designed to help you learn the basics of ROS2 node communication.

## Getting Started
Follow these steps to set up and run the talker and listener nodes:

### Step 1: Create a Workspace
```bash
mkdir -p ~/ros2_ws/src
```

### Step 2: Build the Workspace
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Step 3: Clone and Source the Repository
```bash
cd ~/ros2_ws/src
git clone https://github.com/KarthikeshJG/talk.git
cd ..
```

### Step 4: Build and Source the Workspace
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Step 5: Running the Nodes

#### In the First Terminal (Publisher Node)
```bash
ros2 run talk pub
```

#### In the Second Terminal (Subscriber Node)
```bash
ros2 run talk sub
```

### Enjoy!
You should now see the talker node publishing messages and the listener node receiving and displaying them.

## Contributing
Feel free to submit issues or pull requests to improve this example or add new features.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

