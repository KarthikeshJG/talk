# talk
Basic ROS2 Talker and Listener Program to  learn.

**Step-1**
Create a Workspace 
mkdir -p ~/ros2_ws/src

**Step-2**
Build the Workspace
cd ~/ros2_ws
colcon build
source install/setup.bash

**step-3**
Clone and Source the Repo
cd ~/ros2_ws/src
git clone https://github.com/KarthikeshJG/talk.git
cd ..

**step-4**
Build and Source the Workspace
cd ~/ros2_ws
colcon build
source install/setup.bash

**Step-5**
Running the Nodes

1st Terminal
ros2 run talk pub

Open 2nd Terminal
ros2 run talk sub

Enjoy!
