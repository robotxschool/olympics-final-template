# parameters
ARG REPO_NAME="ADO-Final"
ARG DESCRIPTION="ADO-Finale Template"
ARG MAINTAINER="Chaika Konstantin (pro100kot14@gmail.com)"

# ==================================================>
# ==> Do not change the code below this line

# define base image
FROM pro100kot/ado-ros:v2-amd64
# cp solution replacing default dummy one
COPY ./solution/solution.py /code/catkin_ws/src/ADO-ROS/packages/circle_drive/scripts/solution/solution.py
