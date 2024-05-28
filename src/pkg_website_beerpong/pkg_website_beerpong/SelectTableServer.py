from select_table_interfaces.srv import TableSelect
import rclpy
from rclpy.node import Node
from SelectedTable import SelectedTable


class MinimalService(Node):

    def __init__(self):
        super().__init__('table_server')
        self.srv = self.create_service(TableSelect, 'table_server', self.selectedTable_callback)

    def selectedTable_callback(self, request, response):
        response.table_id = SelectedTable.table_id
        #self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


    def main(args=None):
        rclpy.init(args=args)

        minimal_service = MinimalService()

        rclpy.spin(minimal_service)

        rclpy.shutdown()
        SelectedTable.table_id = 0


if __name__ == '__main__':
    main()