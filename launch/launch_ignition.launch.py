from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start Ignition Gazebo
        Node(
            package='ros_gz_sim',
            executable='create',
            name='gz_sim',
            output='screen',
            arguments=['-r', '-v', '4']  # -r = reset world, -v 4 = verbose
        ),

        # Spawn your robot from the robot_description topic
        Node(
            package='ros_gz_sim',
            executable='create',
            name='spawn_entity',
            output='screen',
            arguments=[
                '-topic', 'robot_description',
                '-name', 'my_bot'
            ]
        ),

        # Publish robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': True}],
        ),
    ])
