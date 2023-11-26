CREATE TABLE Resource(
    id INT AUTO_INCREMENT PRIMARY KEY,
    size NVARCHAR(255) UNIQUE NOT NULL,
    amount BIGINT NOT NULL DEFAULT 0
)