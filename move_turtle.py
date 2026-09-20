# move_turtle.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


def main(args=None):
    rclpy.init(args=args)
    node = Node('move_turtle')
    publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 1.0

    timer = node.create_timer(0.5, lambda: publisher.publish(msg))
    rclpy.spin(node)


if __name__ == '__main__':
    main()