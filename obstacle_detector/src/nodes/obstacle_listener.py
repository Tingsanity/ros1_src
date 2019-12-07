import rospy
import numpy as np
import csv
from obstacle_detector.msg import Obstacles,CircleObstacle,SegmentObstacle

class obstacle_sub:
    def __init__(self):
        rospy.init_node("drawer")
        
    def run(self):
        self.sub = rospy.Subscriber("obstacles2",Obstacles,self.obstaclecallback)
        rospy.spin()

    def obstaclecallback(self,data):
        self.circle_vec = data.circles
        
        for circle in self.circle_vec:
            with open("test.csv","a") as csvfile:
                writer =csv.writer(csvfile)
                print(circle.id)
                print(circle.center.x)
                print(circle.center.y)
                print(circle.radius)
                print(circle.true_radius)
                writer.writerow([circle.id,circle.center.x,circle.center.y,circle.radius,circle.true_radius])



if __name__ == "__main__":
    print("start")
    o = obstacle_sub()
    o.run()