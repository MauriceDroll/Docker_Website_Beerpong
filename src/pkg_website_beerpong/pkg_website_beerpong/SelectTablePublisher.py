import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16  # Importiere die Nachrichtenart, die du verwenden möchtest
from SelectedTable import SelectedTable

class SelectTablePublisher(Node):
    def __init__(self):
        print("bin in der Init")
        super().__init__('selected_table_publisher')
        self.publisher_ = self.create_publisher(Int16, 'selected_table', 1)
        timer_period = 2.0  # Sekunden
        self.timer_callback()
        #self.i = 0
        
    def timer_callback(self):
        msg = Int16()
        msg.data = SelectedTable.table_id
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

        #self.i += 1
    
    @staticmethod
    def main(args=None):
        rclpy.init(args=args)
        node = SelectTablePublisher()
        try:
            rclpy.spin(node)
            node.destroy_node()
            rclpy.shutdown()
        except KeyboardInterrupt:
            pass
        finally:
            node.destroy_node()
            rclpy.shutdown()
            self.get_logger().info('Node wurde zerstört!')

if __name__ == '__main__':
    main()
