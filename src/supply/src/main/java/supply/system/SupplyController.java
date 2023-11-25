package supply.system;

import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

import javax.naming.InsufficientResourcesException;

@RestController
@AllArgsConstructor
public class SupplyController {

    private final SupplyService supplyService;

    @PostMapping(value = "/order", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> supplyOrder(@RequestBody Order order) throws InsufficientResourcesException {
        supplyService.supply(order);
        return new ResponseEntity<>(HttpStatus.OK);
    }

}
