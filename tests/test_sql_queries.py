import unittest

class TestSQLQueries(unittest.TestCase):

        def setUp(self):
        # Establish a connection to your SQLite database
        self.conn = sqlite3.connect('shopify.db')  # Replace with the path to your SQLite database file
        self.cur = self.conn.cursor()

    def tearDown(self):
        # Close the database connection
        self.cur.close()
        self.conn.close()

    def execute_and_test_query(self, path, query_number, expected_result):
        # Task: Example SQL query in task1.sql
        with open(path, 'r') as file:  # Adjust the path as necessary
            sql_query = file.read()
        
        sql_query = sql_query.split(';')[query_number-1]
        
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        
        self.assertEqual(result, expected_result, f"{path}.{query_number}: Query output doesn't match expected result.")


    def test_task1(self):
        # Task 1: Example SQL query in task1.sql
        with open('/sql/task1.sql', 'r') as file:
            sql_query = file.read()

        self.cur.execute(sql_query)
        result = self.cur.fetchall()

        # Define expected outcome for Task 1 and compare
         self.execute_and_test_query('sql/task1.sql', 1, [(15, 'Mountain Bike'), (16, 'Tennis Racket')])
    
        # Test case 2: Ensure all users with a valid subscription are returned
        self.execute_and_test_query('sql/task1.sql', 2, [(1, 'johndoe', 1), (2, 'janesmith', 1), (3, 'maryjones', 1)])
        
        # Test case 3: Ensure all products with a rating of 4 or higher are returned
        self.execute_and_test_query('sql/task1.sql', 3, [(1, 'Smartphone X', 5.0), (2, 'Wireless Headphones', 4.0),
                                                         (4, 'Smart TV', 5.0), (6, 'Designer Dress', 4.0),
                                                         (7, 'Coffee Maker', 5.0), (9, 'Action Camera', 4.0),
                                                         (11, 'Yoga Mat', 5.0), (12, 'Skincare Set', 4.0),
                                                         (16, 'Tennis Racket', 4.0)])
        
        # Test case 4: Ensure the top 5 users with the highest total purchase amounts are returned
        self.execute_and_test_query('sql/task1.sql', 4, [(12, 'jasonrodriguez', 160.0), (4, 'robertbrown', 155.0),
                                                         (8, 'chrisharris', 150.0), (24, 'jamesrogers', 150.0),
                                                         (17, 'olivialopez', 145.0)])
    

    def test_task2(self):
        # Task 2: Example SQL query in task2.sql
        with open('/sql/task2.sql', 'r') as file:
            sql_query = file.read()

        self.cur.execute(sql_query)
        result = self.cur.fetchall()

        self.execute_and_test_query('sql/task2.sql', 1, [(1, 'Smartphone X', 5.0), (4, 'Smart TV', 5.0), 
                                (7, 'Coffee Maker', 5.0), (11, 'Yoga Mat', 5.0), (15, 'Mountain Bike', 5.0)])
        
        self.execute_and_test_query('sql/task2.sql', 2, [])
        self.execute_and_test_query('sql/task2.sql', 3, [])
        self.execute_and_test_query('sql/task2.sql', 4, [])
        
        # Additional test cases for task2
        self.execute_and_test_query('sql/task2.sql', 5, [(3, 'Laptop Pro', 3.0), (5, 'Running Shoes', 2.0), (6, 'Designer Dress', 4.0), (8, 'Toaster Oven', 3.0), (9, 'Action Camera', 4.0), (10, 'Board Game Collection', 1.0), (12, 'Skincare Set', 4.0), (13, 'Vitamin C Supplement', 2.0), (14, 'Weighted Blanket', 3.0), (16, 'Tennis Racket', 4.0)])
        
        self.execute_and_test_query('sql/task2.sql', 6, [(2, 'Wireless Headphones', 4.0), (15, 'Mountain Bike', 5.0)])


    # Add more test methods for additional SQL tasks
    def test_task3(self):
        # Task 3: Example SQL query in task3.sql
        with open('/sql/task3.sql', 'r') as file:
            sql_query = file.read()

        self.cur.execute(sql_query)
        result = self.cur.fetchall()

        self.execute_and_test_query('sql/task3.sql', 1, [(8, 'Sports & Outdoors', 155.0), (4, 'Home & Kitchen', 145.0), (1, 'Electronics', 125.0)])
        
        self.execute_and_test_query('sql/task3.sql', 2, [(4, 'Home & Kitchen', 145.0), (1, 'Electronics', 125.0)])
        
        self.execute_and_test_query('sql/task3.sql', 3, [(8, 'Sports & Outdoors', 155.0), (1, 'Electronics', 125.0)])
        
        self.execute_and_test_query('sql/task3.sql', 4, [(8, 'Sports & Outdoors', 155.0), (4, 'Home & Kitchen', 145.0)])
        
        # Additional test cases for task3
        self.execute_and_test_query('sql/task3.sql', 5, [(8, 'Sports & Outdoors', 155.0)])
        
        self.execute_and_test_query('sql/task3.sql', 6, [(4, 'Home & Kitchen', 145.0)])

if __name__ == '__main__':
    unittest.main()
