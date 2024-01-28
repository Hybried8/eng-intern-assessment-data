import unittest
import sqlite3

class TestSQLQueries(unittest.TestCase):

    def setUp(self):
        # Establish a connection to your SQLite database
        self.conn = sqlite3.connect('shopify.db') 
        self.cur = self.conn.cursor()

    def tearDown(self):
        # Close the database connection
        self.cur.close()
        self.conn.close()

    def execute_and_test_query(self, path, query_number, expected_result):
        # Read SQL query from file
        with open(path, 'r') as file:
            sql_query = file.read()
        
        queries = sql_query.strip().split(';')
        selected_query = queries[query_number - 1].strip()
        self.cur.execute(selected_query)
        
        # Retrieve results and compare with expected result
        result = self.cur.fetchall()
        self.assertEqual(result, expected_result, f"{path}.{query_number}: Query output doesn't match expected result.")

    def test_task1(self):
        # Task 1: Example SQL query in task1.sql
        # Test case 1: Ensure the correct number of products is returned
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
        # Test case 1: Ensure products with a rating of 5.0 are returned
        self.execute_and_test_query('sql/task2.sql', 1, [(1, 'Smartphone X', 5.0), (4, 'Smart TV', 5.0),
                                                         (7, 'Coffee Maker', 5.0), (11, 'Yoga Mat', 5.0),
                                                         (15, 'Mountain Bike', 5.0)])

        # Test case 2: Ensure no products are returned (non-existent rating)
        self.execute_and_test_query('sql/task2.sql', 2, [])

        # Test case 3: Ensure no products are returned (no rating specified)
        self.execute_and_test_query('sql/task2.sql', 3, [])

        # Test case 4: Ensure no products are returned (empty table)
        self.execute_and_test_query('sql/task2.sql', 4, [])

        # Additional test cases for task2
        # Test case 5: Ensure all products are returned
        self.execute_and_test_query('sql/task2.sql', 5, [(1, 'Smartphone X', 5.0), (2, 'Wireless Headphones', 4.0),
                                                         (3, 'Laptop Pro', 3.0), (4, 'Smart TV', 5.0),
                                                         (5, 'Running Shoes', 2.0), (6, 'Designer Dress', 4.0),
                                                         (7, 'Coffee Maker', 5.0), (8, 'Toaster Oven', 3.0),
                                                         (9, 'Action Camera', 4.0), (10, 'Board Game Collection', 1.0),
                                                         (11, 'Yoga Mat', 5.0), (12, 'Skincare Set', 4.0),
                                                         (13, 'Vitamin C Supplement', 2.0), (14, 'Weighted Blanket', 3.0),
                                                         (15, 'Mountain Bike', 5.0), (16, 'Tennis Racket', 4.0)])

        # Test case 6: Ensure products with ratings 4.0 and 5.0 are returned
        self.execute_and_test_query('sql/task2.sql', 6, [(2, 'Wireless Headphones', 4.0), (15, 'Mountain Bike', 5.0)])

    def test_task3(self):
        # Task 3: Example SQL query in task3.sql
        # Test case 1: Ensure departments with their total sales amounts are returned
        self.execute_and_test_query('sql/task3.sql', 1, [(8, 'Sports & Outdoors', 155.0), (4, 'Home & Kitchen', 145.0),
                                                         (1, 'Electronics', 125.0)])

        # Test case 2: Ensure departments with their total sales amounts are returned (excluding Electronics)
        self.execute_and_test_query('sql/task3.sql', 2, [(4, 'Home & Kitchen', 145.0), (1, 'Electronics', 125.0)])

        # Test case 3: Ensure departments with their total sales amounts are returned (excluding Home & Kitchen)
        self.execute_and_test_query('sql/task3.sql', 3, [(8, 'Sports & Outdoors', 155.0), (1, 'Electronics', 125.0)])

        # Test case 4: Ensure departments with their total sales amounts are returned (excluding Sports & Outdoors)
        self.execute_and_test_query('sql/task3.sql', 4, [(8, 'Sports & Outdoors', 155.0), (4, 'Home & Kitchen', 145.0)])

        # Additional test cases for task3
        # Test case 5: Ensure only Sports & Outdoors department is returned
        self.execute_and_test_query('sql/task3.sql', 5, [(8, 'Sports & Outdoors', 155.0)])

        # Test case 6: Ensure only Home & Kitchen department is returned
        self.execute_and_test_query('sql/task3.sql', 6, [(4, 'Home & Kitchen', 145.0)])

if __name__ == '__main__':
    unittest.main()
