# /*******************************************************************************
# * Copyright 2019 Yutaka Kondo
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *     http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *******************************************************************************/

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node


def generate_launch_description():
    urdf = os.path.join(
        get_package_share_directory('raspimouse_description'),
        'urdf', 'raspimouse.urdf')

    return LaunchDescription([
        Node(
            package='raspimouse',
            node_executable='raspimouse',
            node_name='raspimouse_driver',
            output='screen'),
        Node(
            package='rplidar_ros',
            node_executable='rplidar_node',
            node_name='raspimouse_rplidar_driver',
            output='screen'),
        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            node_name='raspimouse_robot_state_publisher',
            output='screen',
            arguments=[urdf]),
    ])
