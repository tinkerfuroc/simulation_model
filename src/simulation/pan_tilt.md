## 可能要安装的包

```
sudo apt-get install ros-melodic-gazebo-ros-control
sudo apt-get install ros-melodic-joint-state-controller
sudo apt-get install ros-melodic-effort-controllers
```

## 代码说明

官方教程链接：[gazebo Tutorial: ROS Control](http://gazebosim.org/tutorials?tut=ros_control&cat=connect_ros)

- < type > 传动器的种类，目前仅transmission_interface/SimpleTransmission可以实现

- < hardwareInterface > 在 < actuator >和 < joint >标签内部，gazebo_ros_control plugin 加载什么类型的硬件接口 （position, velocity or effort interfaces）

  

