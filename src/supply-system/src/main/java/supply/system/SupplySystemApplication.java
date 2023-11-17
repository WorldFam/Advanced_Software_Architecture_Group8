package supply.system;

import org.flywaydb.core.Flyway;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SupplySystemApplication {

	public static void main(String[] args) {
		SpringApplication.run(SupplySystemApplication.class, args);
		Flyway flyway = Flyway.configure().load();
		flyway.migrate();
	}
}
