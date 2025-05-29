#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from numpy import random

class BatteryPublisherNode(Node):
    def __init__(self):
        super().__init__("Battery_publisher")
        self.battery_publisher_ = self.create_publisher(Float64MultiArray,"readings",10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
       
    
    def timer_callback(self):
        msg = Float64MultiArray()
        x = (random.uniform(0.05, 2))
        y = (random.uniform(0.05, 2))
        z = (random.uniform(0.05, 2))
        
        msg.data = [float(x), float(y), float(z)]

        self.battery_publisher_.publish(msg)
        self.get_logger().info(f"voltage: {x:.2f}, current: {y:.2f}, temperature: {z:.2f}")
        
    
def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()

