import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    rviz = IncludeLaunchDescription(
        os.path.join(get_package_share_directory("urdf_tutorial"), "launch", "display.launch.py"),
        launch_arguments={"model": "/home/pulak/all_ros2_workspace/assistive_claw_workspace/src/assistive_claw/urdf/arm.urdf.xacro"}.items()
    )


    return LaunchDescription([
        rviz
    ])

