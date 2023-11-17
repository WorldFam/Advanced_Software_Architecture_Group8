package org.example;

import java.sql.*;

public class SupplyChainDatabaseManager {
    public void ConnectAndQueryDatabase() {
        // Define your database connection URL and credentials
        String jdbcUrl = "jdbc:mysql://localhost:3306/supply_chain_management_system";
        String jdbcUser = "root";
        String jdbcPassword = "admin";

        try {
            // Establish a connection to the database
            Connection connection = DriverManager.getConnection(jdbcUrl, jdbcUser, jdbcPassword);

            // Create a SQL statement
            Statement statement = connection.createStatement();

            // Define your SQL query to select data from a specific column
            String query = "SELECT resource_name FROM inventory LIMIT 10"; // Adjust the query as needed

            // Execute the query and retrieve the result set
            ResultSet resultSet = statement.executeQuery(query);

            // Iterate through the result set and print the values
            while (resultSet.next()) {
                String columnValue = resultSet.getString("resource_name");
                System.out.println(columnValue);
            }

            // Close the result set, statement, and connection
            resultSet.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
