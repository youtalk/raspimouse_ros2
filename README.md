# raspimouse_ros2
ROS 2 navigation pakcages for Raspberry Pi Mouse V3

## OS and ROS 2 set up

First of all, you need to install Ubuntu 18.04 and ROS 2 Dashing Diademata on your Raspberry Pi 3 B and PC.
Please refer the official ROS 2 installation process: https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/

### `colcon` and `rosdep` set up

```
sudo apt install python3-colcon-common-extensions python3-rosdep python3-argcomplete
sudo rosdep init
rosdep update
```

### `ROS_DOMAIN_ID` network configuration

Set the environmental variable `ROS_DOMAIN_ID` to specify your network configuration.
The `ROS_DOMAIN_ID` is a number between `0` and `255`.

```
export ROS_DOMAIN_ID=XXX
```

## Package build for Raspberry Pi 3 B

### Raspberry Pi Mouse driver installation

```
git clone https://github.com/rt-net/RaspberryPiMouse.git
cd RaspberryPiMouse/src/drivers
make
sudo make install
sudo insmod rtmouse.ko
sudo usermod -aG dialout $USER
```

### raspimouse_ros2 build

```
mkdir -p ~/ros/dashing/src
cd ~/ros/dashing/src
git clone https://github.com/youtalk/raspimouse_ros2.git -b ignore-cartographer-navigation2
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
git clone https://github.com/youtalk/raspimouse_ros2.git
git submodule update --init
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source ~/ros/dashing/install/setup.bash
```

## Keyboard teleoperation

Run Raspberry Pi Mouse and RPLiDAR A1M8 drivers.

### Raspberry Pi 3 B

```
ros2 launch raspimouse_bringup robot.launch.py
```

### PC

Enable Raspberry Pi Mouse.

```
ros2 lifecycle set raspimouse_driver configure && \
ros2 lifecycle set raspimouse_driver activate && \
ros2 service call /motor_power std_srvs/SetBool '{data: true}'
```

Run Rviz2.

```
ros2 launch raspimouse_bringup rviz2.launch.py
```

Run `teleop_twist_keyboard`.

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Note that the default linear speed is too fast.
Please decrease the linear speed to 0.15 [m/s] or lower by pressing `x` key several times.

## Cartographer SLAM

### Raspberry Pi 3 B

Do the same as above.

### PC

First do the same as above.
Then move around a floor while recording the bag file for SLAM data.

```
sudo apt install 'ros-dashing-ros2bag*' 'ros-dashing-rosbag2*'
ros2 bag record -a -o ./raspimouse_slam.bag
```

Run `raspimouse_cartographer` to generate 2D map.

```
ros2 launch raspimouse_cartographer cartographer.launch.py
```

Play the bag file recorded before.

```
ros2 bag play ~/raspimouse_slam.bag
```

Save map files if the quaility of the map on RViz2 is acceptable.

```
ros2 run nav2_map_server map_saver -f ~/.ros/map
```

Note that a sample bag file and map data are stored following directories.

- Bag file: https://github.com/youtalk/raspimouse_bags/tree/master/raspimouse_slam.bag
- Map data: https://github.com/youtalk/raspimouse_ros2/tree/master/raspimouse_navigation2/map

## Navigation 2

TBA
