import rclpy
from rclpy.node import Node
from battery_msg.msg import BatteryStatus
from std_msgs.msg import String

class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(BatteryStatus,"readings",self.callback_number,10)
        self.get_logger().info("Number counter has been started")
        self.battery_publisher_ = self.create_publisher(String,'battery_alert', 10)

    def callback_number(self, msg):
        if msg.voltage < 10.5:
            alert = "LOW"
        if msg.temperature > 60:
            alert = "OVERHEAT"
        else:
            alert = "OK"

        alert_msg = String()
        alert_msg.data = alert
        
        self.get_logger().info(f"Přijato: V={msg.voltage:.2f} V, I={msg.current:.2f} A, T={msg.temperature:.2f} °C,{alert}")
        self.battery_publisher_.publish(alert_msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Subscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()
