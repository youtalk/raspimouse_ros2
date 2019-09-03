# raspimouse_ros2
ROS 2 navigation pakcages for Raspberry Pi Mouse v3

## OS and ROS 2 set up

First of all, you need to install Ubuntu 18.04 and ROS 2 Dashing Diademata on your Raspberry Pi 3 B+ and PC.

Please refer the official ROS 2 installation process: https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/

## Package build for Raspberry Pi 3 B+

### Raspberry Pi Mouse driver installation

```
git clone https://github.com/rt-net/RaspberryPiMouse.git
cd RaspberryPiMouse/src/drivers
make
sudo make install
sudo insmod rtmouse.ko
sudo usermod -aG dialout $USER
sudo chmod 666 /dev/rt*
```

### raspimouse_ros2 build

```
mkdir -p ~/ros/dashing/src
cd ~/ros/dashing/src
git clone git@github.com:youtalk/raspimouse_ros2.git -b ignore-cartographer-navigation2
git submodule update --init
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source ~/ros/dashing/install/setup.bash
```

## Package build for PC

### raspimouse_ros2 build

```
mkdir -p ~/ros/dashing/src
cd ~/ros/dashing/src
git clone git@github.com:youtalk/raspimouse_ros2.git
git submodule update --init
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source ~/ros/dashing/install/setup.bash
```

## Keyboard teleoperation

### Raspberry Pi 3 B+

```
ros2 launch raspimouse_bringup robot.launch.py
```

### PC

Enable Raspberry Pi Mouse

```
ros2 lifecycle set raspimouse_driver configure && \
ros2 lifecycle set raspimouse_driver activate && \
ros2 service call /motor_power std_srvs/SetBool '{data: true}'
```

Run Rviz2

```
ros2 launch raspimouse_bringup rviz2.launch.py
```

Run teleop_twist_keyboard

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
