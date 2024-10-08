import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('nav_stack'),'config')
    map_dir = os.path.join(get_package_share_directory('nav_stack'),'maps')
    param_file = os.path.join(config_dir,'tb3_nav2_params.yaml')
    rviz_file = os.path.join(config_dir,'tb3.rviz')
    map_file = os.path.join(map_dir,'my_map.yaml')
    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([get_package_share_directory('turtlebot3_gazebo'),'/launch','/turtlebot3_world.launch.py'])
        # ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch','/bringup_launch.py']),
            launch_arguments={
            'map':map_file,
            'params_file':param_file}.items()
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2_node',
            arguments=['-d',rviz_file],
            output='screen'
        )
    ])