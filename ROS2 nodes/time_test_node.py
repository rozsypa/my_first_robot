#this is first node to test time and callbacks. nothing fancy
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time


class TimeTestNode(Node):
    def __init__(self):
        super().__init__('time_test_node')
        self.timer = self.create_timer(0.05,self.my_callback)
        self.publisher = self.create_publisher(Float64,"chatter",10)
        self.previous_time = None
        self.current_time = None

    def my_callback(self):

        start_time = time.perf_counter()
        self.current_time = time.perf_counter()
        #time.sleep(0.005)
        if self.previous_time is None:
            self.previous_time = self.current_time
            return
        else:
            dt = self.current_time - self.previous_time
            self.previous_time = self.current_time

            msg = Float64()
            msg.data = dt
            self.publisher.publish(msg)
            self.get_logger().info(f'Time test node published {dt} seconds')
            end_time = time.perf_counter()
            time_diff = (end_time - start_time)
            self.get_logger().info(f'Time test node published {time_diff} seconds')

# the period of callback is set on 50ms. Execution length of callback cca 0.6-0.9ms. We have big buffer for our callback

def main(args=None):
    rclpy.init(args=args)
    node = TimeTestNode()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()