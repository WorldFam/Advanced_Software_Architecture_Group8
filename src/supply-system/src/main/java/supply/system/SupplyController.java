package supply.system;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SupplyController {
    @PostMapping(value = "/order", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> supplyOrder(@RequestBody Order order) {
        // Create service for calculate amount leftover and returning appropriate result
        return new ResponseEntity<>(HttpStatus.OK);
    }

}
