#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration,Command,PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    launch_file_dir = os.path.join(get_package_share_directory('diff_robot_config'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')


    world = os.path.join(
        get_package_share_directory('diff_robot_config'),
        'world',
        'home.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )
    

    
    gz_spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'spawn_rover.launch.py')
        )
        
    )
    
    
    gz_robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        )
    )    
    ld = LaunchDescription()


    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    ld.add_action(gz_spawn_robot)
    ld.add_action(gz_robot_state_publisher)

# load and START the controllers in launch file
	
	

    return ld
