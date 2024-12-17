
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Replace with your message type if needed


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('listen')  # Name of the node
        self.subscription = self.create_subscription(
            String,                  # Message type
            'chatter',                 # Topic name
            self.listener_callback,  # Callback function
            10                       # QoS (queue size)
        )
        self.subscription  # Prevent unused variable warning
        self.get_logger().info("Subscriber node has been started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: '{msg.data}'")  # Logs the received message


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    try:
        rclpy.spin(node)  # Keep the node running
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
