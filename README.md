# ready2educate cell tutorial

**Note:** To set up the cell, if not done already, follow the instructions in the `cell_setup` branch of this
repository.

## Exercise 1: setup your environment and run example

1. Clone or download and unpack this repository
2. Navigate to the `r2e_tutorial` directory
3. Build container

```bash
./start_docker.sh
```

You should now be inside the container and see following prompt:

```
robot@<pc_name>:~/ros2_ws$
```

4. Start robot driver and visualization

```bash
ros2 launch kuka_kr3_cell_description cell.launch.py
```

This should open up RViz and you should see the robot model.
You can play around with MoveIt! and the robot should move in the visualization.

5. To run the example application, open a new terminal and connect to running container

```bash
docker exec -it r2e bash
```

6. Build workspace

```bash
colcon build
```

7. Source workspace

```bash
source install/setup.bash
```

8. Run example

```bash
ros2 run r2e_tutorial example
```

## Exercise 2 (optional): Haus vom Nikolaus

Write a program that draws the "Haus vom Nikolaus" with the robot in the air.

You can use the ```r2e_tutorial/src/example.py``` file as a starting point.

1. Create a new file ```r2e_tutorial/src/house.py```
2. Write a program that draws the "Haus vom Nikolaus" with the robot in the air.
   You can start by copying the example program and modifying it.
3. Before you can run your program, you need to add it to the ```r2e_tutorial/setup.py``` file.
   Add the following lines to the ```entry_points['console_scripts']``` section:

```python
'house = r2e_tutorial.house:main'
```

This is a list, don't forget the comma between the entries.

This way, you can test your code by running ```ros2 run r2e_tutorial house``` after building the workspace.

4. Build the workspace. Make sure you are in the container and in the ```ros2_ws``` directory.

```bash
colcon build
```

5. Source the workspace

```bash
source install/setup.bash
```

6. Run your program

```bash
ros2 run r2e_tutorial house
```

## Exercise 3 (optional): Implement methods for picking and placing objects

In this exercise, you will implement methods for picking and placing objects.
You can use ```complex_movement_example(robot, pose)``` from ```r2e_tutorial/src/example.py``` as a starting point.

Consider what types of motion is required for picking and placing objects (pre-pick, post-pick poses, approach, etc.).
Create a new file ```r2e_tutorial/src/pick_and_place.py``` and implement the following methods:

```python
pick_cartesian(robot, pose)
pick_joint_position(robot, joint_positions)
place_cartesian(robot, pose)
place_joint_position(robot, joint_positions)
```

## Exercise 4 (optional): Implement a method for building a pyramid of 6 blocks

In this exercise, you will implement a program for building and disassembling a pyramid of 6 blocks
(3 blocks in the first row, 2 blocks in the second row, 1 block in the third row).
Use the methods you implemented in the previous exercise.

Create a new file for your program, just like in exercise 2. Don't forget to add the program to the ```setup.py``` file.
Before testing your code, build the workspace and source it.

The goal is to run the code on the real robot. You will be able to pick up blocks from the slide and place them on the
table.
To determine the pick and place poses you can for example move the robot to the desired position using the smartHMI,
start the robot driver (see next exercise) and use `node.get_transform` as in the example program to get the current
pose of the robot, or by simply using `ros2 topic echo /joint_states` to get the current joint positions. Alternatively,
you can implement your own logic in python to adapt the poses without using the smartHMI.

Neither the blocks nor the slide is available in the simulation.

## Exercise 5: Test your code on the real robot

Once you are in the lab, you can test your code on the real robot.

### Start Hardware Interface on Robot

Before connecting to the real robot, you need to start the driver on the robot. Check out the
instructions [here](https://github.com/IRAS-HKA/r2e_tutorial/tree/cell_setup?tab=readme-ov-file#start-hardware-interface-on-robot)

### Run your code on the real robot

Use one of the PCs in the lab, set up the workspace as before,
**EXCEPT!!!** before running ```./start_docker.sh```, edit it and set ```DOMAIN_ID``` in line 4 to the last 2 digits of
the IP of the Roboter-Steuerung.

Adapt your code: initialize ```RobotClient``` with ```is_simulation=True```.

To connect to the real robot run

```bash
ros2 launch kuka_kr3_cell_description cell.launch.py use_fake_hardware:=false robot_ip:=<robot_ip>
```

where ```<robot_ip>``` is the IP address of the Roboter-Steuerung.

Run your code as before.