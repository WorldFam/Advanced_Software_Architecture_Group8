# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set the working directory to /app
WORKDIR /app

# Copy the application JAR file into the container
COPY out/artifacts/SupplyChainManagementSystem_jar/SupplyChainManagementSystem.jar ./app.jar

# Run the application when the container starts
CMD ["java", "-jar", "app.jar"]
