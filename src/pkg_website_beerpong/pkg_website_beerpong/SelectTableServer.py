from select_table_interfaces.srv import TableSelect
import rclpy
from rclpy.node import Node
from SelectedTable import SelectedTable
from threading import Timer


class MinimalService(Node):

    def __init__(self):
        rclpy.init(args=None)
        super().__init__('table_server')
        self.srv = self.create_service(TableSelect, 'table_server', self.selectedTable_callback)
        print("Node wurde initialisiert")

    def selectedTable_callback(self, request, response):
        response.table_id = SelectedTable.table_id
        #self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response
    
    def shutdown_node(self):
        rclpy.shutdown()
        print("Service zerstört")
        SelectedTable.table_id = 0


    def main(args=None):
        #rclpy.init(args=args)

        #minimal_service = MinimalService()
        print("Service erzeugt")
        #timer = Timer(50.0, minimal_service.shutdown_node)
        #timer.start()
        #print("Timer gestartet")


        #rclpy.spin(minimal_service)
        rclpy.spin('table_server')

        #rclpy.shutdown()
        #print("Service zerstört")
        #SelectedTable.table_id = 0

    

if __name__ == '__main__':
    main()