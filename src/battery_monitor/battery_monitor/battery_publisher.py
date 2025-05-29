#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from numpy import random
from battery_msg.msg import BatteryStatus

class BatteryPublisherNode(Node):
    def __init__(self):
        super().__init__("Battery_publisher")
        self.battery_publisher_ = self.create_publisher(BatteryStatus,"readings",10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
       
    
    def timer_callback(self):
        msg = BatteryStatus()
        msg.temperature = (random.uniform(0.05, 2))
        msg.voltage = (random.uniform(0.05, 2))
        msg.current = (random.uniform(0.05, 2))
  
        self.battery_publisher_.publish(msg)
        self.get_logger().info(f"voltage: {msg.voltage:.2f}, current: {msg.current:.2f}, temperature: {msg.temperature:.2f}")
        
    
def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()

